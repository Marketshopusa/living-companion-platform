# Gate 1 identity contract check (Windows)
$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
if (-not $Root) { $Root = Resolve-Path (Join-Path $PSScriptRoot "..") }
Set-Location $Root

Write-Output "== Gate 1 identity contracts =="

$schemas = @(
  "core/contracts/identity/v1/companion-identity.schema.json",
  "core/contracts/identity/v1/personality-configuration.schema.json",
  "core/contracts/identity/v1/companion-configuration.schema.json",
  "core/contracts/identity/v1/commands.schema.json",
  "core/contracts/identity/v1/errors.schema.json"
)
foreach ($s in $schemas) {
  if (-not (Test-Path -LiteralPath $s -PathType Leaf)) {
    Write-Output "MISSING SCHEMA: $s"
    exit 1
  }
  Write-Output "OK schema: $s"
}

$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) { $python = Get-Command python3 -ErrorAction SilentlyContinue }
if (-not $python) {
  Write-Output "FAIL: Python 3.x is required (ADR-001)"
  exit 1
}

& $python.Source -m pip install -q -r requirements-dev.txt
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& $python.Source -m pytest tests/identity
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Output "RESULT: PASS"
exit 0
