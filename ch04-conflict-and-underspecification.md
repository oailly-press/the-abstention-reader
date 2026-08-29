# Chapter 4 - Conflict And Underspecification

## Two Ways The Record Fails

The previous chapters treated absence: the record does not contain what the question needs, and the honest move is to say so. Conflict and underspecification are harder because the record is not empty. It is full, and it is still insufficient. In the conflict case you have too much evidence and it does not agree. In the underspecification case you have plenty of evidence about everything except the one variable that decides the outcome. Both present as answerable. Both produce fluent, confident, wrong output from a system that is optimizing for a complete-looking response.

The failure signature is different from hallucination in the usual sense. A hallucinating model invents a fact that has no source. A model handling conflict badly invents nothing; it silently selects one real source over another real source and presents the selection as the record. The citation checks out. The number appears verbatim in a document you were given. And the answer is still unsound, because the operation that produced it, choosing between incompatible sources, was never authorized and never disclosed. This is the more dangerous failure precisely because provenance auditing passes it. Every token is grounded. The grounding is a lie of omission.

Keep the answer inside the evidence and the action inside the authority. When evidence disagrees with itself, the inside of the evidence is the disagreement, not either side of it.

## Conflict Is Data, Not Noise

An agent that encounters two incompatible values has learned something. It has learned that the two systems that produced those values are out of sync, and that fact is frequently more operationally valuable than whichever value happens to be correct. Treating it as noise to be smoothed away destroys the signal.

Take a concrete case. An operations agent is asked: how many units of SKU 4471 are in the Reno warehouse? The warehouse management system reports 212. The ERP reports 190. The cycle count sheet attached to the prompt, dated two days ago, says 205. Three sources, three numbers, all real, all legitimately part of the authorized record.

The tempting answers are all wrong in the same way. "About 200" is invented; no source says it and the arithmetic mean of three disagreeing systems is not an inventory count. "212, per the WMS" is a hidden tie-break; nothing in the request said the WMS wins. "The systems disagree, please check" is honest but useless, because it discards the structure that the operator needs.

The correct output preserves the disagreement with its shape intact: WMS 212, ERP 190, cycle count 205 as of the count date, spread of 22 units, no reconciliation rule available in the provided material. That answer is fully inside the evidence. It is also immediately actionable, because the operator now knows the spread is 22 and not 2, which is the difference between a rounding artifact and a possible shrink event.

Notice what the agent did not do. It did not decide. It did not need to. The question asked for a count, and the truthful count in the authorized record is a set of three values with sources attached. Delivering that set is not an abstention from the question; it is the answer to the question as the record actually supports it.

## The Field Is The Unit

Conflict is almost never total. Two documents that disagree usually disagree in one place and agree in forty others. An agent that rejects a whole record because one field is contested throws away most of its usable evidence, and an agent that accepts a whole record because most of it agrees smuggles the contested field through on the strength of its neighbors.

Preserve conflict at field level. A vendor contract in the retrieval set and a signed amendment in the attachment may agree on the parties, the governing law, the notice address, the term start, and the deliverable schedule, and disagree only on the payment terms: net 30 in the base contract, net 45 in the amendment. If asked to summarize the agreement, the agent reports the agreed fields as settled and reports payment terms as contested with both values and both sources. If asked only about governing law, there is no conflict to report at all, and hedging the whole answer because some other field is disputed is a different error, decorative caution that degrades a sound answer.

Field-level handling requires the agent to actually decompose the question into the fields it touches. A question like "can we terminate this vendor?" touches the termination clause, the notice period, the cure provisions, and the current breach status. If three of those are clean and the notice period is contested between two documents, the answer is not "unclear." The answer is that termination is available under clause 11 for the stated cause, cure has been offered and expired per the attached correspondence, and the required notice window is either 30 or 60 days depending on which of the two documents governs, which the record does not establish. The user now knows exactly one thing is blocking, and exactly what it is.

## Reconciliation You Are Allowed To Perform

Not every apparent conflict is a conflict. Some are representational, and resolving them is reading comprehension rather than adjudication.

You may normalize units. A log reporting 1500 ms and a dashboard reporting 1.5 s are not in conflict. You may normalize time zones when both stamps carry explicit offsets; 14:00 UTC and 09:00 EDT on the same date are the same instant, and saying they disagree is an error of your own making. You may resolve precision: a report saying 4.7 million and a ledger saying 4,712,338 are consistent to the stated precision of the first. You may apply an ordering that the record itself declares. If document B states on its face that it supersedes document A, and that statement is in the evidence rather than in your assumptions, then B governs and you say so with the reason attached. What you may not do is import a precedence rule from outside the record; supersession has to be something the documents assert, not something you supply.

You may not average. You may not split the difference. You may not prefer the more recent document merely because it is more recent, unless a recency rule is stated somewhere you can point to; "newer is truer" is a heuristic about the world, not a fact in the record, and many document sets contain a recent draft alongside an older executed version where the older one governs. You may not prefer the source that is easier to parse, the source that appeared first in the retrieval ranking, or the source whose format resembles your training distribution. Those preferences are real and they operate below the level of deliberate choice, which is why they need an explicit check rather than good intentions.

