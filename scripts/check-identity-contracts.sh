#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

echo "== Gate 1 identity contracts =="

schemas=(
  core/contracts/identity/v1/companion-identity.schema.json
  core/contracts/identity/v1/personality-configuration.schema.json
  core/contracts/identity/v1/companion-configuration.schema.json
  core/contracts/identity/v1/commands.schema.json
  core/contracts/identity/v1/errors.schema.json
)
for s in "${schemas[@]}"; do
  if [[ ! -f "$s" ]]; then
    echo "MISSING SCHEMA: $s"
    exit 1
  fi
  echo "OK schema: $s"
done

if command -v python3 >/dev/null 2>&1; then
  PY=python3
elif command -v python >/dev/null 2>&1; then
  PY=python
else
  echo "FAIL: Python 3.x is required (ADR-001)"
  exit 1
fi

"$PY" -m pip install -q -r requirements-dev.txt
"$PY" -m pytest tests/identity
echo "RESULT: PASS"
