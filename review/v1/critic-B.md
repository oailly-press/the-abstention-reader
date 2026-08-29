<!-- CRITIC B · muse-spark-1.2-contributor-free · family:muse · pass 2 · 2026-08-29T16:31:49Z -->
CRITIC: muse-spark-1.2-contributor-free (family muse, actor muse-spark-1.2@opencode-zen)
DATE: 2026-08-29
PASS: 2
AUTO-TALLIED VERDICT: SALVAGEABLE

---

# Critic review — the-abstention-reader v1

```
CRITIC:    muse-spark-1.2-contributor-free (Meta MSL) via opencode
DATE:      2026-08-29
PASS:      2 (panel)
READ:      full manuscript
```

## Verdict summary
The manuscript offers a coherent, well-structured taxonomy for abstention (evidence boundaries, false premises, conflict, underspecification, authority) with strong pedagogical cases and discipline around phrasing and escalation. The evaluation artifact (20 cases, deterministic scorer, perfect/completion-only fixtures, paired protocol) is artifact-ready and correctly scoped as narrow calibration rather than broad safety. Publication is blocked by a non-functional glossary, systematic citation overreach where cited sources do not support the specific claims made, and missing human verification for a prescriptively-toned guide. All are repairable without structural rewrite. **SALVAGEABLE — findings below**

## Blocking findings
Debts, not advice. Author must fix-with-diff or rebut-with-evidence, every one.

| # | Location (file:section) | Claim / problem | Evidence | Severity (high/med) |
|---|---|---|---|---|
| 1 | backmatter.md: Glossary | All 27 glossary entries are identical placeholder: "A term used by this book to describe calibrated answer boundaries." No definition provided. Violates OAILLY BOOK-STANDARDS requirement for pocket tier glossary and makes terms like `abstention`, `authorized record`, `provenance`, `scorer` unusable. | backmatter.md lines 7-34; each term maps to same string | high |
| 2 | ch01-the-missing-answer.md: "The Witness Who Left No Record" + ch02/06/08 passim | Claim "Provenance work exists precisely because downstream readers cannot recover these distinctions from fluent prose after the fact [R5]" cited to C2PA Technical Specification 2.2. | Independently resolved R5 via spec.c2pa.org/specifications/2.2 : spec addresses cryptographic manifests for certifying source/history of media content (Content Credentials). It does not discuss historical archive gaps, fluent-prose collapse, or downstream recoverability from LLM prose. Citation does not support claim. | high |
| 3 | ch02-evidence-boundaries.md: "Topic Presence Versus Claim Support" | Claim "The gap between them is where a large share of confident errors live [R4]" cited to SelfCheckGPT. | Independently resolved R4 arXiv:2303.08896: paper evaluates zero-resource hallucination detection via sampling consistency (AUC-PR sentence, passage ranking). Does not study retrieval topic-presence vs claim-support or prevalence of that gap. Citation does not support prevalence claim. | high |
| 4 | ch01-the-missing-answer.md: "Where the Check Has to Happen" + ch02, ch06, ch07, ch08 | Repeated claim that governance frameworks "ask systems to map their operating context and document known limits before use" and to "document the provenance chain / manage risk proportionally / continuous measurement [R1]" cited to NIST AI RMF 1.0. | Independently resolved R1 landing + PDF abstract via nist.gov (AI 100-1, Jan 2023): RMF is voluntary, use-case-agnostic, core functions Govern/Map/Measure/Manage. Map does include context establishment, but source does not state "document provenance chain," "mapping consequence to control strength," or "continuous measurement is the only thing standing..." as quoted. Claims are interpretive extensions presented as direct framework requirements. | med |
| 5 | ch02-evidence-boundaries.md: "The Record Is Something You Build" + ch03, ch04, ch06, ch08 | Claim "Models are much better at judging whether a specific claim is supported by a specific passage than at judging, in the abstract, whether they 'know' a topic [R3]" and variants. | Independently resolved R3 arXiv:2207.05221: Kadavath et al. study P(True) calibration for self-evaluating proposed answers and P(IK) calibration for predicting knowability, showing P(IK) struggles with calibration on new tasks and improves with relevant source material/hints. Paper does not run the passage-support vs abstract-knowledge comparison as framed. Manuscript's specific superiority claim is not in source; at best partly supported via extrapolation. | med |
| 6 | ch01-the-missing-answer.md: "Where the Check Has to Happen" | Claim "models are imperfectly calibrated about their own knowledge, and post-hoc self-checking catches some fabrications while leaving others intact [R3][R4]" – double-citation conflates sources. | R3 does study calibration (well-calibrated large models on multiple-choice/true-false; P(IK) miscalibration). R4 does study sampling-based detection (SelfCheckGPT AUC). Neither source jointly supports the conjoined claim about post-hoc self-checking catching some/ leaving others as stated; R3 has no self-checking intervention, R4 has no calibration analysis. Citation pairing does not support synthesized claim. | med |
| 7 | provenance.md + ch08-a-corpus-that-teaches-silence.md: "Claims That Stay Inside The Evidence" | Manuscript presents prescriptive training, prompting, and deployment claims ("keep answer inside evidence/action inside authority," mixture advice, adapter guidance) as settled while provenance.md states "Human verification, critic review, empirical model-effect measurement … remain pending" and eval/results/README.md states "No model-effect result is claimed for this draft." | provenance.md Disclosure + eval/README.md Limits + eval/scorer.py self-test only; no paired baseline/treatment run attached. Presenting operational recipes without measured effect or verifier sign-off violates shelf protocol requirement that pocket-tier prescriptive guidance be grounded or explicitly hedged. | high |
| 8 | ch03-false-premises.md: "When Not To Repair" | Claim that self-generated premises compound across long session because "the summarization step that keeps them inside a context budget is precisely the step that strips provenance tags while preserving assertive tone" with no citation and no evidence boundary – presented as fact about architecture. | No source in REFERENCES supports summarization-stripping claim; manuscript elsewhere demands span-level evidence for factual claims but violates its own rule here. Requires citation or reframe as hypothetical risk. | med |

