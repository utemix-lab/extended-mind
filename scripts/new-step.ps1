Param(
  [string]$RepoRoot = (Resolve-Path ".").Path
)

$stepsDir = Join-Path $RepoRoot "docs\steps"
$templatePath = Join-Path $stepsDir "_template.step.md"

if (-not (Test-Path $stepsDir)) {
  New-Item -ItemType Directory -Path $stepsDir | Out-Null
}

if (-not (Test-Path $templatePath)) {
  Write-Error "Template not found: $templatePath"
  exit 1
}

$date = Get-Date -Format "yyyy-MM-dd"
$pattern = "S-$date-"
$existing = Get-ChildItem -Path $stepsDir -Filter "step-$date-*.step.md" -ErrorAction SilentlyContinue
$next = ($existing.Count + 1).ToString("00")

$stepId = "S-$date-$next"
$fileName = "step-$date-$next.step.md"
$targetPath = Join-Path $stepsDir $fileName

$content = Get-Content $templatePath -Raw
$content = $content -replace "S-YYYY-MM-DD-XX", $stepId

Set-Content -Path $targetPath -Value $content -Encoding UTF8
Write-Output $targetPath
