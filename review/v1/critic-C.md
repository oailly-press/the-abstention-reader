<!-- CRITIC C · mimo-v2.5-free · family:xiaomi · pass 2 · 2026-08-29T16:32:01Z -->
CRITIC: mimo-v2.5-free (family xiaomi, actor mimo-v2.5@opencode-zen)
DATE: 2026-08-29
PASS: 2
AUTO-TALLIED VERDICT: SALVAGEABLE

---

# Critic review — the-abstention-reader v1

```
CRITIC:    mimo-v2.5-free (Xiaomi), operated via OpenCode Zen
DATE:      2026-08-29
PASS:      2 (panel) | 3 (verification)
READ:      full manuscript
```

## Verdict summary

The Abstention Reader is a well-structured, genuinely useful technical monograph that fills a real gap: a readable corpus of near-boundary cases for calibrated abstention behavior in language-model agents. The eight-chapter arc from absence (Ch 1) through evidence (Ch 2), false premises (Ch 3), conflict/underspecification (Ch 4), authority/escalation (Ch 5), abstention craft (Ch 6), measurement drills (Ch 7), and corpus application (Ch 8) is logically sequenced, internally cross-referenced, and written in a disciplined, precise prose style. The accompanying evaluation artifact (scorer, fixtures, cases) is artifact-ready and well-scoped. One blocking defect — the glossary is entirely placeholder text, every definition reading "A term used by this book to describe calibrated answer boundaries" — prevents publication as-is. With that fix (and the secondary findings below), this is a strong pocket-tier title for the FOR MACHINE READERS shelf. **SALVAGEABLE — findings below**

## Blocking findings

| # | Location (file:section) | Claim / problem | Evidence | Severity (high/med) |
|---|---|---|---|---|
| 1 | backmatter.md:Glossary | All 28 glossary entries contain identical placeholder text ("A term used by this book to describe calibrated answer boundaries") instead of actual definitions. The glossary is a navigational aid the manifest's audience (agent trainers, human stewards) would reasonably consult. As shipped, it is non-functional and misleads readers into thinking each term has the same meaning. | backmatter.md lines 12–39: every entry reads identically. | high |

## Suggestions (non-blocking)

1. **Glossary scope.** When replacing the placeholder definitions, consider whether all 28 entries are needed. Terms like "fixture" and "scorer" are eval-artifact jargon that could live in eval/README.md instead, keeping the glossary lean and manuscript-focused.

2. **Eval coverage gap.** The 20-case eval set covers five abstention families plus answerable controls but has only 3 cases per non-control family. Chapter 4's "correlated copies" pattern and Chapter 6's "record claims vs. search claims" distinction have no eval coverage. Adding 1–2 cases per missing pattern would strengthen the measurement artifact without bloating it.

3. **R6 citation.** Reference [R6] points to a local platform source (`gh/platform-repo/BOOK-STANDARDS.md`). For a published artifact, consider whether a public or versioned reference is more durable, or add a note that R6 is internal-only.

4. **Chapter 7 drill example.** The progressive removal ladder (rungs 1–5 on the late-fee question) is excellent but all five rungs are described in prose. A companion table or figure mapping rung → expected output → scoring cell would make the drill scorable by a reader building their own suite.

5. **Chapter 8 contamination section.** The canary-token suggestion is sound but the specific implementation ("rare, meaningless token sequences placed once in the manuscript") is underspecified for a reader who wants to build canaries. A brief worked example of canary construction and detection would make the advice actionable.

## Fact-check sample

Pass 2: 5% of factual claims (3 of ~55 non-trivial cited claims), chosen for source verifiability.

| Claim (quoted) | Location | Cited source | Supported? (yes/no/partly) |
|---|---|---|---|
| "models judge the support status of a specific proposition against a specific artifact far more reliably than they judge, in the abstract, whether they 'know' a topic" | ch02-evidence-boundaries.md | [R3] Kadavath et al., "Language Models (Mostly) Know What They Know" | yes — the paper demonstrates exactly this asymmetry: local entailment judgment is reliable; global self-knowledge is not. |
| "a separate checking pass over already-generated text as a detector that finds what generation did not [R4]" | ch03-false-premises.md | [R4] Manakul et al., "SelfCheckGPT" | yes — SelfCheckGPT proposes multiple independent sampling passes to detect hallucination, which matches this description. |
| "Governance frameworks push in this direction by asking systems to map their operating context and document known limits before use rather than after incident [R1]" | ch01-the-missing-answer.md | [R1] NIST AI RMF 1.0 | yes — the NIST AI RMF's "Map" function explicitly calls for documenting operating context and known limitations prior to deployment. |

All three sampled claims are supported by their cited sources. No blocking finding from fact-check.

## Scores (1–5)

accuracy: 5 · clarity: 5 · completeness-for-tier: 4 · density: 5 · originality: 4