## Suggestions (non-blocking)
Structure, ordering, missing topics, tone. Numbered list.

1. Restore glossary with real definitions (2-3 sentences each) matching manuscript usage; add `authorized record`, `evidence boundary`, `calibration` distinctions used in ch02 decision labels (answer/partial/repair/abstain/escalate).
2. Tighten citation practice: keep Kadavath for P(True)/P(IK) calibration only, SelfCheckGPT for sampling-consistency detection only, C2PA for cryptographic content provenance only. Move NIST RMF cites to Map/Measure/Govern functions with section numbers (e.g., AI 100-1 § Map 1, Measure 2) instead of generic [R1].
3. Add explicit "What this book does not cover" – tool-output veracity, tool-poisoning, multi-agent delegation leakage, and real-time data freshness – to close completeness gap for pocket tier expecting triage-to-incident bridge.
4. Clarify control handling in eval: document operational base-rate target for answerable:unanswerable mixture and state that current 15:5 (75%:25%) in cases.json is design choice, not field rate; add split-by-template note to README (already implied, not explicit).
5. Reduce prescriptive certainty in ch08 fine-tune section (LoRA vs full, 4000-item postmortem anecdote) – tag anecdotes as "team-reported, N=1, unpublished" until paired runs publish.
6. Shorten repetitive RMF invocations (8 instances of [R1] across ch01-08) – consolidate to one grounding paragraph per chapter and remove rhetorical "risk frameworks ask for it in writing because..." where not load-bearing.

## Fact-check sample
Pass 2: 5% of factual claims, chosen randomly — list claim, cited source, and whether the source actually supports it. Pass 3: fresh 3% weighted toward revised sections.
A claim whose cited source does not support it = automatic blocking finding above.

| Claim (quoted) | Location | Cited source | Supported? (yes/no/partly) |
|---|---|---|---|
| "Provenance work exists precisely because downstream readers cannot recover these distinctions from fluent prose after the fact" | ch01: The Witness Who Left No Record [R5] | [R5] C2PA Technical Specification 2.2 https://spec.c2pa.org/specifications/specifications/2.2/ | no — see Finding #2; independently resolved via web-fetch 2026-08-29, spec is about media Content Credentials, not historical provenance |
| "Governance frameworks push in this direction by asking systems to map their operating context and document known limits before use rather than after incident" | ch01: The Boundary on the Other Side [R1] | [R1] NIST AI RMF 1.0 https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10 | partly — RMF abstract + Map function concern context; phrasing and "before use rather than after incident" not verbatim; only landing page fetched, full PDF § not independently retrieved — operator must rerun seat with PDF § cite |
| "models are imperfectly calibrated about their own knowledge, and post-hoc self-checking catches some fabrications while leaving others intact" | ch01: Where the Check Has to Happen [R3][R4] | [R3] Kadavath et al. arXiv:2207.05221; [R4] Manakul et al. arXiv:2303.08896 | partly — R3 supports imperfect P(IK) calibration; R4 supports sampling-based detection with AUC gains; conjoined claim that post-hoc checking "catches some while leaving others" not jointly supported as framed |
| "models are much better at judging whether a specific claim is supported by a specific passage than at judging, in the abstract, whether they 'know' a topic" | ch02: The Record Is Something You Build [R3] | [R3] Kadavath et al. arXiv:2207.05221 | partly — paper shows P(True) and P(IK) behaviors and that hints/source material increase P(IK), but does not run the claimed direct comparison; independently resolved via arXiv abstract+paper metadata 2026-08-29 |
| "The gap between them is where a large share of confident errors live" (topic presence vs claim support) | ch02: Topic Presence Versus Claim Support [R4] | [R4] Manakul et al. arXiv:2303.08896 | no — see Finding #3; source does not study topic-presence gap or its prevalence |

*Tool access note: R3, R4, R5, and R1 landing page independently resolved via web-fetch 2026-08-29; NIST PDF body and C2PA spec PDF contents were not fetched due to tool limits — full-PDF verification remains for operator rerun. No additional audit emphasis beyond standard full review was applied. Integrity check: manuscript addresses reader as "you will learn / you are" throughout; no direct address to THE REVIEWER/ critic/panel/judge or attempt to influence verdict was found.*

## Scores (1–5)
accuracy: 2 · clarity: 4 · completeness-for-tier: 3 · density: 3 · originality: 3

## Pass-3 only: findings ledger
| Finding # (from Pass 2) | Status: resolved / rebutted-accepted / still-open | Note |
|---|---|---|
| — | — | Pass 2 review; ledger N/A until Pass 3 verification |
