#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
FAIL=0

required_files=(
  MASTER_BUILD_SPECIFICATION.md
  BUILD_PLAN.md
  ACCEPTANCE_TESTS.md
  ARCHITECTURE.md
  PRODUCT_SPEC.md
  DECISIONS.md
  SECURITY.md
  PRIVACY.md
  CONTRIBUTING.md
  AGENTS.md
  README.md
  .gitignore
  .env.example
  docs/adr/README.md
  docs/adr/000-no-stack-lock.md
  docs/runbooks/environments.md
  docs/evidence/gate-0/.gitkeep
)

required_dirs=(
  apps core backend ai integrations cms assets infrastructure scripts tests
  docs/adr docs/evidence docs/evaluations docs/runbooks
  apps/ios apps/android apps/windows apps/macos apps/web apps/telegram
)

echo "== Gate 0 baseline check =="

for f in "${required_files[@]}"; do
  if [[ ! -f "$f" ]]; then
    echo "MISSING FILE: $f"
    FAIL=1
  else
    echo "OK file: $f"
  fi
done

for d in "${required_dirs[@]}"; do
  if [[ ! -d "$d" ]]; then
    echo "MISSING DIR: $d"
    FAIL=1
  else
    echo "OK dir: $d"
  fi
done

if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  while IFS= read -r p; do
    base="$(basename "$p")"
    case "$base" in
      .env|credentials.json) echo "FORBIDDEN TRACKED: $p"; FAIL=1 ;;
    esac
    case "$p" in
      *.pem) echo "FORBIDDEN TRACKED: $p"; FAIL=1 ;;
    esac
  done < <(git ls-files)
else
  echo "WARN: not a git repo; skipped tracked-secret scan"
fi

if [[ -f .env ]]; then
  echo "FAIL: .env present in workspace (must stay gitignored and uncommitted)"
  FAIL=1
fi

product_hits="$(find core backend ai apps -type f \( -name '*.ts' -o -name '*.tsx' -o -name '*.py' -o -name '*.go' -o -name '*.rs' -o -name '*.cs' -o -name '*.java' -o -name '*.kt' -o -name '*.swift' \) 2>/dev/null || true)"
if [[ -n "$product_hits" ]]; then
  echo "FAIL: product source found during Gate 0:"
  echo "$product_hits"
  FAIL=1
else
  echo "OK: no product source under core/backend/ai/apps"
fi

if [[ "$FAIL" -ne 0 ]]; then
  echo "RESULT: FAIL"
  exit 1
fi
echo "RESULT: PASS"
