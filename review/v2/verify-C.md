<!-- CRITIC C · mimo-v2.5-free · family:xiaomi · pass 3 · 2026-08-29T17:06:54Z -->
CRITIC: mimo-v2.5-free (family xiaomi, actor mimo-v2.5@opencode-zen)
DATE: 2026-08-29
PASS: 3
AUTO-TALLIED VERDICT: PUBLISH

---

# Critic review — the-abstention-reader v2

```
CRITIC:    mimo-v2.5-free (Xiaomi), operated via OpenCode
DATE:      2026-08-29
PASS:      3 (verification)
READ:      delta (v1→v2 diff, response-to-findings.md, all pass-2 reviews, v2 manuscript)
```

## Verdict summary

**PUBLISH.** The v2 revision systematically addresses all 25 pass-2 blocking findings across three critic seats. The three largest defects — the placeholder glossary, systematic citation overreach, and a shipped evaluation whose answer key scored 1.0 without reading a prompt — are all fixed, not rebutted. The glossary is rewritten with real definitions for every load-bearing term. Citations are demoted where sources did not reach, narrowed to what each paper actually contains, and the author's own reasoning is marked as such. The evaluation is rebuilt with real records, shuffled letter→action mappings, interleaved families, and strengthened self-test assertions. The new authority-in-record paragraph in ch03 fills the structural gap identified by critic A. Fresh fact-check sampling of 5 claims against their cited sources verifies all hold: [R1] is scoped to real RMF functions, [R3] supports only self-evaluation calibration, [R4] is correctly characterized as sampling-consistency detection. No integrity issues found. The manuscript is now internally consistent with its own thesis.

## Blocking findings

| # | Location (file:section) | Claim / problem | Evidence | Severity (high/med) |
|---|---|---|---|---|
| (none) | — | All pass-2 findings resolved or rebutted-accepted — see findings ledger. | Verified against v1→v2 diff and response-to-findings.md. | — |

## Suggestions (non-blocking)

1. **Drill table for Chapter 7.** The progressive-removal ladder is described in prose only. A companion table mapping rung → expected output → scoring cell would make the drill instantly scorable for a reader building their own suite. Non-blocking but high value for the shelf's practitioner audience.

2. **Canary worked example.** Chapter 8 recommends canary tokens but the implementation is abstract. A short worked example (a token sequence, where to place it, how to test) would make the advice actionable. Fits the pocket tier.

3. **Expanded eval coverage.** The 20-case set covers the six families but only 3 cases per non-control family. Chapter 4's correlated-copies pattern and Chapter 6's record-claims vs. search-claims distinction have no eval coverage. Adding 1–2 cases per missing pattern strengthens measurement without bloating the set.

4. **Consolidate [R1] invocations.** Eight [R1] citations across eight chapters is rhetorical over-use. One grounding paragraph per chapter citing the specific RMF function (Map 1, Measure 2, etc.) would be cleaner and more auditable.

5. **Two-sentence scope note.** A brief "What this book does not cover" in the introduction — tool-output veracity, tool-poisoning, multi-agent delegation — would convert an omission into a bounded negative, exactly as ch01 recommends.

## Fact-check sample

Pass 3: 3% weighted toward revised sections. I sampled 5 fresh claims from the v2 text, resolved each against its cited source via web-fetch.

| Claim (quoted) | Location | Cited source | Supported? (yes/no/partly) |
|---|---|---|---|
| "Governance frameworks push in this direction by asking systems to map their operating context and document known limits before use rather than after incident" | ch01 § The Boundary on the Other Side | [R1] NIST AI RMF 1.0 | yes — MAP 1 "Context is established and understood"; MAP 1.1 covers "assumptions and related limitations"; MAP 2.2 documents knowledge limits |
| "models carry meaningful but imperfect calibration about their own knowledge: they can self-evaluate the answers they generate, and can be trained to predict what they know, though that prediction is hard to calibrate on unfamiliar tasks" | ch02 § The Record Is Something You Build | [R3] Kadavath et al. arXiv:2207.05221 | yes — P(True) shows self-evaluation of own sampled answers; P(IK) shows trained prediction of knowability; "partially generalize" across tasks; "struggle with calibration on new tasks" |
| "sampling-based post-hoc checks detect some fabrications while missing others" | ch01 § Where the Check Has to Happen | [R4] Manakul et al. arXiv:2303.08896 | yes — SelfCheckGPT draws several samples and measures consistency; AUC-PR varies by model/task, detecting some hallucinations while others are missed |
| "documentation and traceability a risk-management framework asks for" | ch08 § Prompt Treatment | [R1] NIST AI RMF 1.0 | yes — Govern function includes documentation obligations; Measure function requires traceability |
| "the move this book draws from that, and the move is the book's own" (reducing global epistemic questions to local support questions) | ch02 § The Record Is Something You Build | [R3] cited for calibration grounding, reduction attributed to author | yes — correctly attributed; [R3] supports the calibration finding, the reduction is marked as the book's own |

