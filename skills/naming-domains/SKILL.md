---
name: naming-domains
description: Suggest practical domain names for a brand or shortlist, check registration availability and quoted prices, and compare options. Use for domain discovery or a naming follow-up; excludes purchasing and registration.
---

# Naming Domains

Suggest useful domain options and distinguish creative proposals from verified registration results. Work independently with an existing brand or continue a naming project. Read [the project-file contract](../naming-studio/references/project-files.md), STATUS.md and the relevant brief/shortlist when present. A domain-only request does not need a full naming brief.

## Select useful options

Use required extensions, exact-match rules, target markets, and budget when supplied. Ask if an unresolved constraint would materially change the work. Otherwise begin with each shortlisted name's exact `.com`, explicitly stating that starting choice. Check the shortlist, not the entire brainstorm ledger. If the user provides exact domains, check those first.

When exact options are unavailable or alternatives are requested, propose a compact second batch: an appropriate extension, a natural brand-plus-descriptor, or a short action phrase when it fits how customers use the product. Explain memorability, spoken spelling, category credibility, length, and future-range tradeoffs. Avoid awkward forced spellings, gratuitous hyphens/numbers, or implying a local presence or affiliation that is unsupported. Do not silently replace a strong brand just to obtain an exact .com. If new brand ideation is needed, offer [naming-lab](../naming-lab/SKILL.md).

Label unqueried suggestions `not checked`. Domain alternatives are domain wording, not automatically new approved brand candidates. Preserve the connection to the candidate ID and the exact brand spelling.

## Check availability read-only

Discover available domain-registration tools. Prefer an already connected Namecheap integration; discover its current bulk-domain-check operation and follow its actual schema instead of hardcoding a tool name. Batch shortlisted exact domains, then query only a useful set of alternatives. Do not purchase, reserve, register, or add to a paid cart.

If Namecheap tools are unavailable, use its public domain search when accessible. If neither is available, keep the suggestions and report `not checked`, describing the missing access. Do not scrape inaccessible pages or fabricate a registrar response. A search-engine result, absent website, or DNS/RDAP observation alone does not establish purchase availability or price.

For every result, record:

- Exact domain, source, and check date/time.
- Availability as returned: available, unavailable, not checked, invalid input, or check error; preserve any relevant provider qualification.
- Quoted purchase amount and currency.
- Registration term, renewal price, and fees only if supplied; otherwise `not provided`.

Never infer annual cost or renewal from a purchase quote. Treat `tldNotSupportedDomains` (or equivalent) as `not checked: extension unsupported or temporarily paused`, not unavailable. Treat `invalidNameDomains` as invalid inputs; correct obvious formatting errors before retrying. Keep errors, missing entries, unsupported extensions, and unavailable domains distinct. Retry transient failures once when useful; if access stays unavailable, report the limitation and continue with the evidence obtained.

## Recommend and save

Compare a manageable set of exact and alternative options. Recommend a domain with its brand fit and meaningful tradeoff, and explain whether the findings change the naming recommendation. If a mandatory domain constraint fails, return that specific constraint to the coordinator/name lab rather than claiming the naming task is resolved.

Write DOMAINS.md with candidate links, suggestions, result statuses, dated evidence, quote details, and recommendation impact; update STATUS.md. On a refresh retain prior observations as dated history and mark the latest one. Availability and prices are snapshots, not reservations, trademark clearance, handle checks, or linguistic validation. Return to [naming-studio](../naming-studio/SKILL.md) when continuing a full naming project; stop after the domain result when called directly.
