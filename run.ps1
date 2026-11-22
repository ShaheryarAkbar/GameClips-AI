# GameClips AI - Launch Script
# Launches the local dashboard and opens the default browser

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

$venvPython = "$scriptDir\.venv\Scripts\python.exe"

if (-not (Test-Path $venvPython)) {
    Write-Host "[INFO] Virtual environment not found. Running setup first..." -ForegroundColor Yellow
    & "$scriptDir\setup.ps1"
}

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "  Starting GameClips AI Command Center    " -ForegroundColor Cyan
Write-Host "  URL: http://127.0.0.1:5000              " -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan

# Open default browser after 1 second
Start-Job -ScriptBlock {
    Start-Sleep -Seconds 2
    Start-Process "http://127.0.0.1:5000"
} | Out-Null

& $venvPython app.py