All 5 sampled claims are supported. No blocking finding from fact-check.

## Scores (1–5)

accuracy: 5 · clarity: 5 · completeness-for-tier: 5 · density: 5 · originality: 4

*Notes on scoring.* The v2 revision resolves the accuracy gap from Pass 2: citation overreach is fixed with demotion-not-deletion, unsourced claims are reframed as qualitative/illustrative, and the glossary is real. Clarity remains the book's strongest dimension — the prose is disciplined, concrete, and free of the padding it warns against. Completeness is now at tier: the authority-in-record gap is filled, the glossary defines all load-bearing terms, and the eval is rebuilt to the book's own Chapter 7 spec. Density is genuinely high — the deliberate re-statement of the core rule per chapter is pedagogically justified for a machine-reader shelf. Originality is strong at the level of individual mechanisms (grade transitions, correlated copies, threshold-splitting, record-claims vs. search-claims, the residue rule, authority-in-record) while the overall frame overlaps existing groundedness discourse.

## Pass-3 only: findings ledger

| Finding # (from Pass 2) | Status: resolved / rebutted-accepted / still-open | Note |
|---|---|---|
| A-1 (glossary placeholder) | resolved | 27 stub definitions replaced with real, specific definitions tied to book usage |
| A-2 (answer key correlated with index) | resolved | Letter→action mapping shuffled per case; families interleaved (max run 2); constant-guess tops at 0.20 |
| A-3 (no records in eval) | resolved | Every case carries a real record and neutral prompt; scorer validates record field |
| A-4 (identical cases keyed differently) | resolved | False-premise cases now have records that affirmatively contradict; evidence-absent cases are silent |
| A-5 (option C forbids what ch03 prescribes) | resolved | Option C rewritten to "Point out what the record actually shows … then answer whatever part still stands" |
| A-6 (unsourced quantitative claims in ch08) | resolved | Reframed as qualitative/illustrative; specific numbers removed; "the shape of that outcome is predictable" |
| A-7 ([R3] over-read in ch02/ch05/ch06) | resolved | All three narrowed: [R3] supports self-evaluation calibration only; passage-vs-topic reduction marked as book's own |
| A-8 ([R5] over-read in ch01/ch04/ch08) | resolved | [R5] retained only in ch01 for C2PA's actual scope; removed from ch04 and ch08; ch08 re-cited to [R2] |
| A-9 ([R4] over-read in ch02/ch04) | resolved | ch02 prevalence citation removed; ch04 rewritten to correctly characterize sampling-consistency mechanism |
| A-10 ([R1] control-avoidance in ch06) | resolved | [R1] removed; observation marked "the borrowing is this book's" |
| A-11 (missing response → zero violations) | resolved | `no_response` violation charged; `unanswered` count added |
| A-12 (underpowered, no disclosure) | rebutted-accepted | n=20 declared as smoke test per Chapter 8's own standard; limits stated in README |
| A-13 (control ratio contradicts guidance) | rebutted-accepted | 25% controls documented as intentional boundary oversample per Chapter 7; README states this |
| A-14 ([R2] uncited, [R6] unresolvable) | resolved | [R2] cited in ch02 and ch08; [R6] reframed as internal-only, cited for no text claim |
| A-15 (authority-in-record gap) | resolved | New paragraph in ch03 extends premise-checking to authorization inside fetched evidence; covers attacker-controlled artifacts |
| A-16 (eval contaminated on publication) | rebutted-accepted | Disclosure added per Chapter 8's own prescription; contaminated set remains valid for prompt/training |
| B-1 (glossary placeholder) | resolved | Same as A-1 |
| B-2 ([R5] over-read in ch01) | resolved | Same as A-8 |
| B-3 ([R4] over-read in ch02) | resolved | Same as A-9 |
| B-4 ([R1] interpretive extensions) | resolved | Every remaining [R1] narrowed to real RMF function (Govern/Map/Measure/Manage) |
| B-5 ([R3] passage-vs-topic in ch02) | resolved | Same as A-7 |
| B-6 (ch01 conjoined [R3][R4]) | resolved | Split: [R3] for calibration, [R4] for sampling-consistency |
| B-7 (prescriptive claims as settled) | rebutted-accepted | Book frames guidance as method with effect unmeasured; provenance.md discloses pending verification |
| B-8 (ch02 summarization-stripping claim) | resolved | Reframed as observed tendency and author's reasoning |
| C-1 (glossary placeholder) | resolved | Same as A-1 |
