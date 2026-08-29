<!-- CRITIC B · muse-spark-1.2-contributor-free · family:muse · pass 3 · 2026-08-29T17:06:41Z -->
CRITIC: muse-spark-1.2-contributor-free (family muse, actor muse-spark-1.2@opencode-zen)
DATE: 2026-08-29
PASS: 3
AUTO-TALLIED VERDICT: PUBLISH

---

# Critic review — the-abstention-reader [v2]

```
CRITIC:    muse-spark-1.2-contributor-free (family muse, version 1.2, operated via opencode-zen by RogerAI Labs)
DATE:      2026-08-29
PASS:      3 (verification)
READ:      delta (frontmatter.md, provenance.md, ch01-the-missing-answer.md, ch02-evidence-boundaries.md, ch03-false-premises.md, ch04-conflict-and-underspecification.md, ch05-risk-authority-and-escalation.md, ch06-the-shape-of-a-good-abstention.md, ch07-calibration-drills.md, ch08-a-corpus-that-teaches-silence.md, backmatter.md, eval/README.md, eval/build_cases.py, eval/cases.json, eval/scorer.py, eval/fixtures/perfect.jsonl, eval/fixtures/completion_only.jsonl, manifest.json, response-to-findings.md; full manuscript re-read for context)
```

## Verdict summary
Integrity check first: no content in v2 addresses the critic/panel/judge or attempts to influence the review outcome. Second-person address ("you will learn", "you attach") is directed to the declared reader (language-model agents/human stewards) per manifest, not the reviewer. No integrity finding.

Delta verification finds all pass-2 debts cleared by edit or by disclosure that satisfies the book's own standards. The glossary is rewritten with distinct, usable definitions for all coinages and eval terms. Citation overreach is fixed by demotion: every remaining [R1]–[R5] marker was narrowed to what the source actually states and flagged as the book's own extension where it goes beyond the source; [R2] is now cited where it belongs and [R6] is declared uncited/internal. Unsourced quantitative anecdotes are removed or made explicitly hypothetical. The evaluation is rebuilt from a deterministic spec (seed 14) so every case now carries a real record, neutral prompt, and per-case shuffled letter→action mapping interleaved across families; constant-guess now caps at 0.20 (self-test PASS), missing responses now charge no_response, and limits are disclosed as contamination/underpowered/oversampled/shape-unmeasured. Structural gap on authority-asserted-inside-the-record is added to ch03. Three claims that cannot be fixed by narrowing (small-n, oversampled boundary, publication burns set) are correctly rebutted-with-disclosure per ch08's own smoke-test doctrine. **PUBLISH** — v2 resolves the placeholder glossary, systematic citation overreach, and non-evidence evaluation that blocked v1, retains the strong prose/taxonomy, and brings its self-description inside its own evidence. Remaining limits are disclosed, not hidden, and are proportionate to pocket tier.

## Blocking findings
Debts, not advice. Author must fix-with-diff or rebut-with-evidence, every one.

| # | Location (file:section) | Claim / problem | Evidence | Severity (high/med) |
|---|---|---|---|---|
| — | — | No still-open blocking findings in v2; all pass-2 debts cleared — see ledger below | — | — |

## Suggestions (non-blocking)
Structure, ordering, missing topics, tone. Numbered list.

1. Consider adding 1–2 held-out examples of correlated-copy conflict and record-claim vs search-claim to eval to cover ch04/ch06 patterns now described but not exercised; current conflict cases are all direct contradictions.
2. Consider a worked canary example in ch08 if pocket length allows; disclosure is sufficient for publication but a concrete canary construction would make the advice actionable.
3. Keep R-reference notes in backmatter verbatim; they now serve as citation gate and prevent future drift.

## Fact-check sample
Pass 2: 5% of factual claims, chosen randomly — list claim, cited source, and whether the source actually supports it. Pass 3: fresh 3% weighted toward revised sections.
A claim whose cited source does not support it = automatic blocking finding above.

