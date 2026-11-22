# GameClips AI - Real-time Git Auto-Watcher
# Watches for file changes in the workspace and automatically commits & pushes to GitHub

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "  GameClips AI - Real-Time Git Watcher    " -ForegroundColor Cyan
Write-Host "  Watching for code changes to auto-push  " -ForegroundColor Cyan
Write-Host "  Press Ctrl+C to stop watching           " -ForegroundColor Yellow
Write-Host "==========================================" -ForegroundColor Cyan

$watcher = New-Object System.IO.FileSystemWatcher
$watcher.Path = $scriptDir
$watcher.IncludeSubdirectories = $true
$watcher.EnableRaisingEvents = $true

# Filter out ignored folders
$ignoredPatterns = @("\.git", "\.venv", "temp_render", "__pycache__", "\.db-")

$lastSync = [datetime]::MinValue
$syncLock = $false

$action = {
    $path = $Event.SourceEventArgs.FullPath
    $changeType = $Event.SourceEventArgs.ChangeType
    
    # Check if path contains ignored folder
    foreach ($pattern in $ignoredPatterns) {
        if ($path -match $pattern) { return }
    }

    # Only sync for source extensions
    if ($path -notmatch "\.(py|js|html|css|ps1|txt|md|sql)$") { return }

    $now = Get-Date
    if (($now - $lastSync).TotalSeconds -lt 5) { return } # 5s debounce

    $global:lastSync = $now
    Write-Host "`n[CHANGE DETECTED] $changeType on $(Split-Path $path -Leaf)" -ForegroundColor Cyan
    Write-Host "[AUTO-SYNC] Running Git sync..." -ForegroundColor Yellow
    & "$scriptDir\git_sync.ps1" "Auto-sync update: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
}

Register-ObjectEvent $watcher 'Changed' -Action $action | Out-Null
Register-ObjectEvent $watcher 'Created' -Action $action | Out-Null
Register-ObjectEvent $watcher 'Deleted' -Action $action | Out-Null

try {
    while ($true) {
        Start-Sleep -Seconds 1
    }
} finally {
    $watcher.Dispose()
    Get-EventSubscriber | Unregister-Event
    Write-Host "[INFO] Git Watcher stopped." -ForegroundColor Yellow
}
