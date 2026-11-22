# GameClips AI - Setup Script
# Target: Windows 10 Pro / HP EliteBook Folio 9470m (Lightweight, CPU-only)

$ErrorActionPreference = "Stop"
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "  GameClips AI - Environment Setup        " -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan

# 1. Storage Check
$driveE = Get-PSDrive E -ErrorAction SilentlyContinue
if ($driveE) {
    $freeGB = [math]::Round($driveE.Free / 1GB, 2)
    Write-Host "[OK] Drive E: Free Space: $freeGB GB" -ForegroundColor Green
    if ($freeGB -lt 2.0) {
        Write-Error "Insufficient disk space on Drive E! At least 2.0 GB required."
        exit 1
    }
}

# 2. FFmpeg Check
$ffmpegCmd = Get-Command ffmpeg -ErrorAction SilentlyContinue
if ($ffmpegCmd) {
    Write-Host "[OK] FFmpeg detected at: $($ffmpegCmd.Source)" -ForegroundColor Green
} else {
    Write-Warning "FFmpeg not found in PATH. Please ensure FFmpeg is installed."
}

# 3. Python Check & Installation
$localPyPath = "$env:LOCALAPPDATA\Programs\Python\Python311\python.exe"
if (Test-Path $localPyPath) {
    $pyExe = $localPyPath
    Write-Host "[OK] Detected Python at: $pyExe" -ForegroundColor Green
} else {
    $pythonCmd = Get-Command python -ErrorAction SilentlyContinue
    if ($pythonCmd -and $pythonCmd.Source -notlike "*WindowsApps*") {
        $pyExe = "python"
        Write-Host "[OK] Python detected in PATH: $($pythonCmd.Source)" -ForegroundColor Green
    } else {
        Write-Host "[INFO] Installing Python 3.11 for current user..." -ForegroundColor Yellow
        $installer = "$env:TEMP\python-3.11.9-amd64.exe"
        Invoke-WebRequest -Uri "https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe" -OutFile $installer
        Start-Process -FilePath $installer -ArgumentList "/quiet InstallAllUsers=0 Include_launcher=0 InstallLauncherAllUsers=0 PrependPath=1 TargetDir=`"$env:LOCALAPPDATA\Programs\Python\Python311`"" -Wait
        $pyExe = $localPyPath
    }
}

# 4. Virtual Environment (.venv)
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

if (-not (Test-Path "$scriptDir\.venv")) {
    Write-Host "[INFO] Creating virtual environment (.venv)..." -ForegroundColor Yellow
    & $pyExe -m venv .venv
}
Write-Host "[OK] Virtual environment ready." -ForegroundColor Green

# 5. Install Dependencies
$venvPython = "$scriptDir\.venv\Scripts\python.exe"
$venvPip = "$scriptDir\.venv\Scripts\pip.exe"

Write-Host "[INFO] Installing minimal dependencies from requirements.txt..." -ForegroundColor Yellow
& $venvPip install --quiet --upgrade pip
& $venvPip install --quiet -r requirements.txt
Write-Host "[OK] Dependencies installed successfully." -ForegroundColor Green

# 6. Database Initialization
if (Test-Path "$scriptDir\init_db.py") {
    Write-Host "[INFO] Initializing SQLite database..." -ForegroundColor Yellow
    & $venvPython init_db.py
    Write-Host "[OK] Database initialized." -ForegroundColor Green
}

Write-Host "`nSetup completed successfully! Run './run.ps1' to launch GameClips AI." -ForegroundColor Green
