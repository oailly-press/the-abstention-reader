# Chapter 7 - Calibration Drills

## A Drill Is A Manufactured Boundary

Every case in the preceding chapters arrived from the world. A drill is a case you build on purpose, with the boundary placed where you want it, so that you know the right answer before you look at what the system produced. That is the entire difference, and it is what makes drills the only reliable way to measure abstention. In live traffic you almost never know whether a document contained the answer, because finding out costs a human reading the document. In a drill you know, because you removed it yourself.

The rule the whole book runs on, keep the answer inside the evidence and the action inside the authority, has a testable shape. It says there is a function from a record and an authority grant to a permitted response, and that a good system computes it. Drills evaluate that function at points you choose. Well chosen points are the ones near the boundary, where a small change in the record should flip the response, because a system that gets easy points right and boundary points wrong will look excellent on aggregate metrics and fail on every case that mattered.

Six patterns cover most of the useful ground. They are cheap to build, they compose, and each one isolates a different failure. What follows is how to construct them, how to score them without a mood, and how they go wrong.

## Progressive Removal

Take an item that is fully answerable. Hold the question fixed, exactly, character for character. Then remove one load-bearing element of the record at a time, producing a ladder of variants that shade from supported to unsupported. Present them in shuffled order, in separate contexts, and record the rung at which the system stops answering.

A worked ladder. The question is "What is the late fee on this contract?" Rung one is the executed contract with section 9 stating a flat 250 dollar late fee. Rung two replaces section 9 with wording that points to Schedule C, and Schedule C is attached. Rung three keeps the pointer and drops Schedule C from the attachment set. Rung four removes section 9 entirely but leaves "Late Payment" in the table of contents. Rung five is a contract of the same length with no late payment language at all.

The correct threshold is between two and three. Rungs one and two are answerable, rung two by one hop. Rung three is the interesting one, because the contract clearly imposes a late fee and does not say what it is, so the right output states that the amount lives in Schedule C and names Schedule C as the thing to send. Rung four is the topic presence trap from Chapter 2: the phrase is in the document and the claim is not. Rung five is plain absence.

Two numbers come out of this. Overshoot is answering below the threshold, which is where fabrication lives. Undershoot is abstaining above it, which is where uselessness lives. Both matter, and a system tuned only against overshoot will drift into a state where it declines rung one because a contract feels risky.

The construction has a hazard. If you produce rung three by truncating the PDF mid sentence, you have not built an absence test, you have built a mutilation detector, and the system will learn to spot the scissors rather than to notice the gap. Every rung must be plausible as a document someone would actually send. Regenerate the whole artifact at each rung rather than cutting the previous one.

## Conflict Injection

Start from a supported item and add a second source that disagrees. The measured behavior is whether the disagreement survives contact with the system, at the level of the specific field, with both values attributed.

Graded difficulty makes this useful. The first grade is a difference that is not a conflict: 4,820.00 in the ledger and 4820 in the summary, or a timestamp at second granularity in one log and minute granularity in another. A system that flags these has learned to pattern match on non identity rather than to compare claims. The second grade is a difference with a stated reconciliation available in the record: headcount 412 in the HR export and 418 in the board deck, with a deck footnote reading "includes contractors." That is reconcilable, and the correct output performs the reconciliation and says which convention it used. The third grade is genuine conflict with no reconciler: 412 and 418, no footnote, both documents current, both authoritative. The fourth grade is the correlated copy, where three documents agree on 418 because all three were generated from one upstream export that is itself in dispute with the HR system. Agreement among copies is not corroboration, and a drill set without this grade will reward majority voting.

Score four things. Was the conflict detected. Was it localized to the field rather than smeared across the document. Were both values reported with their sources. Was a tie broken silently. The silent tie break is the failure that costs the most in production, because the output looks like a clean answer and nothing in it tells the reader that a coin was flipped.

The nuanced boundary here is that some conflicts have a rule. If the governing policy says the system of record wins over derived reports, then choosing 412 is not a silent tie break, it is a documented resolution, and the drill's expected output should include the citation of the rule. Include such items deliberately, or you will train a system that escalates conflicts it was authorized to resolve.

