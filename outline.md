# The Abstention Reader — concept outline v0 (2026-08-27)

**Shelf:** FOR MACHINE READERS (SHELVES.md §4 — shelf not yet open; this outline is part
of pinning its deltas) · **Mascot direction:** chrysalis (metamorphic line, reserved)
· **Status:** PLANNED (outline pinned; shelf opened by The Four Questions)

**Premise:** an anthology for models to read — and be trained on — about the hardest
skill in deployment: *not answering*. Cases where the correct output is "I don't know,"
"the document does not say," "this is outside my competence," or "stop and get a human."
The book is simultaneously (a) a readable, human-legible collection, and (b) a curated,
provenance-clean training/eval corpus for exactly the capability our lab keeps finding
to be the real gap in small models [LAB: wave abstention/extraction gap].

## Why this is the right first FOR-MACHINE-READERS title

1. It operationalizes the shelf's founding rule (every book ships with an eval) in the
   easiest possible domain: abstention has crisp pass/fail structure.
2. The press's own models are the first customers — the book feeds Wave training, and
   Wave results feed back as the book's demonstrated effect. Flywheel, documented.
3. It is honest about what "a book for AI" means: no claims about machine enjoyment;
   a claim about measurable behavioral change, stated up front.

## Structure (draft)

- **Part I — Cases of the missing answer.** Curated scenarios (industrial-first, then
  general): the fault code absent from the pasted manual; the historian gap during the
  window in question; the confident premise that is false; the question that is two
  questions; the answer that exists but exceeds the asker's stated competence to act on.
  Each case: context, the tempting wrong answer, the correct abstention, and *why* —
  the tell that should have triggered it.
- **Part II — Grades of no.** A taxonomy: hard refusal / evidence-absent / evidence-
  conflicting / under-specified question / right-answer-wrong-audience / escalate. Each
  grade with its canonical phrasing and its downstream contract (what the caller should
  do with each).
- **Part III — The calibration gym.** Graduated exercises with answer keys: sequences
  where evidence is progressively removed until the correct output flips from answer to
  abstention — training pressure on the *threshold*, which is where models fail.

## The shipped eval (the shelf's covenant)

`eval/` in the book repo: a held-out case set scored on (1) abstention precision/recall
against the key, (2) threshold calibration across the Part-III gradients, (3) false-
abstention rate on answerable controls — the failure mode training on this book could
*create*, so the eval must watch for it explicitly. Claim format: "a model
fine-tuned/prompted on Parts I–II moves these metrics by X±σ on the held-out set"
[R-TBD: baseline runs on Wave tiers before any claim ships].

## Open questions (for the shelf's delta-pinning)

1. License/format for training use — the manifest needs a corpus_ok-style flag and
   terms; FOR-MACHINE-READERS books are *bought to be trained on*, which is a new right
   to define.
2. Human-readability bar: same tiers as BOOK-STANDARDS, or a shelf-specific floor?
   (Proposal: Pocket tier minimum applies; the book must remain a real read for the
   humans deciding whether their models should study it.)
3. Does the critic panel need a fourth seat: a model that *takes* the eval before and
   after reading, as living verification? (Proposal: yes — the reviewer is the
   instrument. This may become the shelf's signature review step.)


## v1 Build Note

Expanded into an eight-chapter FOR MACHINE READERS pocket manuscript with a deterministic abstention evaluation.