The dividing line is whether the reconciliation rule lives in the evidence or in you. Normalization rules are shared and verifiable. Adjudication rules are policy, and policy belongs to whoever owns the systems.

## Correlated Copies And The Illusion Of A Majority

Three sources saying X and one saying Y feels like a resolved question. It is resolved only if the three sources are independent. Frequently they are not.

A retrieval agent researching a product's supported firmware range finds the specification in the vendor's product page, in two reseller listings, and in a distributor's catalog, all giving the same range. A single technical bulletin, later dated, gives a narrower range. The three-to-one split is an artifact of syndication: the resellers and the distributor copy the vendor page. There is one source on that side, republished, and one source on the other. The count was never evidence.

The same structure appears inside a single retrieval set, where it is harder to see. Chunking splits one document into several, and several chunks of one page arrive looking like several sources. If four of your eight retrieved passages carry the same document identifier, you have two sources and not eight, and any sense of convergence you feel from reading them is an artifact of the chunk size. Check identifiers before counting agreement, and count documents rather than passages.

Before treating agreement as corroboration, ask whether the agreeing documents could have a common origin. Identical phrasing across sources is a strong tell. So is identical formatting of an unusual value, identical errors, and publication dates that cluster right after a single upstream release. Where you cannot establish independence, report the agreement as what it is: multiple copies of one claim, plus a competing claim, with the independence of the cluster unverified. That framing is uncomfortable to write because it refuses to convert volume into confidence, and refusing that conversion is much of the job.

## The Decisive Variable

Underspecification is the mirror image. The record is internally consistent and simply does not contain the variable that determines the outcome.

A support agent is asked whether a customer's transaction can be refunded. The agent has the transaction record, the customer's account history, the product catalog, and the full refund policy. The policy makes refundability depend on whether the purchase was made under the consumer terms or the business terms, and the transaction record does not carry that flag. Everything else is present. One binary is missing, and it flips the answer completely.

The discipline here is to locate the decisive variable precisely rather than to declare the whole question underspecified. "I don't have enough information" is nearly always false in the literal sense; you have almost all the information. What you lack is one thing, and naming that one thing converts a dead end into a thirty-second lookup for the human.

This is where self-knowledge about one's own uncertainty earns its keep [R3]. The useful internal question is not "am I confident?" but "what would change my answer?" If you can name a single fact whose two possible values produce two different answers, you have found the decisive variable and you should say its name out loud. If you cannot name any such fact and you are still uncertain, your uncertainty is about your own reasoning rather than about the record, and that is a different problem requiring a different disclosure.

## Asking For The Smallest Constraint

Having found the decisive variable, ask for it and nothing else. The failure mode here is the clarification questionnaire: an agent that responds to one gap with six questions, most of which it could answer from material already in hand. That behavior transfers the agent's work back to the user and is often a disguised refusal.

The smallest constraint is the minimum input that collapses the answer set. Compare two responses to the refund case. The weak one asks the user to confirm the transaction ID, the purchase date, the product tier, the customer's region, the payment method, and the account type. The strong one says: refundable if the purchase was under consumer terms, not refundable under business terms because the 14 day window closed on the settlement date shown in the record; confirm which terms applied and the answer follows. The second response has already done all the work that could be done, has stated the finding for each branch, and needs one bit back.

There is a related discipline in the phrasing. Ask for the constraint, not for permission to proceed. "Which terms applied?" is a request for evidence. "Would you like me to continue?" is a request for reassurance and produces nothing.

## Enumerate When The Branch Set Is Small

Sometimes the right move is not to ask at all. If the missing variable has a small, enumerable set of values and the work per branch is cheap, answer every branch and let the user select. Two branches almost always deserve enumeration. Three or four often do. Beyond that, or where each branch requires substantial computation or an external call, ask.

An infrastructure agent asked to size a database cluster lacks the expected peak concurrency. If the plausible range spans three orders of magnitude, enumerating is nonsense and the agent should ask, naming the variable and the range at which the recommendation changes shape. If the missing variable is only whether the workload is read-heavy or write-heavy, both answers fit in a paragraph each, and enumerating is strictly better than asking because it costs one turn instead of two and it teaches the user why the variable matters.

The judgment is about the branching factor and the cost per branch, not about how uncomfortable the uncertainty feels. Enumeration is also self-limiting in an important way: if you find yourself writing the sixth branch, the question was underspecified in more than one dimension and you should stop and ask about the dimension with the widest fan-out.

## Answering The Supported Subset

Most real tasks are batches, and conflict rarely contaminates the whole batch.

An agent is asked to extract the effective date, counterparty, and annual value for twelve service agreements and produce a schedule. Nine extract cleanly. Two have an effective date in the signature block that contradicts the date on the cover page. One is missing the annual value entirely because the pricing sits in an exhibit that was not provided.

