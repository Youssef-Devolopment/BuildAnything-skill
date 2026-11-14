# Update the BuildAnything skill clone (and manage automatic daily updates).
# Usage (run from anywhere - it operates on the clone next to this script):
#   .\update.ps1             # fetch + fast-forward pull, show what changed
#   .\update.ps1 -Status     # check only: up to date or behind? (changes nothing)
#   .\update.ps1 -Schedule   # register a hidden daily Windows task that updates for you
#   .\update.ps1 -Unschedule # remove that task
#
# Clones (README Option 1/2) update via git. Copy installs (Option 3/4) cannot
# self-update: re-run install.ps1 -Force from a fresh download instead.

param(
    [switch]$Status,
    [switch]$Schedule,
    [switch]$Unschedule
)

$repo = $PSScriptRoot
$taskName = "BuildAnything-Skill-Update"

function Say([string]$msg, [string]$color = "Gray") { Write-Host $msg -ForegroundColor $color }

# --- Schedule / unschedule the daily Windows task -----------------------------
if ($Schedule -or $Unschedule) {
    if ($env:OS -ne "Windows_NT") {
        Say "Scheduled tasks are Windows-only. On macOS/Linux add a crontab line instead:" Cyan
        Say "  0 9 * * * cd `"$repo`" && git pull --quiet" Cyan
        exit 2
    }
    if ($Unschedule) {
        schtasks /Delete /TN $taskName /F 2>$null | Out-Null
        if ($LASTEXITCODE -eq 0) { Say "Removed scheduled task '$taskName'." Green; exit 0 }
        Say "No scheduled task '$taskName' found - nothing to remove." Yellow
        exit 0
    }
    $ps = (Get-Command powershell -ErrorAction SilentlyContinue).Source
    if (-not $ps) { $ps = "powershell.exe" }
    $tr = "$ps -NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -File `"$repo\update.ps1`""
    schtasks /Create /SC DAILY /TN $taskName /TR $tr /ST 09:00 /F | Out-Null
    if ($LASTEXITCODE -ne 0) { Say "Failed to create the scheduled task (try an admin shell)." Red; exit 1 }
    Say "Scheduled: daily update at 09:00 (hidden window, only if there are new commits)." Green
    Say "Remove anytime with:  .\update.ps1 -Unschedule" Gray
    exit 0
}

# --- Not a clone? (copy install cannot self-update) --------------------------
if (-not (Test-Path (Join-Path $repo ".git"))) {
    Say "NOT A CLONE: no .git folder here - this looks like a copy install." Red
    Say "Copies cannot self-update. Either:" Yellow
    Say "  * re-run install.ps1 -Target <t> -Force from a fresh download, or" Yellow
    Say "  * install as a clone instead (README Option 1) to enable updates." Yellow
    exit 1
}

# --- Fetch and decide --------------------------------------------------------
git -C $repo fetch origin 2>$null | Out-Null
$behind = 0
$st = (git -C $repo status -sb) -join "`n"
if ($st -match "behind (\d+)") { $behind = [int]$Matches[1] }
$dirty = @(git -C $repo status --porcelain)

if ($Status) {
    if ($dirty.Count -gt 0) {
        Say "Local modifications present (commit or stash them before updating):" Yellow
        $dirty | ForEach-Object { Say "  $_" Yellow }
    }
    if ($behind -gt 0) {
        Say "$behind new commit(s) available on origin/main. Run:  .\update.ps1" Cyan
        exit 1
    }
    Say "Up to date with origin/main." Green
    exit 0
}

if ($dirty.Count -gt 0) {
    Say "ABORT: local modifications in this clone - will not overwrite your edits." Red
    Say "Commit or stash them first, then run .\update.ps1 again:" Yellow
    Say "  git -C `"$repo`" status -sb" Yellow
    exit 1
}

if ($behind -eq 0) {
    Say "Already up to date with origin/main." Green
    exit 0
}

$before = git -C $repo rev-parse HEAD
git -C $repo pull --ff-only --quiet 2>$null
if ($LASTEXITCODE -ne 0) {
    Say "Pull failed (not a fast-forward). Inspect and resolve, then retry:" Red
    Say "  git -C `"$repo`" log --oneline -5" Yellow
    exit 1
}
$after = git -C $repo rev-parse HEAD

Say "Updated $behind commit(s):" Cyan
git -C $repo log --oneline "$before..$after"
Say ""
Say "Restart OpenCode to load the new skill files." Green
exit 0
