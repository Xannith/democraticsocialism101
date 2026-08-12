# Open Items

Punch list for the next working session, compiled from the evidence of the
Phase 5 launch session. Each item has a checkbox, a one-line description, and an
effort guess (small, medium, or large). Items are ordered by value within each
heading.

## 1. Generalized claims (Path B)

These claims were softened because verification did not produce a specific
source. Restoring the specific version is the highest-value follow-up.

- [x] **NHS public support** (`case-studies/united-kingdom.html`): RESOLVED
  2026-08-12, but not in the direction this item anticipated, and that is the
  point worth keeping. The item asked to restore the specific version of "remains
  widely supported across the political spectrum." The British Social Attitudes
  2025 results, published by The King's Fund and the Nuffield Trust in March 2026
  and read in full, support the first half and contradict the second. Founding
  principles do command large majorities: free at the point of need 89 percent,
  primarily tax-funded 81 percent, available to everyone 74 percent. But the
  report states that party differences on universality "were especially
  pronounced," with 68 percent of Labour supporters saying the principle should
  "definitely" apply against 45 percent of Conservative supporters and 30 percent
  of Reform supporters. Restoring the claim as originally written would have made
  the site wrong. The page now carries the sourced figures, names the party gap,
  and separates support for the principles from satisfaction with the service,
  which was 26 percent in 2025, up 6 points on 2024 and still low.
  LESSON: a claim softened for lack of a source is not necessarily a true claim
  waiting for a citation. Sometimes the reason no source was found is that the
  claim is not quite right, and the fix is to change it rather than to prove it.

## 2. Cut claims (Path C)

None. No claim was cut during verification.

## 3. Removed or uncertain figures

No figure was removed. Two entries need watching.

- [ ] **Ocasio-Cortez DSA status** (`figures.html`): entry corrected during
  launch. Her self-identification as a democratic socialist is verified and is
  her basis for inclusion, but DSA withdrew its national endorsement of her in
  2024, so her current relationship to the organization is contested. Recheck at
  the next review and update if it changes. Effort: small.
- [ ] **Rashida Tlaib basis** (`figures.html`): included as "DSA-aligned" (2018
  DSA endorsement plus self-identification), which is a slightly weaker basis
  than the other three entries. Reconfirm a clear self-identification statement
  or current DSA membership. Effort: small.

## 4. Deferred quality items

Gates that passed with a caveat, or checks that could not be run here.

- [ ] **Lighthouse audit not run**: Lighthouse and a usable headless browser
  were not available in the build environment, so performance, accessibility,
  best-practices, and SEO scores were not measured. Manual accessibility and QA
  checks passed. Run Lighthouse against the deployed site after launch. Effort:
  small.
- [ ] **Secondary sources where primary is preferable**: a few citations are
  encyclopedic (for example Wikipedia for the Vienna Gemeindebau and the Alaska
  Permanent Fund). Upgrade to primary sources where practical. Effort: small.

## 5. Spec debt

- [ ] **No open decisions remain** in SITE-SPEC.md; section 10 is fully
  resolved. None outstanding.
- [ ] **Fly-stage features** (explicitly out of v1): interactive explainers,
  reading-level variants, and a guided argument explorer. Effort: large.

## 6. Content backlog

- [ ] **Place the uploaded image** `img/systems-of-government4.png`: uploaded to
  the repo during this session but not referenced by any page, and its intended
  use is unknown. Confirm whether it is a content diagram or a share image, then
  place and optimize it. It is currently about 7 MB and must be compressed and
  resized before use, especially for a phone-first audience. Effort: medium.
- [ ] **Real Open Graph image**: the current Open Graph and Twitter setup is
  tag-only with no image. Create a branded share image (about 1200 by 630) and
  reference it site-wide. Effort: medium.
- [ ] **Additional case study candidates**: more countries or cooperatives,
  each following the section 4 template and the verification workflow. Effort:
  large.
- [ ] **Pending DC and LA mayoral outcomes**: monitor for possible future
  `figures.html` entries, added only if a winner publicly self-identifies as a
  democratic socialist, per the inclusion rule. Effort: small.
- [ ] **Designed favicon**: replace the current SVG letter mark with a designed
  favicon. Effort: small.

## 7. Maintenance obligations

- [ ] **Figures page quarterly review**: the "Last verified" date is 2026-07-22;
  the next review is due by 2026-10-22. Reconfirm each figure's
  self-identification and affiliation against a current source and refresh the
  date. Recurring, every quarter. Effort: small.