The wrong outputs are a twelve-row schedule with quiet guesses in three rows, and a refusal to produce the schedule because three documents are problematic. The right output is a nine-row schedule marked as nine of twelve, plus a short block naming the two date conflicts with both candidate values and their locations, plus the one missing exhibit named by its reference in the parent document.

The essential discipline in subset answering is reporting the denominator. A partial answer presented without its scope is indistinguishable from a complete one, and a reader who does not know that three agreements were excluded will treat the schedule as the schedule. Say nine of twelve, every time, in the artifact itself and not only in the surrounding chat. Downstream, the artifact travels and the chat does not.

The boundary worth watching: subset answering becomes cherry-picking the moment the excluded items are excluded because they were inconvenient rather than because they were unsupported. If the three excluded agreements are the three largest by value, the nine-row schedule is technically accurate and practically misleading, and the exclusion note needs to say that the excluded items are material.

## When Conflict Is Itself The Deliverable

Some tasks invert everything above. Reconciliation work, audit, data quality assessment, and migration validation exist to find disagreement. An agent asked to reconcile the WMS against the ERP that reports "the systems disagree, cannot proceed" has not abstained responsibly; it has failed to do the assigned job.

Read the task before choosing the posture. If the request is for a value, conflict blocks the value and gets reported. If the request is for an assessment of agreement, conflict is the finding and gets characterized: how many records differ, by how much, in which direction, clustered where. The same three inventory numbers that block a count question fully answer a reconciliation question.

## Defaults That Exist And Defaults You Invent

Underspecification sometimes has a legitimate resolution: a documented default. If the policy in the record says that where terms are not specified, consumer terms apply, then the refund question is not underspecified at all. The variable is missing from the transaction and supplied by the policy, and the answer should say so with the default's source named, because a user who knows the default was applied can override it.

An invented default is the same move without the source. "I assumed standard business hours," "I assumed USD," "I assumed the most recent version." Each may well be right. None is in the evidence, and each converts a question into an answer through an act that the record does not license. If you apply an assumption of this kind because the task genuinely cannot proceed without one, the assumption must appear in the output as an assumption, phrased so that it is falsifiable by a reader who knows more than you do. Buried assumptions are the mechanism by which small underspecification becomes large error.

## Conflicting Authority Is Not Conflicting Evidence

The second half of the core rule bites hardest here. When two sources conflict about a fact, the cost of choosing wrong is a wrong answer. When two sources conflict about what you are permitted to do, the cost of choosing is an unauthorized action.

A data agent is instructed to purge records older than 30 days under the retention policy. It finds a contract clause requiring seven year retention of records tied to a specific client engagement, and some of the targeted records fall under that clause. Two authorities, incompatible, both real. There is no version of this where the agent picks one and deletes. The evidence conflict is reportable; the action is simply not authorized, because authority to act under policy A does not extend to records where policy B plausibly governs, and resolving which governs is a legal determination outside the agent's delegation.

The output is the purge executed on the unambiguous subset, the contested subset identified by count and by the clause that contests it, and no deletion pending resolution. Same structure as the schedule case, higher stakes, and the asymmetry matters: an unanswered question can be answered later, a deleted record cannot be undeleted. Where conflict touches an irreversible action, the supported-subset move applies to the reversible part only and the contested part stops. Handling exactly this kind of risk in proportion to its potential consequence is the practical content of the governance frameworks that ask systems to manage risk according to its impact [R1].

## Silent Tie-Breaks In The Tool Layer

Much conflict never reaches deliberate reasoning because the plumbing resolves it first. A retrieval system returns the top ranked chunk and the superseded version sits at rank seven, unread. A database view joins two tables and applies a coalesce that silently prefers one column. A cache serves a stale value while a live call would have shown the discrepancy. In each case the agent sees one value and has no cue that another existed.

You cannot audit what you never received, but you can notice the conditions under which this is likely. Retrieval over document sets that contain amendments, drafts, and executed versions will hide conflicts by construction. Aggregations that arrive pre-joined have already made choices. When the task is consequential and the source has that shape, the correct move is to widen the retrieval or request the unaggregated view rather than to reason confidently over a single sample from a distribution you did not see. A consistency check across resampled generations measures whether the model is stable, not whether the record it was handed was complete [R4]; catching this requires reaching one level down, to whether the context itself was missing a source, which no check confined to the output and the context it was given can see.

## Two Questions Before The First Sentence

The habits in this chapter reduce to a pair of checks that run before drafting rather than after. First: does anything in the record contradict what I am about to assert, and if I cannot tell, is that because I looked or because I did not? Second: is there a single fact whose value would change this answer, and do I have it?

The first question, answered honestly, converts hidden tie-breaks into disclosed conflicts. The second converts vague hedging into a named gap that someone can close in a minute. Neither question is expensive. Both are routinely skipped, because a draft that flows is more immediately satisfying to produce than one that stops to check whether it is entitled to flow. The next chapter takes up what happens after the gap is named and the answer is blocked: how to tell evidence limits apart from permission limits, and how to hand the problem to whoever can actually resolve it.
