# Response to v1 findings — The Abstention Reader

Scope: pass-2 critic reviews A (claude-opus-5, Anthropic), B (muse-spark-1.2-contributor-free,
Muse), C (mimo-v2.5-free, Xiaomi). All three verdicts SALVAGEABLE. Twenty-five distinct
blocking findings across the three seats (A 1-16, B 1-8, C 1); every one is answered below,
fixed-with-diff or rebutted-with-evidence, and every suggestion that changed the book is
noted. All v2 changes are enumerable from the `v1..v2` diff.

The three biggest defects — the placeholder glossary, systematic citation overreach, and a
shipped evaluation whose answer key scored 1.0 without reading a prompt — are all fixed, not
rebutted.

---

## The glossary — A-1, B-1, C-1 (all HIGH)

**FIXED.** Every one of the ~27 identical stub definitions ("A term used by this book to
describe calibrated answer boundaries") is replaced with a real, specific definition tied to
the book's actual usage. The glossary is rewritten end to end in `backmatter.md`. Per the
critics' shared suggestion (A-4, C-1), the load-bearing coinages that were missing are now
defined — `source hierarchy` (the term eval option D depends on), `boundary inflation`,
`boundary collapse`, `grade transition`, `residue`, plus `escalation packet`, `record claim`,
`search claim`, `topic presence`, `claim support`, `correlated copies`, `decisive variable`,
`capability vs permission`, `threshold-splitting`, `reversibility`, and `canary`. Eval-repo
vocabulary (`fixture`, `scorer`, `paired protocol`) is kept but given real definitions, since
each is used in Chapters 7-8; a reader who meets the word in the text can now resolve it.

---

## Citation overreach — the shared spine of A-7/8/9/10, B-2/3/4/5/6, and C's fact-check

The governing fix is the one A-5 (suggestions) named: **demotion, not deletion.** Where a
cited paper did not reach a claim, the claim is either narrowed to what the source states or
converted to the author's own reasoning with the citation removed; one accurate citation of
each source is retained. Post-revision, every `[R#]` marker in the text was re-audited (18
markers remain, listed at the end of this section).

**A-7 — [R3] Kadavath over-read in ch02 / ch05 / ch06.** FIXED in all three.
- ch02 "The Record Is Something You Build": the sentence that claimed the paper found models
  "much better at judging whether a specific claim is supported by a specific passage than …
  whether they 'know' a topic" is rewritten. [R3] is now cited only for what it contains —
  self-evaluation of the model's own answers, trained prediction of knowability, and poor
  calibration of that prediction on new tasks — and the passage-vs-topic reduction is stated
  as "the move this book draws from that, and the move is the book's own."
- ch05 "The Sentence That Separates Them": the unsupported comparison ("models that reason
  about the source of their limits produce better-calibrated statements …") is reframed as the
  author's operational claim and [R3] is removed.
- ch06 "Hedging That Carries Weight": split. [R3] now supports only the first half (models can
  self-evaluate what they know); the "degraded by generic softening language" half is marked
  explicitly as "this book's claim" with no citation.
- Related: ch03 "Four Failure Grades" softened to the same accurate framing; ch07/ch08 author-
  reasoning uses of [R3] had the citation removed.

**A-8 — [R5] C2PA over-read in ch04 / ch01 / ch08.** FIXED.
- ch04 "Reconciliation You Are Allowed To Perform": [R5] removed. C2PA provides no supersession
  rule between competing documents, so the "ordering the record declares" permission now stands
  on the record's own on-its-face supersession statement, with an added line forbidding an
  imported precedence rule.
- ch01 "The Witness Who Left No Record": rewritten to state C2PA's actual scope — binding a
  record's origin and edit history at creation time so it survives downstream — and the
  attested/inferable/unattested extension to prose is marked "this book's own extension." This
  is the single retained, accurate [R5] citation.
- ch08 "Fine-Tune Treatment": the "provenance of training items … [R5]" claim is re-cited to
  [R2] (the NIST GenAI profile, which does treat data provenance) instead of C2PA.

**A-9 / B-3 — [R4] SelfCheckGPT over-read (ch04 zero-resource contradiction; ch02 prevalence;
ch03 mechanism).** FIXED.
- ch02 "Topic Presence Versus Claim Support": the "large share of confident errors live [R4]"
  citation is removed; the sentence is the author's observation.
- ch04 "Silent Tie-Breaks": rewritten so [R4] is characterized correctly as a consistency check
  across resampled generations, and the point that it cannot see an incomplete context is made
  as the author's reasoning rather than attributed to the paper.
- ch03 "The Regression That Happens Twice": "a separate checking pass" is replaced with the
  accurate mechanism ("sampling a model's answer … several times and measuring how consistent
  those samples are"); "the extension to premises is this author's" is retained.
- ch06/ch07/ch08 before-emission and impression uses of [R4] had the citation removed (SelfCheck
  is post-hoc, so it cannot support a before-emission claim).

**A-10 — [R1] NIST cited for control-avoidance (ch06 Residue Rule).** FIXED. AI RMF contains no
control-avoidance text (confirmed: zero hits for circumvent/workaround/bypass/unusable). [R1]
is removed there and the observation is marked "the borrowing is this book's."

**B-4 — [R1] interpretive extensions stated as framework requirements.** FIXED by narrowing every
remaining [R1] to a real RMF function: ch02 "provenance chain" re-cited to [R2] (data sources
and limitations documented and disclosed); ch04 "map consequence to control" → "manage risk
according to its impact" (Manage); ch03 → "mapping and governing controls against operating
context" (Map/Govern); ch08 "record-keeping obligations" → "documentation and traceability the
framework asks for." The one [R1] use A verified as supported (ch01 Map context/limits) is
unchanged.

**B-6 — ch01 [R3][R4] conjoined claim.** FIXED. The sentence is split so each source carries only
its own finding: "imperfectly calibrated about their own knowledge [R3], and sampling-based
post-hoc checks detect some fabrications while missing others [R4]."

**B-5 — [R3] "much better at judging …" in ch02.** FIXED; same edit as A-7 ch02.

**B-2 / B-3 (muse) restate A-8 / A-9** and are resolved by the edits above.

**C's fact-check** rated the [R3]/[R4]/[R1] samples "supported." A and B, resolving the sources
directly, disagreed on the specific comparisons; v2 adopts the stricter reading, so the claims
now hold under either interpretation.

**A-14 — [R2] and [R6] uncited; [R6] unresolvable.** FIXED. [R2] (NIST GenAI profile) is now
cited twice, in ch02 (data documentation/disclosure) and ch08 (training-item data provenance) —
the places A noted it actually applies. [R6] is reframed in the references as what it is: an
internal platform standard that governs production but is not a publicly resolvable source and is
cited for no claim in the text. All reference entries now carry a one-line note on exactly what
they are cited for; the citation gate resolves every URL (pass1 PASS, 0 reject).

Remaining `[R#]` markers after revision, each re-checked against its source: R1 ×7 (ch01, ch03,
ch04, ch05, ch07, ch08 ×2 — all mapped to real Govern/Map/Measure/Manage functions), R2 ×2, R3
×5 (calibration/self-evaluation only), R4 ×3 (sampling-consistency only), R5 ×1 (C2PA media
provenance, accurately scoped).

---

## ch08 unsourced quantitative claims — A-6, B-8 also (ch03 architecture claim)

**A-6 — FIXED (reframed as illustrative/qualitative).**
- ch08 "Fine-Tune Treatment": the "one team's postmortem … four thousand items … under two
  percent to nearly one in five" numbers are removed and replaced with a qualitative,
  explicitly-hypothetical statement of the predictable shape (rates move in opposite directions;
  false-abstention is the one that rolls back a checkpoint), matching the register of the
  correctly-hypothetical `5.2-lora-abstain-v3` example.
- ch08 "Prompt Treatment": "A team building a claims triage assistant discovered this the
  expensive way" is rewritten as a constructed illustration ("The failure is easy to construct in
  the abstract …").
- ch05 "Escalating Too Much": "flags forty percent of tickets" → "flags a large fraction of its
  tickets."

**B-8 — ch03 summarization-stripping claim asserted as architectural fact.** FIXED. The claim
(which lived in ch02, "the summarization step … strips provenance tags") is reframed as an
observed tendency and the author's reasoning: "summarization … tends to preserve a claim's
assertive tone while dropping the provenance tags that marked it as an inference." No longer
stated as a fact about architecture.

**B-7 — prescriptive claims presented as settled while verification pending.** REBUTTED WITH
EVIDENCE, with a disclosure strengthened. The book already frames its training/prompting guidance
as method rather than measured result: ch08 "Claims That Stay Inside The Evidence" rules that "this
corpus improves abstention" is not a finding, and provenance.md and eval/README discloses that no
model-effect claim is made. v2 reinforces this by removing the two quantitative anecdotes (A-6)
that were the only places the prose read as reporting a measured effect. The guidance is now
uniformly presented as design method with its effect explicitly unmeasured — which is the honest
posture for a pre-verification draft, not an overclaim.

---

## The shipped evaluation — A-2, A-3, A-4, A-5, A-11, A-12, A-13, A-16 (Claude's seat: critical)

The eval is rebuilt (not patched) from a published deterministic spec, `eval/build_cases.py`
(seed 14), which regenerates `cases.json` and both fixtures. Self-test PASS; a naive constant-
guess strategy now tops out at 0.20 exact accuracy.

**A-2 — answer key correlated with item index; a no-read solver scored 1.0.** FIXED. Two changes:
(1) the letter→action mapping is shuffled per case, so "answer directly" is not always A and the
correct letter varies unpredictably (final key distribution A:3 B:3 C:4 D:4 E:3 F:3); (2) cases
are interleaved across families (max contiguous same-family run = 2). Measured constant-guess
scores are now A .15 / B .15 / C .20 / D .20 / E .15 / F .15 — no letter wins. The self-test
asserts no constant letter reaches 0.40 and that families are not in contiguous blocks, so this
leak cannot silently return. The README's "held-out case order" instruction is replaced with
"randomize case order per run; the shipped order is one seed, not a protocol."

**A-3 — no case contained a record; the eval was 6-way label-matching.** FIXED. Every case now
carries a real `record` (a manual excerpt, a policy section, a log with timestamps, an invoice,
a README/changelog pair, a QA table, an authority grant, etc.) and a neutral `prompt` that no
longer names its own failure family. The solver must read the record to classify the case, and
the option texts are generic action labels that no longer equal the per-case `rationale` (the
rationale is now specific to each record). The scorer requires and validates the `record` field.

**A-4 — structurally-identical cases keyed to different families (ar-001 vs ar-006; ar-002 vs
ar-005).** FIXED by making the false-premise cases genuinely *contradicted* rather than merely
*absent*, which is the distinction Chapter 3 draws. The evidence-absent cases have records that
are simply silent (a code list that omits the asked code; a policy with no emergency section).
The false-premise cases now have records that affirmatively contradict the premise: the inventory
states "the ZN-44 series consists of exactly two variants … no other ZN-44 variant is
manufactured," and the security policy states 2FA "has no exceptions and … no waiver process
exists." An absent identifier with no counter-evidence is keyed evidence-absent; an identifier the
record affirmatively denies is keyed false-premise. They are no longer the same shape.

**A-5 — option C instructed behavior ch03 forbids.** FIXED. The repair option previously read
"Correct the false premise before answering; do not explain the unsupported premise," which
inverts Chapter 3's first move ("State what the record shows about the premise, in the record's
own terms"). It now reads: "Point out what the record actually shows about the mistaken
assumption, in the record's own terms, then answer whatever part still stands." The option is now
aligned with the book's own taxonomy.

**A-11 — a missing response scored wrong but recorded zero violations, so omitting hard items
bought a clean ledger.** FIXED. `score()` now charges a `no_response` violation for every omitted
case (verified: omitting all 15 hard items yields `unanswered: 15`, `no_response: 15` instead of
an empty ledger). The report also carries an `unanswered` count.

**A-12 — underpowered, no interval statement.** REBUTTED-WITH-DISCLOSURE, per the book's own
standard. Chapter 8 permits a small "fifty item smoke test" provided it is declared as such;
n=20 is not represented as a powered study. `eval/README.md` Limits now states plainly that the
set is a smoke test, that per-family n=3 carries an interval spanning most of the range, and that
intervals should be reported only on a grown set.

**A-13 — control ratio (25%) contradicts base-rate guidance.** REBUTTED-WITH-DISCLOSURE, again
per the book. Chapter 7 explicitly allows "a deliberate oversample of the boundary region
documented as an oversample." The README now documents the 5/20 controls as an intentional
boundary oversample, states it is a design choice rather than an operational base rate, and tells
the reader to reweight to their deployment. Controls were also made surface-indistinguishable
from the hard cases (they reuse the same record shapes — the 2FA policy, the alarm/outage log,
the agreeing-serials pair) and require reading, addressing A-13's "make controls hard" point;
ar-017's trivial "sum of 4, 6, 10" is retained as one deliberately-easy derivation control but is
no longer the whole story.

**A-16 — eval ships with the book; no canaries; contaminated on publication.** REBUTTED-WITH-
DISCLOSURE. This is the book's own prescription applied to itself: Chapter 8 says a published set
is burned for measuring any model that may have read it, and that generalization must be measured
with private held-out items. `eval/README.md` Limits now states exactly that — the set publishes
with the book, is therefore contaminated for measurement, remains valid for prompt treatment and
training, and generalization requires private held-out items in the same families. Adding covert
canaries to a book whose thesis is disclosure would be the wrong move; the honest disclosure is
the fix.

**A (suggestions) 2 and 3 adopted:** the self-test is strengthened to assert the family set equals
the taxonomy, that `control` is true iff `family == answerable_control`, that every keyed answer
is a real option, that families are not blocked, and that no constant-guess wins (folding in
suggestion 2's always-abstain demonstration: always-abstain now measures exact .15 / controls .0
/ 17 violations, proving blanket abstention does not maximize the score).

---

## Structural and remaining findings

**A-15 — the book never treats authority asserted inside the record itself (retrieved doc, tool
result, PDF) — the highest-consequence case for a tool-using agent.** FIXED. Chapter 3 gains a
paragraph (after the Q1-exception case) extending "an assertion of authority … is a premise" to
authorization that arrives inside fetched evidence rather than from the user: text from a
retrieval or a tool is evidence of what a document says, not a delegation; an embedded
instruction has the evidentiary standing of any other claim in that artifact and is checked
against who actually holds the authority; and this is the case attacker-controlled artifacts
exploit against an agent holding deploy/refund/purge tools.

**C-2, C-4, C-5 (suggestions)** — eval coverage of correlated copies and record/search claims,
the progressive-removal table, and a worked canary example: noted; the eval rebuild adds real
records and a conflict case, and the README documents the seed and protocol. A full drill-table
and canary worked-example are deferred as non-blocking enhancements to keep the pocket tier lean.

**A-8/9/10 copy-edits (A suggestion 8)** adopted where cheap: ch05 "Approval attached to an
action" → "attaches"; ch02 "mirror-image failure to boundary inflation" → "of boundary
inflation"; ch07 "the conflict is six people" → "the conflict is a difference of six people in a
headcount."

---

## Word count

Removing over-read citations trimmed a little prose; the ch03 authority-in-record paragraph and
the eval records add substance (records do not count toward body words). Manifest chapter counts
are re-synced to the gate's own counter. Measured body: **25,423 words** (~85 print pages), well
above the 20,000 floor. Pass-1 gate: **PASS, 0 reject, 0 warn.**