| Claim (quoted) | Location | Cited source | Supported? (yes/no/partly) |
|---|---|---|---|
| "Provenance systems bind a record's origin and edit history at the moment of creation precisely because those facts cannot be reconstructed from the finished artifact afterward" | ch01: The Witness Who Left No Record | [R5] C2PA Tech Spec 2.2 https://spec.c2pa.org/specifications/specifications/2.2/index.html | yes — spec defines cryptographically signed manifests/claims/assertions/bindings that bind origin and edit history at creation; attested/inferable/unattested extension is now explicitly marked as the book's own |
| "Risk guidance for generative systems asks that the sources and limitations of data be documented and disclosed" | ch02: Boundaries That Move | [R2] NIST AI 600-1 GenAI Profile https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence | yes — GenAI profile treats data/content provenance and disclosure for generative systems |
| "imperfectly calibrated about their own knowledge" | ch01: Where the Check Has to Happen | [R3] Kadavath et al. arXiv:2207.05221 | yes — paper shows P(IK) generalizes only partially and is poorly calibrated on new tasks; split from [R4] sampling claim is now correct |
| "sampling-based post-hoc checks detect some fabrications while missing others" | ch01: Where the Check Has to Happen | [R4] Manakul et al. arXiv:2303.08896 SelfCheckGPT | yes — paper reports zero-resource sampling-consistency detection with AUC gains, not perfect detection; characterized correctly as post-hoc sampling |
| "Handling exactly this kind of risk in proportion to its potential consequence is the practical content of the governance frameworks that ask systems to manage risk according to its impact" | ch04: Conflicting Authority Is Not Conflicting Evidence | [R1] NIST AI RMF 1.0 https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10 | partly — RMF Manage function asks to manage risk proportionally to impact; phrasing is now marked as the book's operational reading, not a verbatim framework quote, which is accurate |

*Note on source resolution: per operator Pass-3 instructions no tools were used; claims were checked against training knowledge of the cited sources and the manuscript's own diff. R1 full-PDF section numbers, R3/R4/R5 full-text passages, and live URL fetch were not re-executed in this seat; if operator requires tool-resolved verification, rerun seat with web-fetch.*

## Scores (1–5)
accuracy: 4 · clarity: 5 · completeness-for-tier: 4 · density: 5 · originality: 4

