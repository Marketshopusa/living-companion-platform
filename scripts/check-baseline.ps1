# Gate 0 repository baseline check (Windows)
$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
if (-not $Root) { $Root = Resolve-Path (Join-Path $PSScriptRoot "..") }
Set-Location $Root
$Fail = 0

function Fail-Msg([string]$m) {
  Write-Output $m
  $script:Fail = 1
}

$requiredFiles = @(
  "MASTER_BUILD_SPECIFICATION.md",
  "BUILD_PLAN.md",
  "ACCEPTANCE_TESTS.md",
  "ARCHITECTURE.md",
  "PRODUCT_SPEC.md",
  "DECISIONS.md",
  "SECURITY.md",
  "PRIVACY.md",
  "CONTRIBUTING.md",
  "AGENTS.md",
  "README.md",
  ".gitignore",
  ".env.example",
  "docs/adr/README.md",
  "docs/adr/000-no-stack-lock.md",
  "docs/adr/002-legal-policy-pack-draft.md",
  "docs/legal/README.md",
  "docs/legal/ai-disclosure.md",
  "docs/legal/privacy-policy.md",
  "docs/legal/terms-of-service.md",
  "docs/legal/acceptable-use-policy.md",
  "docs/runbooks/environments.md",
  "docs/evidence/gate-0/.gitkeep"
)

$requiredDirs = @(
  "apps", "core", "backend", "ai", "integrations", "cms", "assets", "infrastructure", "scripts", "tests",
  "docs/adr", "docs/evidence", "docs/evaluations", "docs/runbooks", "docs/legal",
  "apps/ios", "apps/android", "apps/windows", "apps/macos", "apps/web", "apps/telegram"
)

Write-Output "== Gate 0 baseline check =="

foreach ($f in $requiredFiles) {
  if (-not (Test-Path -LiteralPath $f -PathType Leaf)) { Fail-Msg "MISSING FILE: $f" }
  else { Write-Output "OK file: $f" }
}

foreach ($d in $requiredDirs) {
  if (-not (Test-Path -LiteralPath $d -PathType Container)) { Fail-Msg "MISSING DIR: $d" }
  else { Write-Output "OK dir: $d" }
}

try {
  $tracked = git ls-files
  foreach ($p in $tracked) {
    $base = Split-Path $p -Leaf
    if ($base -eq ".env" -or $base -eq "credentials.json" -or $p -like "*.pem") {
      Fail-Msg "FORBIDDEN TRACKED: $p"
    }
  }
} catch {
  Write-Output "WARN: git ls-files failed; skipped tracked-secret scan"
}

if (Test-Path -LiteralPath ".env" -PathType Leaf) {
  Fail-Msg "FAIL: .env present in workspace (must stay gitignored and uncommitted)"
}

# Gate 0 forbade all product source. After Gate 1, core/backend identity code is allowed.
# Client and AI trees must still not grow identity/product implementations.
$exts = "*.ts","*.tsx","*.py","*.go","*.rs","*.cs","*.java","*.kt","*.swift"
$hits = @()
foreach ($dir in @("ai","apps")) {
  if (Test-Path $dir) {
    $hits += Get-ChildItem -Path $dir -Recurse -File -Include $exts -ErrorAction SilentlyContinue
  }
}
if ($hits.Count -gt 0) {
  Fail-Msg "FAIL: product source found under ai/ or apps/ (clients must not fork identity):"
  $hits | ForEach-Object { Write-Output $_.FullName }
} else {
  Write-Output "OK: no product source under ai/apps (core/backend identity code is allowed)"
}

if ($Fail -ne 0) {
  Write-Output "RESULT: FAIL"
  exit 1
}
Write-Output "RESULT: PASS"
exit 0
