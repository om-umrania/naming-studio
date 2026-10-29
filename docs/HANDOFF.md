# Handoff

V1 source is ready: three skills, shared Markdown progress contract, portable/Codex/Claude manifests, installation documentation, checks, and archive builder. The original globally installed param-brand-name skill has not been modified.

Run ./scripts/check.sh and python3 scripts/package.py after edits. Keep manifest versions aligned. See docs/VALIDATION.md for actual validation limits and docs/EVALUATION.md for behavioral acceptance cases.

Installed-plugin tests now cover full workflow, direct skill calls, saved-state refinement, and cross-tool resume. The v0.1.1 fix reconciles domain follow-ups with affected recommendation statements. See docs/RUNTIME-TESTS.md. Next product work should follow real naming-project feedback. Directory/store submission and runtime evaluation on each host remain separate from publishing the source repository.
