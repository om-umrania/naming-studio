# Project instructions

Naming Studio is a portable three-skill naming plugin. Canonical instructions live in skills/; portable, Codex, and Claude manifests describe the same package.

- Preserve exactly three task boundaries unless a deliberate scope change is agreed: coordinator/brief, creative name lab, domain discovery/checks.
- Keep skills directly callable, sibling links portable, and naming-project files outside the installed plugin.
- Preserve evidence statuses, source attribution, and read-only domain behavior. Do not invent availability, customer feedback, linguistic validation, or legal clearance.
- Do not commit client naming data, credentials, or machine-specific paths.
- Validate with ./scripts/check.sh. Update docs and version metadata together when packaging changes.
- No deployment service is needed. Publication means pushing the plugin source to GitHub; app-directory submission is a separate action.
