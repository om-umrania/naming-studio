# Architecture

One skills/ tree is canonical across hosts. Root plugin.json follows the Agent Plugins portable format. .codex-plugin/plugin.json supports Codex compatibility packaging; .claude-plugin/plugin.json and marketplace.json support Claude plugin discovery. .agents/plugins/marketplace.json supplies a repository-local Codex marketplace.

naming-studio owns the brief and routing. naming-lab owns ideation, evaluation, preliminary non-domain screening, applications, and feedback. naming-domains owns domain suggestions and registrar checks. Skill links work without a nested-invocation API: read and follow the linked instructions in the same session.

The shared project-file contract lives under the coordinator's references/. All three folders must travel together. Markdown files in a separate user project persist state across sessions and platforms. No runtime server, hooks, database, or credentials are bundled. Namecheap is an optional connected capability; missing access produces explicit unchecked results.
