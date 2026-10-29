# Naming Studio

Three connected skills that turn a commercial naming problem into a reasoned shortlist and practical domain options. Start with one coordinator, or call the focused skill you need. Progress lives in your project files so you can resume across sessions and compatible tools.

| Skill | Use it for |
| --- | --- |
| **naming-studio** | Build the brief, coordinate the process, resume work, and make the final recommendation |
| **naming-lab** | Generate, evaluate, shortlist, or refine names; research category patterns and preliminary conflicts |
| **naming-domains** | Suggest domain wording, check shortlisted domains, compare quotes, and recommend options |

The workflow adapts the identify–invent–implement process and diamond exercise from David Placek's interview on Lenny's Podcast, June 29, 2025. This is an independent adaptation; no affiliation or endorsement is claimed. See [attribution and limits](skills/naming-studio/references/attribution.md).

## What it does

- Starts with the business, audience, desired experience, and constraints.
- Separates creative generation from evaluation; evaluates an existing shortlist before restarting ideation.
- Recommends names with specific fit, weaknesses, and comparable applications.
- Suggests domains beyond an exact match and checks registration availability through an optional connected Namecheap integration or accessible public search.
- Distinguishes opinions, evidence, unchecked questions, errors, and dated availability quotes.
- Saves the brief, candidate history, research, domain findings, feedback, and next action in Markdown.

Domain suggestions remain useful without a registrar connection, but availability stays **not checked**. Naming research is preliminary; it does not establish trademark clearance. No purchase, registration, outreach, or customer-project publication is authorized by these skills.

## Install

### Codex

In a current Codex CLI with plugin commands:

```sh
codex plugin marketplace add om-umrania/naming-studio
codex plugin add naming-studio@naming-studio-marketplace
```

The repository also includes `.agents/plugins/marketplace.json` for local marketplace discovery. Desktop interfaces and plugin support vary by version; follow the client's marketplace controls if it does not expose these commands. Reload the client after installation if skills do not appear.

Invoke the coordinator:

```text
Use $naming-studio to help name my business. Ask for missing context and save progress in this project's workspace.
```

Or call `$naming-lab` / `$naming-domains` directly.

### Claude Code

```text
/plugin marketplace add om-umrania/naming-studio
/plugin install naming-studio@naming-studio-marketplace
```

Invoke `/naming-studio:naming-studio`, `/naming-studio:naming-lab`, or `/naming-studio:naming-domains` with your request. To try a checkout without installing a marketplace:

```sh
claude --plugin-dir /absolute/path/to/naming-studio
```

### Claude Cowork

Build the archive below and use the client's custom-plugin upload flow where available. The `.plugin` archive includes the Claude manifest and shared skills. Custom-plugin access depends on the client and workspace settings. This repository has not been submitted to a curated plugin directory.

### Other Agent Skills hosts

Copy **all three folders** from `skills/` into the host's supported skills directory, preserving folder names and relative references. Hosts supporting the portable Agent Plugins format can inspect root `plugin.json`. A plain chat interface without skill/file support needs the skill content supplied manually and cannot promise persistent project files.

Other platforms are a portability target, not a claim of verified runtime support. Host-specific browsing, registrar tools, and filesystem permissions determine which capabilities are available.

## Example requests

```text
Use naming-studio to name an Indian consumer footwear business. Begin by clarifying the audience and desired experience.
```

```text
Use naming-lab to evaluate these existing names against my saved brief. Do not generate new names yet.
```

```text
Use naming-domains to suggest and check domains for my shortlisted names. Compare exact matches with natural alternatives; do not purchase anything.
```

```text
Use naming-studio to resume naming-projects/my-business. Read the saved feedback before revising the shortlist.
```

## Saved progress

The default project location is `naming-projects/<project-slug>/` inside your working project, after identifying the project. An explicitly selected location takes precedence. Files are created as needed:

- `STATUS.md` — progress, open questions, and next action.
- `BRIEF.md` — business context, diamond, constraints, and confirmed vs open details.
- `CANDIDATES.md` — stable candidate IDs, directions, evaluation, and decisions.
- `RESEARCH.md` and `DOMAINS.md` — scoped, dated evidence with separate statuses.
- `RECOMMENDATION.md` and `FEEDBACK.md` — recommendations, reactions, and revisions.

See the [project-file contract](skills/naming-studio/references/project-files.md). Keep customer work outside this public plugin repository. Saving project files does not publish them.

## Development and packaging

Python 3.9+ is sufficient for the bundled validation and packaging scripts. Claude CLI is optional and adds native manifest validation when installed.

```sh
./scripts/check.sh
python3 scripts/package.py
```

The archive is written to `dist/naming-studio.plugin`. Packaging uses an explicit public-file allowlist and a temporary archive before copying the result; development files and customer projects are excluded.

Checks cover manifest consistency, skill entrypoints, relative links, and marketplace paths. Native Claude validation checks the Claude manifests when available. GitHub Actions runs structural validation and archive building. These structural checks do not establish model behavior. Installed-plugin workflow tests were also run in Codex CLI 0.160.0 and Claude Code 2.1.290; see [runtime test results](docs/RUNTIME-TESTS.md) for scenarios and limits. See [evaluation cases](docs/EVALUATION.md), [validation results](docs/VALIDATION.md), and [contributing](CONTRIBUTING.md).

## Package layout

```text
plugin.json                    Portable Agent Plugins manifest
.codex-plugin/plugin.json      Codex compatibility manifest
.claude-plugin/                Claude manifest and marketplace
.agents/plugins/marketplace.json
skills/
  naming-studio/               Coordinator, shared state contract, attribution
  naming-lab/                  Creative naming and evaluation
  naming-domains/              Domain suggestions and checks
scripts/                       Validation and archive creation
```

## Packaging references

- [OpenAI plugin packaging](https://developers.openai.com/plugins/build/plugins)
- [Claude plugin manifest reference](https://code.claude.com/docs/en/plugins-reference)
- [Agent Skills specification](https://agentskills.io/specification)

## License

MIT. See [LICENSE](LICENSE).
