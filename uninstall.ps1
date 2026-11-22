# GameClips AI - Clean Uninstall Script

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "  GameClips AI - Cleanup & Uninstaller    " -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

# 1. Ask or remove .venv
if (Test-Path "$scriptDir\.venv") {
    Write-Host "[INFO] Removing virtual environment (.venv)..." -ForegroundColor Yellow
    Remove-Item -Recurse -Force "$scriptDir\.venv"
    Write-Host "[OK] .venv removed." -ForegroundColor Green
}

# 2. Clean temporary render cache
if (Test-Path "$scriptDir\temp_render") {
    Write-Host "[INFO] Cleaning temporary render cache..." -ForegroundColor Yellow
    Remove-Item -Recurse -Force "$scriptDir\temp_render"
    Write-Host "[OK] Temp cache cleaned." -ForegroundColor Green
}

# 3. Cache and pycache
Get-ChildItem -Path $scriptDir -Filter "__pycache__" -Recurse -Directory -ErrorAction SilentlyContinue | Remove-Item -Recurse -Force
Write-Host "[OK] Python cache cleaned." -ForegroundColor Green

Write-Host "`nNotice: Project database (data/) and exports (exports/) have been preserved for safety." -ForegroundColor Cyan
Write-Host "To remove everything completely, manually delete the folder '$scriptDir'." -ForegroundColor Gray
Write-Host "Uninstallation complete." -ForegroundColor Green