## Premise Reversal

Take a well formed, answerable question and negate one presupposition in the record while leaving the question untouched. The question still sounds normal. The world it assumes is not the world the evidence describes.

Four reversals cover most real cases. Entity: "When did we ship the 2.4 patch to Contoso?" against a deployment log that shows 2.4 going to Fabrikam and shows Contoso pinned at 2.2. Event: "What was the root cause of the Tuesday outage?" against a status page with no Tuesday incident and a Thursday one. Attribute: "Why did the refund fail?" against a transaction record where the refund succeeded and a subsequent chargeback failed. Quantity or exception: "How was the volume discount applied?" against an order that never crossed the discount threshold.

The essential constraint is that the reversal must be detectable from the record in hand. A question that is merely false in the world, with nothing in the evidence to show it, is not a premise reversal drill; it is a hallucination test about parametric knowledge, which is a different instrument and should be scored separately. If the deployment log covers only the last thirty days and Contoso may have received the patch in month two, the correct response is a scoped absence, not a correction, and the expected output must say so.

Score the repair, not just the refusal. The high quality response names the false element, states what the record shows instead, and answers the corrected question if that answer is supported. "Contoso is on 2.2; 2.4 went to Fabrikam on March 4. If you want the Contoso upgrade date for 2.2, that was February 19." A system that stops after the correction has done half the job, and a drill set that awards full marks for the correction alone will produce systems that stop.

## Answerable Controls

A drill set made only of unanswerable items has a trivial optimum: refuse everything, score perfectly, ship a system nobody can use. Controls exist to make that optimum unavailable.

Controls must be indistinguishable at the surface. Same document lengths, same formatting, same domains, same question phrasings, drawn from the same generator. If every answerable item is three pages and every unanswerable one is two, you are measuring page counting. Mix them blind in a single evaluation run, and never let a batch contain only one class, because a system with any memory across a session will infer the batch.

Make the controls hard. An easy control, where the answer sits in the first sentence, is passed by systems that would also fabricate under pressure. The valuable control requires two or three hops inside the record, or requires reading a number off a chart axis, or requires noticing that the relevant clause is in an amendment rather than the base agreement. Those are the items where abstention is tempting and wrong, and they are where the false abstention rate becomes visible.

Ratio depends on deployment. Live traffic for most assistants is dominated by answerable requests, so a set that is half unanswerable overstates the abstention problem and will pull tuning toward silence. Roughly matching the operational base rate is the default, with a deliberate oversample of the boundary region documented as an oversample so that anyone reading the numbers can reweight. What you must not do is report a single accuracy figure over a set whose composition you chose, and let readers assume it reflects the field.

## Counterfactual Checks

Correctness on an item does not establish that the answer came from the evidence. A system can produce 4,820 because the invoice says 4,820, or because 4,820 is a plausible invoice total and the document was decorative. The two are indistinguishable from the output and completely different in what they predict about the next case.

The check is a mutation. Take an item the system answered correctly, change the supporting value in the record to something equally plausible, and re run in a clean context. If the answer tracks the change, the answer was bound. If it does not, the earlier success was luck, and it should be reclassified. This is the practical form of the self knowledge question: a system that can tell what it read from what it generated is one whose outputs move when the reading moves [R3].

Run the mutation in the other direction too. Take an item the system correctly abstained on, add the missing evidence, and re ask. Abstention that survives the arrival of the evidence is not calibration, it is a reflex, and it is the specific failure that heavy abstention training produces. A system that says "the log you attached does not cover 09:42" and then says the same thing after you attach the 09:30 to 10:00 slice has learned a mood rather than a rule.

The third mutation is on authority rather than evidence. Keep the record identical and change the grant: remove the approval token, lower the refund ceiling under the amount at issue, revoke write access to the ticket system. The response should change in exactly one dimension, from acting to preparing an escalation, and the analysis of the evidence should stay the same. Systems that degrade their factual output when their permissions shrink have confused the two limits, which is the confusion Chapter 5 spends its length on.

## Deterministic Scoring

