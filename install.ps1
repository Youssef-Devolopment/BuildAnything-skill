# Install BuildAnything skills into an agent's skills directory.
# Usage (run from anywhere - it reads the skill folders next to this script):
#   .\install.ps1                 # OpenCode global (~/.config/opencode/skills)
#   .\install.ps1 -Target claude  # ~/.claude/skills (Claude Code)
#   .\install.ps1 -Target agents  # ~/.agents/skills (other agents)
#   .\install.ps1 -Force          # overwrite existing skills
#   .\install.ps1 -Doctor         # detect duplicate/conflicting installs and print the fix
#
# Install methods are alternatives - use ONE of: clone (README Option 1),
# clone+register (Option 2), or copy (this script). Never two at once;
# run -Doctor if unsure whether you already installed.

param(
    [ValidateSet("opencode", "claude", "agents")]
    [string]$Target = "opencode",
    [switch]$Force,
    [switch]$Doctor
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

if ($Doctor) {
    Write-Host "BuildAnything install doctor" -ForegroundColor Cyan
    Write-Host "Checking every place an agent could load these skills from..."
    Write-Host ""

    $skillIds = @($skills.Name)
    $loaded = @()   # locations where the skills are actually picked up

    # 1) This repo itself, if it sits inside a discoverable skills folder
    if ($source -match '[\\/]\.config[\\/]opencode[\\/]skills[\\/]|[\\/]\.claude[\\/]skills[\\/]|[\\/]\.agents[\\/]skills[\\/]') {
        $loaded += [pscustomobject]@{ Kind = "auto-discovery"; Path = $source }
    }

    # 2) Copy installs: skill-ID folders inside any skills root (other than this repo)
    #    Checks both direct children and one level deep (grouping dirs like <clone>/build-anything)
    foreach ($root in @((Join-Path $home_ ".config/opencode/skills"),
                        (Join-Path $home_ ".claude/skills"),
                        (Join-Path $home_ ".agents/skills"))) {
        if (-not (Test-Path $root)) { continue }
        $dirs = @(Get-ChildItem $root -Directory -ErrorAction SilentlyContinue)
        foreach ($d in $dirs) { $dirs += @(Get-ChildItem $d.FullName -Directory -ErrorAction SilentlyContinue) }
        foreach ($d in $dirs) {
            $p = $d.FullName
            # skip this repo itself (it is reported by check 1)
            if ($p -eq $source -or $p.StartsWith($source + [IO.Path]::DirectorySeparatorChar)) { continue }
            if ($skillIds -contains $d.Name) {
                $loaded += [pscustomobject]@{ Kind = "copy"; Path = $p }
            }
        }
    }

    # 3) Registered paths: "skills" arrays in opencode.json / opencode.jsonc
    foreach ($cfg in @((Join-Path $home_ ".config/opencode/opencode.json"),
                       (Join-Path $home_ ".config/opencode/opencode.jsonc"))) {
        if (-not (Test-Path $cfg)) { continue }
        $raw = Get-Content $cfg -Raw
        foreach ($m in [regex]::Matches($raw, '"skills"\s*:\s*\[([^\]]*)\]')) {
            foreach ($q in [regex]::Matches($m.Groups[1].Value, '"([^"]+)"')) {
                $p = $q.Groups[1].Value -replace '\\\\', '\'
                if ($p.StartsWith('~')) { $p = Join-Path $home_ ($p.Substring(1) -replace '^[\\/]', '') }
                $has = $false
                foreach ($id in $skillIds) { if (Test-Path (Join-Path $p $id)) { $has = $true; break } }
                if ($has -and ($p -ne $source)) {
                    $leaf = Split-Path $cfg -Leaf
                    $loaded += [pscustomobject]@{ Kind = "config entry ($leaf)"; Path = $p }
                }
            }
        }
    }

    # De-duplicate identical paths
    $seen = @{}
    $loaded = @($loaded | Where-Object {
        $k = $_.Path.ToLowerInvariant()
        if ($seen[$k]) { $false } else { $seen[$k] = $true; $true }
    })

    foreach ($l in $loaded) { Write-Host ("found   [{0}] {1}" -f $l.Kind, $l.Path) -ForegroundColor Yellow }

    if ($loaded.Count -eq 0) {
        Write-Host ""
        Write-Host "NOT INSTALLED: no agent will load these skills from here." -ForegroundColor Red
        Write-Host "Fix: run  .\install.ps1 -Target opencode   (or clone this repo into"
        Write-Host "the opencode skills folder - see README Option 1. Pick ONE method.)"
        exit 2
    }
    if ($loaded.Count -eq 1) {
        Write-Host ""
        Write-Host "OK: exactly one install - no conflict." -ForegroundColor Green
        Write-Host "Update with: git pull   (clone)   or   .\install.ps1 -Target <t> -Force   (copy)"
        exit 0
    }

    Write-Host ""
    Write-Host ("DUPLICATE: {0} copies found - OpenCode loads only ONE of them; edits to the losing copy look ignored." -f $loaded.Count) -ForegroundColor Red

    # Which copy actually loads? Verified OpenCode precedence (high to low):
    # explicit config entries > project .opencode/skills > ~/.config/opencode/skills > .agents/skills > .claude/skills
    $best = $null; $bestRank = -1; $ties = 0
    foreach ($l in $loaded) {
        $r = 1
        if ($l.Kind -like "config*") { $r = 6 }
        elseif ($l.Path -like "*\.config\opencode\skills*") { $r = 4 }
        elseif ($l.Path -like "*\.agents\skills*") { $r = 3 }
        elseif ($l.Path -like "*\.claude\skills*") { $r = 2 }
        if ($r -gt $bestRank) { $bestRank = $r; $best = $l; $ties = 1 }
        elseif ($r -eq $bestRank) { $ties++ }
    }
    if ($ties -gt 1) {
        Write-Host ("Loads:    one of {0} copies at the same precedence level (search order decides)" -f $ties) -ForegroundColor Magenta
    } else {
        Write-Host ("Loads:    [{0}] {1}" -f $best.Kind, $best.Path) -ForegroundColor Magenta
    }
    Write-Host "Precedence (high to low): config entries > project .opencode/skills >"
    Write-Host "  ~/.config/opencode/skills > .agents/skills > .claude/skills"
    Write-Host "Note: OpenCode also discovers ~/.claude/skills and ~/.agents/skills, so"
    Write-Host "  -Target claude/agents installs feed OpenCode's search path too."
    Write-Host "Fix - keep EXACTLY ONE:"
    Write-Host "  * Keep an auto-discovery/copy: delete the other folder(s) listed above, AND"
    Write-Host "    remove the skills array entry from opencode.json / opencode.jsonc if present."
    Write-Host "  * Keep a config entry: delete the other folder(s); keep the entry."
    Write-Host "  * Clean slate: delete all folders listed above, then run  .\install.ps1 -Target opencode"
    Write-Host "After fixing, restart your agent session."
    exit 1
}

New-Item -ItemType Directory -Force -Path $dest | Out-Null

$installed = 0
$skipped = 0
foreach ($skill in $skills) {
    $targetPath = Join-Path $dest $skill.Name
    if ((Test-Path $targetPath) -and -not $Force) {
        Write-Host ("skip    {0} (exists - use -Force to overwrite)" -f $skill.Name) -ForegroundColor Yellow
        $skipped++
        continue
    }
    if (Test-Path $targetPath) {
        Remove-Item -Recurse -Force $targetPath
    }
    Copy-Item -Recurse $skill.FullName $targetPath
    Write-Host ("install {0}" -f $skill.Name) -ForegroundColor Green
    $installed++
}

Write-Host ""
Write-Host ("Done: {0} installed, {1} skipped -> {2}" -f $installed, $skipped, $dest) -ForegroundColor Cyan
Write-Host "Restart your agent session to pick up the changes."
