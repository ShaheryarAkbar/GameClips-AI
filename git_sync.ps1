# GameClips AI - Automatic Git Sync & Push Script
# Commits all new or modified code and pushes to GitHub

param (
    [string]$CommitMessage = "Auto-update: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
)

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "  GameClips AI - Git Auto-Sync Engine     " -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan

# 1. Check if git repository exists
if (-not (Test-Path "$scriptDir\.git")) {
    Write-Error "Git repository not initialized in $scriptDir"
    exit 1
}

# 2. Check for changes
$changes = git status --porcelain
if (-not $changes) {
    Write-Host "[OK] Working tree clean. No new code changes to push." -ForegroundColor Green
    exit 0
}

Write-Host "[INFO] Detected new code changes:" -ForegroundColor Yellow
git status -s

# 3. Stage and Commit
Write-Host "`n[INFO] Staging all files..." -ForegroundColor Yellow
git add .

Write-Host "[INFO] Committing changes with message: '$CommitMessage'..." -ForegroundColor Yellow
git commit -m "$CommitMessage"

# 4. Check if remote origin is set
$remoteUrl = git remote get-url origin 2>$null
if (-not $remoteUrl) {
    Write-Warning "`n[ACTION REQUIRED] Remote origin is not set yet!"
    Write-Host "Please link your GitHub repository by running:" -ForegroundColor Cyan
    Write-Host "  git remote add origin https://github.com/<YOUR-USERNAME>/GameClips-AI.git" -ForegroundColor White
    Write-Host "  git push -u origin main" -ForegroundColor White
    exit 0
}

# 5. Push to GitHub (main and gh-pages)
Write-Host "`n[INFO] Pushing latest changes to GitHub main branch ($remoteUrl)..." -ForegroundColor Yellow
git push origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host "`n[INFO] Updating gh-pages branch..." -ForegroundColor Yellow
    git checkout gh-pages
    git merge main -m "Sync main to gh-pages: $CommitMessage"
    git push origin gh-pages
    git checkout main
    Write-Host "`n[SUCCESS] All code and live site successfully synced and updated on GitHub!" -ForegroundColor Green
} else {
    Write-Warning "`n[NOTICE] Push failed or requires authentication. If this is your first push, please verify credentials."
}
