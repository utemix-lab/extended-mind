param(
  [string]$Source,
  [string]$Destination = "R:\temp-hf-space"
)

$repoRoot = Split-Path -Parent $PSScriptRoot
if (-not $Source) {
  $Source = Join-Path $repoRoot "spaces\telegram-content"
}

Write-Host "Sync HF Space files:" -ForegroundColor Cyan
Write-Host "  Source:      $Source"
Write-Host "  Destination: $Destination"

if (-not (Test-Path $Source)) {
  Write-Error "Source path not found: $Source"
  exit 1
}

if (-not (Test-Path $Destination)) {
  Write-Error "Destination path not found: $Destination"
  exit 1
}

$files = @("app.py", "requirements.txt", "README.md")
foreach ($file in $files) {
  $srcFile = Join-Path $Source $file
  if (Test-Path $srcFile) {
    Copy-Item -Path $srcFile -Destination $Destination -Force
  } else {
    Write-Warning "Missing file in source: $file"
  }
}

Write-Host "Sync complete. Commit/push in temp-hf-space to deploy." -ForegroundColor Green
exit 0