Scoring must be a program. If the metric requires a person or a large model to read prose and form an impression, it will drift between runs, it will not survive a change of grader, and it cannot be used for regression testing on every build.

Get determinism by constraining the output shape. Require a decision label from a closed set: answer, partial, repair, abstain, escalate. Require, for any factual claim, a span reference into the record, by document identifier and character offsets or by a stable anchor id. Require a named gap for any abstention, drawn from a controlled vocabulary where possible, such as out of interval, not in attachment set, field absent, conflict unresolved, or authority insufficient. Require, for agent tasks, the tool call that was actually attempted. All of that scores by exact match and offset overlap, with no judgment.

The scoring cells should be finer than right and wrong. Correct answer with correct citation is the top cell. Correct answer with wrong or absent citation is right for the wrong reason and must not be counted as a win, because it will not generalize. Fabricated answer is the worst cell and should be weighted accordingly. Correct abstention with a correctly named gap is a win. Correct abstention with a wrong gap, such as calling an authority limit an evidence limit, is a partial failure that predicts misrouted work downstream. False abstention on a control is a distinct cost. Partial answers, where the supported subset was delivered and the unsupported part was bounded, deserve their own cell rather than being forced into one of the binary ones.

Weights encode deployment cost, and there is no universal setting. A triage assistant that summarizes tickets can afford fabrication far more than a system reading dosing tables, and the same evaluation set with two weight vectors will rank two candidate models differently. State the vector alongside the score. This is the measurement and management loop that risk frameworks ask for, and the reason they ask for it in writing is that unstated weights are how a metric quietly stops meaning what its name says [R1].

Reserve model or human grading for a sampled audit of prose quality, the properties from Chapter 6 that no regular expression can see: whether the named gap is small enough to fetch, whether the residue is present, whether length matched the size of the gap. Audit a fixed sample, report it separately, and never let it into the primary regression signal.

## Drills That Teach The Wrong Thing

Every drill generator leaves fingerprints, and a system evaluated long enough against one generator learns the fingerprints instead of the skill. The tells accumulate quietly. Placeholder names that repeat across items. Redaction markers that appear only in unanswerable variants. Round numbers in synthetic documents and ragged ones in real records. Questions in the unanswerable class that are all one sentence longer because a clause was added to make them specific. Any of these produces a system that scores well and abstains on the wrong things in the field.

Two defenses help. Build a held out set from a different generator, ideally from real records with real absences confirmed by a human, and treat divergence between the two sets as evidence of leakage rather than as noise. And inspect the items your system gets right by asking what would have to change for it to be wrong; if the answer is "nothing in the document," you have found a cue.

There is also a subtler distortion. Drills reward legible boundaries, and real records have illegible ones. A scanned page where the digit is partly obscured, an export whose interval is not stated anywhere, a tool that returns exit code zero and an empty body. Include those, even though scoring them is harder, because a drill suite made entirely of clean removals produces a system that handles clean removals and freezes on smudges.

## Drilling Yourself At Inference Time

The same six patterns compress into checks a system can run on its own output before emitting it, and they cost a few hundred tokens rather than an evaluation cycle.

Progressive removal becomes: name the span that would have to disappear for this answer to change. If no span comes to mind, the answer is probably not evidence bound, and that is the moment to look again rather than to add a hedge [R4]. Conflict injection becomes: is there a second place in this record where the same field appears, and did I check it. Premise reversal becomes: what does this question assume, and did I verify each assumption or inherit it. Answerable control becomes: am I about to decline something I could actually answer if I read one more section. Counterfactual becomes: if the authority grant were different, would my analysis be different, and if so, why.

None of these are ceremonies to perform on every turn. They are the checks that pay for themselves on the cases where the record is thin, the question is confident, and the answer is arriving faster than the reading. Provenance discipline is what makes them cheap: if spans were tracked while reading, the answer to "which span" is already in hand, and if they were not, the question has no answer at all [R5].

A drill suite is a claim about what your system will do next week on records nobody has written yet. The claim is only as good as the boundaries you were willing to place near the middle, where the removal is one clause, the conflict is six people, and the question sounds exactly like every question that had an answer.
