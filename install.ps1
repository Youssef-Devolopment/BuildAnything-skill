# Install BuildAnything skills into an agent's skills directory.
# Usage:
#   .\install.ps1                 # OpenCode global (default)
#   .\install.ps1 -Target claude  # ~/.claude/skills
#   .\install.ps1 -Target agents  # ~/.agents/skills
#   .\install.ps1 -Force           # overwrite existing skills

param(
    [ValidateSet("opencode", "claude", "agents")]
    [string]$Target = "opencode",
    [switch]$Force
)

$home_ = $HOME
$dest = switch ($Target) {
    "opencode" { Join-Path $home_ ".config/opencode/skills" }
    "claude"   { Join-Path $home_ ".claude/skills" }
    "agents"   { Join-Path $home_ ".agents/skills" }
}

$source = $PSScriptRoot
# Skill folders = directories containing SKILL.md at their root
$skills = Get-ChildItem -Path $source -Directory |
    Where-Object { Test-Path (Join-Path $_.FullName "SKILL.md") }

if (-not $skills) {
    Write-Error "No skills found next to install.ps1."
    exit 1
}

New-Item -ItemType Directory -Force -Path $dest | Out-Null

$installed = 0
$skipped = 0
foreach ($skill in $skills) {
    $targetPath = Join-Path $dest $skill.Name
    if ((Test-Path $targetPath) -and -not $Force) {
        Write-Host "skip    $($skill.Name) (exists — use -Force to overwrite)" -ForegroundColor Yellow
        $skipped++
        continue
    }
    if (Test-Path $targetPath) {
        Remove-Item -Recurse -Force $targetPath
    }
    Copy-Item -Recurse $skill.FullName $targetPath
    Write-Host "install $($skill.Name)" -ForegroundColor Green
    $installed++
}

Write-Host ""
Write-Host "Done: $installed installed, $skipped skipped -> $dest" -ForegroundColor Cyan
Write-Host "Restart your agent session to pick up the changes."
