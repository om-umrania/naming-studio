# Installed-plugin runtime tests

Date: 2026-10-29. Hosts: Codex CLI 0.160.0 and Claude Code 2.1.290 on macOS. Both plugins were installed through their GitHub-backed marketplaces, not loaded from a development directory. Initial workflow tests used v0.1.0; the targeted consistency regression uses installed v0.1.1.

## Test setup

Used separate synthetic workspaces outside plugin source. Product: a simple offline desktop timer for English-speaking freelance designers in India; one-click focus, calm rhythm, easy return after a break, possible future planner. Requested exactly nine generated candidates across three directions, three shortlisted names, comparable applications for the best two, a domain follow-up, and a recommendation.

Each follow-up ran in a fresh CLI session. No model override, subagent, domain purchase, registration, publication of a customer project, or contact with people was requested. Model transcripts stayed local because they can contain unrelated host configuration; this is a sanitized results record.

Codex used its existing configured tool connections with workspace-write restrictions. Claude used its installed skills, file tools, and (for the full workflow) web tools, with acceptEdits and unanswered permission prompts denied. External MCP connections were disabled for Claude's bounded test; this intentionally exercises missing-registrar behavior and does not test a connected Namecheap integration in Claude.

## Results

| Scenario | Codex | Claude Code |
| --- | --- | --- |
| GitHub marketplace install | v0.1.0 installed, later updated to v0.1.1 | v0.1.0 installed, later updated to v0.1.1 |
| Full workflow through coordinator | Passed: brief, 9 candidates, 3 shortlisted, applications, recommendation, and domain evidence saved | Passed: same requested stages and project files saved |
| Live registrar access | Namecheap bulk checks returned unavailable exact .com names, a mix of .app results, and available alternative .com quotes; unknown term/renewal/fees stayed unknown | No registrar integration exposed; public search fetch was denied by test permissions; all domains explicitly not checked |
| Direct naming-lab call | Passed: exactly the existing shortlist reevaluated; feedback saved; planner removed from current scope; no new candidate IDs | Passed: same invariants, with original domain rows preserved and changed domain rationale marked |
| Direct naming-domains call | Passed: two offline .app alternatives; unchecked status and unknown quote details explicit | Suggestions/status passed, but the current recommendation retained a contradictory no-fallback sentence; see correction below |
| Claude resumes Codex files | Claude recovered Returnwell/N004, revision 2, shortlist IDs, feedback, and live-vs-offline domain distinctions; appended checkpoint only | Passed in a fresh Claude session |
| Codex resumes Claude files | Recovered Refrain/N009, R2, shortlist IDs, feedback, unchecked domain results, and flagged stale recommendation; appended checkpoint only | Project successfully consumed by Codex |

Artifact comparisons confirmed that both original projects retained all nine candidate IDs and every original domain-evidence row after direct calls. Both saved FEEDBACK.md and cross-host checkpoints. The creative ranking was allowed to change; the shortlist identities were not.

## Observed issue and v0.1.1 correction

Claude's domain-only pass added two fallback suggestions to DOMAINS.md but left RECOMMENDATION.md saying that no fallback wording existed. It correctly flagged the conflict in STATUS.md, and Codex detected it on resume, but a reader of the recommendation alone could reuse stale information.

The domain skill now reads the current recommendation and reconciles directly affected domain statements, or marks older contradictory conclusions superseded in their own file. It preserves the naming lead, IDs, prior evidence, and unrelated creative judgments; a focused follow-up does not trigger a full naming rerun. The shared state contract now makes this responsibility explicit.

## v0.1.1 regression results

Re-ran the same domain-only prompt in fresh sessions on separate copies of the affected Claude project, using the installed v0.1.1 skills in both hosts. Both passed:

- Read the current recommendation and saved project context.
- Retained Refrain/N009 as the lead and the original candidate IDs.
- Preserved earlier dated domain observations and the exactly two proposed .app alternatives.
- Kept availability not checked and quote details not provided without network requests.
- Reconciled the no-fallback statement inside RECOMMENDATION.md itself. Claude marked the old statement superseded; Codex replaced it with the current two-fallback state.
- Updated STATUS.md, with Claude explicitly resolving its previously flagged contradiction.

The correction was verified behaviorally in both hosts, not only by checking instruction text.

## Limits

These are observed workflow tests, not a guarantee of deterministic model behavior. Domain results are dated snapshots and not reservations or naming clearance. This run did not test every provider error/status combination, live customer feedback, Cowork UI installation, every other Agent Skills host, or public-directory submission. Codex startup also reported unrelated existing configuration warnings and a crowded skill list; explicit Naming Studio calls still found the installed skill paths. Those global configurations were not changed.

Existing interactive sessions need reload/restart to pick up an updated plugin; the tests above used fresh processes.
