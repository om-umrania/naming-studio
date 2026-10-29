# Validation

## 2026-10-29 — Initial v0.1.0

Completed locally:

- All three skill folders passed the Codex skill-creator quick validator.
- `./scripts/check.sh` passed: aligned manifest identity/version, three named skill entrypoints, contained relative reference links, and local marketplace sources.
- Claude CLI's native validator passed both `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` without warnings.
- `python3 scripts/package.py --output-dir ...` built the archive with 13 allowlisted files; archive integrity and inclusion of exactly three skill entrypoints passed.
- Reviewed routing for full naming, existing-shortlist evaluation, creative-only requests, domain-only calls, missing registrar access, unsupported/invalid/error statuses, and resuming revised project context. This was an instruction review, not a model execution test.

At the initial packaging checkpoint, live execution and project resumption were not yet verified. Subsequent installed-plugin testing on 2026-10-29 covers Codex CLI and Claude Code, including cross-tool resumption and live Namecheap calls in Codex; see docs/RUNTIME-TESTS.md. Cowork, other hosts, and curated-directory installation remain unverified. No customer research or naming availability claims were generated during package validation.

## 2026-10-29 — v0.1.1 installed workflow validation

Installed on Codex CLI and Claude Code from the public GitHub marketplaces. Full workflow, fresh direct calls to all three skills, preserved project files, feedback refinement, and cross-host resume passed within the scopes documented in [RUNTIME-TESTS.md](RUNTIME-TESTS.md). A stale domain conclusion found in Claude was corrected in v0.1.1 and the same regression passed in both hosts. Live Namecheap results were verified in Codex; Claude's missing-access path was verified, not a live registrar integration.
