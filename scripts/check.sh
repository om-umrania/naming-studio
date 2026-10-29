#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python3 scripts/validate.py
if command -v claude >/dev/null 2>&1; then
  claude plugin validate .claude-plugin/plugin.json
  claude plugin validate .claude-plugin/marketplace.json
fi