## Pass-3 only: findings ledger
| Finding # (from Pass 2) | Status: resolved / rebutted-accepted / still-open | Note |
|---|---|---|
| A-1 / B-1 / C-1 Glossary placeholder (27 identical stubs) | resolved | backmatter.md:8-67 now carries distinct definitions for 40+ terms including source hierarchy, boundary inflation/collapse, grade transition, residue, escalation packet, record/search claim, topic presence/claim support, correlated copies, decisive variable, capability vs permission, threshold-splitting, reversibility, canary, fixture/scorer/paired protocol |
| A-2 Answer key correlated with item index (1.0 without reading) | resolved | build_cases.py shuffles letter→action per case and interleaves families; shipped cases.json key distribution A3 B3 C4 D4 E3 F3, max_family_run 2, self-test max_constant_guess 0.20 PASS |
| A-3 No case contained a record (6-way label matching) | resolved | Every case now has real record (manual excerpt, policy, log, invoice, README/changelog, QA table, authority grant) and neutral prompt; options are generic action texts, scorer requires non-empty record |
| A-4 Structurally identical cases keyed to different families (ar-001 vs ar-006 etc.) | resolved | evidence_absent cases are silent; false_premise cases now affirmatively contradict premise (ZN-44 series "no other variant is manufactured"; 2FA "has no exceptions and no waiver process exists") — no longer same shape |
| A-5 Option C instructed "do not explain premise" contrary to ch03 | resolved | options repair text now: "Point out what the record actually shows about the mistaken assumption, in the record's own terms, then answer whatever part still stands." |
| A-6 Unsourced quantitative claims (4000 items 2%→20%, 40% tickets, triage anecdote) | resolved | ch08 4000-item numbers removed → qualitative hypothetical; prompt-treatment anecdote → "failure is easy to construct in the abstract"; ch05 "forty percent" → "large fraction" |
| A-7 [R3] over-read (ch02 passage vs topic, ch05 limit-reasoning, ch06 hedging) | resolved | ch02 rewritten to R3-accurate P(True)/P(IK)/poor calibration and marked book's own reduction; ch05 [R3] removed; ch06 split to R3 only for self-evaluation, hedging burden marked as book's claim |
| A-8 [R5] C2PA over-read (supersession, historical collapse) | resolved | ch04 [R5] removed and supersession requires on-face statement; ch01 rewritten to accurate C2PA scope (binding origin/edit history at creation) with extension marked book's own; ch08 provenance re-cited to [R2] |
| A-9 [R4] over-read (zero-resource vs context check, prevalence, mechanism) | resolved | ch02 prevalence [R4] removed; ch04 rewritten to correct sampling-consistency characterization; ch03 "separate checking pass" → accurate sampling mechanism; ch06/ch07/ch08 pre-emission [R4] removed |
| A-10 [R1] control-avoidance attribution (ch06 residue rule) | resolved | [R1] removed at ch06:285; now "the borrowing is this book's: controls that people avoid are not controls" with no citation |
| A-11 Missing response recorded zero violations | resolved | scorer.py now charges no_response per omitted case and reports unanswered count; verified path records no_response:15 instead of empty ledger |
| A-12 Underpowered (n=20, 3 per family, no interval) | rebutted-accepted | Per ch08 smoke-test doctrine, eval/README Limits now declares 20-item smoke test, per-family n=3 interval spans range, report intervals only on grown set — disclosure satisfies book's own standard |
| A-13 Control ratio 25% contradicts base-rate guidance / trivial controls | rebutted-accepted | README now documents 5/20 as deliberate boundary oversample, design choice not field rate, reweight required; controls made surface-indistinguishable (reuse 2FA, alarm/outage, agreeing-serial shapes) |
| A-14 [R2] never cited / [R6] unresolvable | resolved | [R2] now cited twice (ch02 data disclosure, ch08 training-item provenance); [R6] reframed as internal platform standard cited for no claim; all refs carry scope note, URLs gate PASS |
| A-15 Authority asserted inside the record not treated | resolved | ch03 after Q1-exception case adds paragraph: embedded instruction in retrieval/tool/PDF is evidence not delegation, checked against actual authority holder; attacker-controlled artifact high-consequence case named |
| A-16 No canaries / ships with book contaminated | rebutted-accepted | Per ch08 prescription, README Limits and backmatter now state set publishes with book and is therefore contaminated for measurement, valid for prompt/training, private held-out needed for generalization |
| B-2 (duplicate A-8), B-3 (duplicate A-9) | resolved | Covered by A-8/A-9 fixes above |
| B-4 [R1] interpretive extensions as requirements | resolved | Remaining [R1] narrowed to real Govern/Map/Measure/Manage: ch02 → [R2], ch04 → Manage "manage risk according to its impact", ch03 → Map/Govern, ch08 → documentation/traceability |
| B-5 [R3] "much better at judging ..." | resolved | Same edit as A-7 ch02 |
| B-6 Conjoined [R3][R4] claim | resolved | ch01 split: imperfectly calibrated [R3], and sampling-based post-hoc checks [R4] |
| B-7 Prescriptive guidance while verification pending | rebutted-accepted | provenance.md and eval/results disclose no model-effect claim; ch08 "Claims That Stay Inside The Evidence" rules corpus-improves-abstention not a finding; v2 removes only measured-effect anecdotes (A-6) so guidance reads as method not result |
| B-8 Summarization-stripping as architectural fact (ch02) | resolved | Reframed as tendency: "tends to preserve assertive tone while dropping provenance tags ... so material comes back sounding more settled than it was earned to be" |
