param(
    [Parameter(Mandatory=$true)][string]$Text,
    [Parameter(Mandatory=$false)][string]$Voice = "Microsoft David Desktop",
    [Parameter(Mandatory=$true)][string]$OutputFile
)

$outDir = Split-Path -Parent $OutputFile
if ($outDir -and -not (Test-Path $outDir)) {
    New-Item -ItemType Directory -Force -Path $outDir | Out-Null
}

Add-Type -AssemblyName System.Speech
$synth = New-Object System.Speech.Synthesis.SpeechSynthesizer

try {
    $synth.SelectVoice($Voice)
} catch {
    # Fallback to default installed voice if named voice not found
}

$synth.SetOutputToWaveFile($OutputFile)
$synth.Speak($Text)
$synth.Dispose()
Write-Host "AUDIO_OK"
