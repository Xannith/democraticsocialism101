# democraticsocialism101.com - Site Specification

Single source of truth for site architecture, content standards, and build workflow.
All Claude Code sessions and content drafts must conform to this document.
If this spec and any page conflict, the spec wins. Update the spec first, then the page.

## 1. Mission and Positioning

An educational explainer on democratic socialism (DemSoc). Not advocacy, not
opposition. The site presents the strongest version of every argument, including
critiques, and lets readers reach their own conclusions.

Core promises to the reader:

1. Terms are defined precisely and used consistently.
2. Every real-world example is honestly classified (democratic socialism vs.
   social democracy vs. mixed economy).
3. Critiques get steelmanned, not strawmanned, and so do responses to them.
4. Established fact, inference, and opinion are visibly distinguished.

## 2. Terminology Rules

- Full term "democratic socialism" in all page titles, H1 headings, and meta
  descriptions (search alignment).
- "DemSoc" in body copy after first use per page.
- Never conflate: democratic socialism, social democracy, socialism,
  communism, and mixed economy each get precise, sourced definitions on the
  taxonomy page, and every other page links to that page rather than
  redefining terms. The single exception is the glossary page (section 3),
  which gives brief companion definitions and must stay consistent with the
  taxonomy page, which remains authoritative.

## 3. Site Architecture

### Tier structure (Crawl / Walk / Run)

The homepage presents three entry doors. These are depth tiers, not
education-level labels.

| Tier  | Public label  | Assumes                        | Content type                        |
|-------|---------------|--------------------------------|-------------------------------------|
| Crawl | Start Here    | Nothing                        | Definitions, taxonomy, common myths |
| Walk  | Go Deeper     | Curiosity, evidence tolerance  | Country case studies, policy areas  |
| Run   | Full Theory   | Comfort with abstraction       | Theory, debates, academic lineage   |

Fly-stage features (future, do not build in v1): interactive explainers,
reading-level variants, guided argument explorer.

### Page inventory (v1)

Crawl:
- index.html (three-door homepage)
- what-is-democratic-socialism.html
- taxonomy.html (DemSoc vs. social democracy vs. socialism vs. communism vs.
  mixed economy)
- common-misconceptions.html
- faq.html (with FAQ structured data markup)
- glossary.html (defines DemSoc and adjacent systems: social democracy,
  socialism, communism, corporate capitalism, crony capitalism, state
  capitalism, and mixed economy; one-paragraph definition plus a short
  exemplar-country list per entry; the informal term "corpo-capitalism" may
  appear only as a colloquial synonym under corporate capitalism, never as a
  primary term; taxonomy remains the authoritative treatment of the five core
  terms and the glossary must not diverge from it)

Walk:
- case-studies/index.html (comparison table across all countries)
- case-studies/nordic-model.html
- case-studies/germany.html
- case-studies/united-kingdom.html
- case-studies/mondragon.html (cooperative, not a country, template adapts)
- case-studies/united-states.html (what exists already, what is proposed)
- policy-areas.html (healthcare, labor, housing, banking, ownership models)
- figures.html ("Who Identifies as a Democratic Socialist"): includes only
  figures who publicly self-identify as democratic socialists, cited to their
  own statements or documented DSA membership; no one is included based on
  labels applied by others; the inclusion criterion is stated on the page
  itself; the page carries a visible "Last verified" date. Initial entries:
  Bernie Sanders (self-identified, not a DSA member), Alexandria Ocasio-Cortez
  (DSA member), Zohran Mamdani (DSA member, NYC mayor), and Rashida Tlaib
  (DSA-aligned).

Run:
- theory/index.html
- theory/historical-lineage.html
- theory/market-socialism.html
- theory/critiques-and-responses.html (calculation debate, incentives, tax
  capacity, historical failures and how DemSoc distinguishes itself)
- theory/coexistence-with-capitalism.html (mixed economy models, regulated
  markets, codetermination)

Support:
- about.html (methodology and editorial standards, not personal bio)
- sources.html (master bibliography)

## 4. Case Study Template (mandatory fields, fixed order)

Every case study page uses exactly this structure:

1. **Classification**: honest label (democratic socialist, social democratic,
   mixed economy, or hybrid) with one-sentence justification.
2. **What they had before**: prior system and conditions.
3. **How they chose it**: electoral path, crisis response, or gradual reform.
4. **What they gained**: outcomes with sources.
5. **What they lost or traded off**: costs with sources, same rigor as gains.
6. **Where they are now**: current status, recent reversals or expansions.
7. **Sources**: every factual claim cited.

## 5. Content Standards

- Distinguish established fact, inference, and contested claims in the prose.
- Steelman rule: before publishing any critique or defense, ask whether an
  informed proponent or opponent would accept it as their best argument.
- No loaded language. Terms like "obviously," "everyone knows," and "so-called"
  are banned.
- Oxford comma always.
- No en dashes or em dashes anywhere. ASCII hyphens only. Rewrite with commas,
  parentheses, or colons instead.
- Reading level target for Crawl tier: accessible to a general adult reader
  with no prior exposure. Walk and Run may increase density but never jargon
  without definition.

## 6. Technical Standards

- Static HTML, CSS, and vanilla JS. No frameworks, no build step in v1.
- One shared stylesheet: /css/site.css. No inline styles, no per-page CSS
  files.
- Consistent nav and footer across all pages. Any nav change is applied to
  every page in the same commit.
- Semantic HTML throughout. Accessibility: proper heading hierarchy, alt text,
  sufficient contrast, keyboard navigable.
- Mobile-first responsive layout.
- FAQ page includes FAQPage structured data (JSON-LD).
- Every page: unique title tag, unique meta description containing the full
  term "democratic socialism."

## 7. Repo and Deploy

- GitHub repo, deployed via Netlify.
- Domain democraticsocialism101.com, DNS pointed from registrar to Netlify.
- Branch: main. Commit locally. Do not push unless explicitly instructed.

## 8. Claude Code Session Rules

Every session working on this repo must:

1. Audit before patching. Read the current state of any file before editing it.
2. Treat this spec as the single source of truth. Flag conflicts rather than
   silently resolving them.
3. Make no unrequested design or content changes.
4. Commit locally with descriptive messages. Never push.
5. Follow all content standards in section 5, including the dash rule.

## 9. Build Phases (prompt sequence)

Phase 1 - Scaffold: repo structure, shared CSS, nav and footer pattern,
homepage with three doors, empty page shells with correct titles and metas.

Phase 2 - Crawl content: taxonomy page first (it is the keystone), then
what-is, misconceptions, and FAQ.

Phase 3 - Walk content: case study template implemented once, reviewed, then
replicated per country.

Phase 4 - Run content: theory pages, critiques-and-responses last (it depends
on everything else being stable).

Phase 5 - Polish: comparison table on case-studies index, sources page,
structured data, accessibility pass, Lighthouse audit.

Each phase gets its own Claude Code prompt. Do not combine phases in one
session.

## 10. Resolved Decisions

- Site byline: unattributed; editorial voice is the first person plural "we";
  no personal names appear anywhere on the site.
- Visual identity: defined in section 11.
- Glossary: approved; added to the Crawl inventory in section 3.
- Contact or comment mechanism: none; the site is informational only.

No open decisions remain at this time.

## 11. Visual Identity

- Palette: red, white, and blue. Blue-dominant, with red as the accent color.
  Whites and off-whites for surfaces. Exact hex values are defined as CSS
  custom properties in /css/site.css and nowhere else.
- Typography: professional and editorial. One serif for headings and one
  humanist sans-serif for body text, each with a system font stack fallback.
  No decorative fonts.
- Glass effects: glassmorphism (translucent surfaces with backdrop blur) is
  used on navigation, buttons, and card containers only. It is never placed
  behind paragraphs of body text. Every glass surface must meet WCAG AA
  contrast for any text it carries, and must define a solid background
  fallback for browsers without backdrop-filter support.
- All colors, spacing units, radii, and blur values live as CSS custom
  properties at the top of /css/site.css. No magic numbers in component rules.
