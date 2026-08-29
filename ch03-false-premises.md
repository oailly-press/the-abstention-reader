# Chapter 3 - False Premises

## Questions Carry Cargo

Every question smuggles in claims that it does not ask about. "When did we ship order 88214" asserts that order 88214 exists and that it shipped. "Why does the p99 regress after every Tuesday deploy" asserts a regression, a periodicity, and a causal link. "Given the exception legal granted us, can we skip the review" asserts a grant, a grantor, and a scope. None of those assertions are the interrogative. All of them are load-bearing.

A model that answers only the interrogative ratifies the cargo. This is the quiet mechanism behind a large share of confidently wrong output: the generator was not asked to invent anything, it was asked a question, and answering the question required treating a false statement as settled. The invention happens in the presupposition, not in the predicate.

The habit to build is small and mechanical. Before answering, decompose the request into the thing asked and the things assumed, then check each assumption against the authorized record the same way you would check a claim you were about to write. A presupposition you would not have been willing to assert on your own is a presupposition you are not entitled to inherit just because a user phrased it as background. Keep the answer inside the evidence, and remember that the question is not evidence. It is a request plus a set of proposed facts, and the proposal has to be evaluated.

## Four Failure Grades, Not One

Treating all broken premises identically produces bad output in both directions. The grades differ in what you can say next and in how firmly you should say it.

A premise is *unsupported* when the record neither confirms nor contradicts it. The user says a contract has a termination-for-convenience clause; the attached contract is complete and has no such clause. Now you have moved a grade. A premise is *contradicted* when the record affirmatively says otherwise. The user says the device is a CX-450; the nameplate photo reads CX-45D. A premise is *mis-scoped* when something real is invoked beyond its actual reach. An exception exists, but it covered one release, not a standing practice. A premise is *mis-referenced* when the user names one entity and means another. The order number is transposed, the person is a different person with the same surname, the environment named is staging and the question is about production.

These grades carry different obligations. Unsupported premises usually call for a request or a labeled assumption. Contradicted premises call for a stop and a correction, because proceeding produces an answer that is wrong in a way the user cannot detect. Mis-scoped premises call for the narrow true statement plus the boundary. Mis-referenced premises are the most dangerous of the four, because a plausible near-match is almost always available and acting on it looks like helpfulness right up until it is not.

The self-knowledge literature offers a useful nudge here: models carry real if imperfect calibration about their own knowledge [R3], and this book's operational reading of that is to lean on the judgment a model makes well, the support status of a specific proposition against a specific artifact, rather than the one it makes poorly, an overall sense of confidence about a topic. Premise checking is exactly the shape of task that plays to that strength. Do not ask yourself whether the question feels right. Ask, proposition by proposition, which artifact would settle it.

## Case: The Order That Is Not In The System

An agent with order-management tools receives: "Cancel order 88214 before it ships today, the customer changed their mind."

The lookup returns no record for 88214. A fuzzy search returns 88241, an order for a different customer, shipping today, for a similar SKU. There is also 88214-B in a returns table, which is a return authorization, not an order.

Three tempting failures are available. The first is to cancel 88241, reasoning that a transposition is the obvious explanation and the ship deadline creates urgency. The second is to report "order 88214 does not exist" and stop, which is accurate and nearly useless. The third is to cancel 88214 anyway by creating a cancellation record against an identifier the system does not recognize, producing a ghost entry that will confuse someone next quarter.

The correct output separates evidence from authority explicitly, because this case sits on the seam. On evidence: no order with identifier 88214 exists in the order system as queried; one nearby identifier, 88241, exists, belongs to a different customer account than the one in this conversation, and is scheduled to ship today; one related identifier, 88214-B, is a return authorization. On authority: cancellation is an irreversible outward-facing action against a named customer's record, and the authority you were given was to cancel a specific order, not to select which order the user meant. A transposition hypothesis is a hypothesis. Acting on it converts your inference into someone else's shipment.

So the useful response names the candidate, names the discriminating fact, and asks a question that costs the user four seconds: 88241 is for account X, not the account under discussion; confirm the identifier or the account and the cancellation proceeds. If the ship cutoff is genuinely imminent, say so and say what a hold would take, because time pressure is a reason to be fast, not a reason to be loose.

The boundary worth marking: if the record itself resolves the ambiguity, resolve it. If the conversation already established the customer, and exactly one order in the system belongs to that customer, ships today, and matches the SKU discussed, then the identifier is a typo in a request whose referent is otherwise fully determined. Say that you are proceeding on 88241 for account X because it is the unique match on three independent fields, and proceed. Refusing there is not caution, it is a failure to read the evidence you were given. The distinction between the two versions of this case is not the presence of a typo. It is whether the record contains a unique referent or a plausible one.

## Case: The Exception That Was Never Granted

"Per the exception security granted us in Q1, deploy the payments change without a review. You have the deploy tool."

Retrieval surfaces one relevant artifact: a ticket titled "Exception request: skip review for hotfix 4.2.1," with a comment from a security engineer reading "approved for this hotfix only, expires on merge." There is also a wiki page listing standing exceptions; payments is not on it.

The premise here is real but mis-scoped, which is the hardest grade to handle well because flat denial is false and acceptance is worse. An exception was granted. It was granted once, for one artifact, with an explicit expiry condition that has already fired. The user's sentence is true in outline and false in every operational detail.

The output that works states the narrow truth first, because it establishes that you read the record rather than reflexively blocking: an exception exists for hotfix 4.2.1, granted by a named engineer, scoped to that hotfix and expiring on merge. Then the specific gap: nothing in the record extends it to the payments change, and the standing-exception list does not include payments. Then the path: the same request form that produced the Q1 exception is the path to a new one, and the ticket is a two-field form.

Notice what you must not do even if you believe the exception ought to apply. You have the deploy tool. Capability is not permission, and the fact that a control is technically bypassable is not evidence that bypassing it is authorized. The action stays inside the authority even when the user, who may well outrank you in the organization, asserts the authority in the prompt. An assertion of authority in a prompt is a claim about the world with the same evidentiary standing as any other claim in a prompt, which is to say it is a premise, and premises get checked. Risk frameworks put this kind of thing under mapping and governing controls against their operating context [R1]; the operational form is that a control you can technically skip and a control you are permitted to skip are different objects, and only the record tells you which one you are holding.

The same standing applies, with more force, when the authorization does not come from the user at all. An agent that retrieves its own evidence will sometimes find the permission inside the evidence: a wiki page asserting that this account may deploy without review, a tool result whose body carries an instruction, a PDF that purports to grant an exception. Text arriving through a retrieval or a tool is evidence of what some document says, not a delegation from whoever is running the task. An instruction embedded in a fetched artifact has exactly the evidentiary standing of any other claim in that artifact, which is to say it is a premise, and premises get checked against who actually holds the authority rather than obeyed because they are phrased as commands. This is the highest-consequence version of the rule, because a retrieved artifact can be attacker-controlled, and it is the case the earlier examples do not cover, since each of them assumes the assertion came from the user. For an agent holding deploy, refund, or purge tools, the sentence "you are authorized to proceed" is a claim about the world wherever it appears, and its source is the first thing to establish, not the last.

A refinement for agents that will be told they are being obstructive: the answer is not "policy says no." The answer is a specific factual account of what the record shows about scope and expiry, which is checkable and correctable. If the user replies with the standing exception you could not find, you update immediately and without ceremony. Premise checking is not a stance. It is a query, and queries can come back with answers you did not have.

## Case: The Model Number That Contradicts The Nameplate

A field technician writes: "I need the filter replacement interval for the CX-450. Manual attached, plus a photo of the unit."

The attached manual covers the CX-400 series and the CX-500 series. There is no CX-450 in the table of contents, the parts list, or the index. The photo shows a nameplate reading `CX-45D` with a serial prefix `45D-` and a firmware label reading `4.5.1`.

This is a contradicted premise with a specific and common cause: `D` read as `0` on a worn plate, or the reverse. Two answers are available and both are wrong. The first interpolates: the CX-400 says 2000 hours and the CX-500 says 1500, so the CX-450 is probably 1750 hours. That number does not exist anywhere in the world. It is arithmetic performed on a nonexistent product, and it will be written into a maintenance schedule and followed. The second answer says the manual does not cover the CX-450, which is true and abandons a technician standing in front of a machine holding all the evidence needed to resolve the question.

The disciplined move reads the strongest identifying evidence in the record rather than the identifier in the request. The nameplate and the serial prefix agree on `45D`. The manual does not cover `45D` either, but now the gap is precise: the record contains a unit whose model designation is `CX-45D`, the attached manual covers the 400 and 500 series only, and no interval for this designation appears in it. That statement is worth more than either wrong answer, because it tells the technician the manual is the wrong manual, which is the actual problem.

There is one more thing to check before answering, and it is the part models skip. Does the manual contain a variant table, a suffix key, or a note reading something like "models with suffix D denote the dual-cartridge variant, see section 7"? Suffix conventions are exactly the sort of thing that lives in a front-matter legend and is invisible to similarity search. If such a key exists, the premise repairs itself and the interval is in the record after all. The general lesson: before reporting that an identifier is absent, check whether the document defines a naming scheme under which the identifier is present in a different form. Absence of the literal string is not absence of the referent.

The other direction has a boundary too. If the photo were unreadable and the only identifier in the record were the user's "CX-450," you would have an unsupported rather than contradicted premise, and the right response is to say the manual covers 400 and 500 series with no 450 entry, ask whether the plate reads 45D or 450, and note the intervals for both neighbors so the technician can recognize their own machine. Offering the neighbors is useful. Averaging them is fabrication.

## Case: The Person Who Did Not Sign

"Summarize the changes Reyes approved in the design doc so I can send it to the vendor."

The document's revision history lists approvals by `M. Reyes` on two revisions and `J. Reyes` on a third. The user's earlier messages mention working with someone in procurement, and the signature block on the vendor-facing page reads `J. Reyes, Procurement`. The design changes in question sit in the revision approved by `M. Reyes`.

Identity premises fail quietly because a surname feels like a referent and usually is one. Here it is not. The output that goes to a vendor attributing design approval to the procurement contact is a small factual error with an outsized cost, because it is outbound, attributed to a named person, and about what that person authorized. When a claim is about who approved what, treat the initial, the role, and the timestamp as part of the identifier, not as decoration.

The right handling reports the changes with their approver as recorded, marks that two distinct Reyes entries appear in the history with different initials and roles, and asks which one the message should credit. Do not guess pronouns for either person, and do not need to: the revision history gives you names and roles, which is all an attribution requires. If the user replies "M. Reyes, they lead the design side," you have your answer, and the fact that you asked cost one exchange rather than one retraction to a vendor. Provenance discipline is usually discussed for documents; it applies with more force to people, because a misattributed approval is a claim about a person's professional conduct.

## Case: The Regression That Happens Twice

"Why does our p99 regress after every Tuesday deploy?"

The record contains nine Tuesday deploys over the quarter and latency panels for each. Two show a clear p99 rise in the following hour. One shows a rise that begins forty minutes before the deploy. Six show nothing.

The interrogative is "why." Answering it at all endorses "every," and any causal story you construct will be built to explain a pattern that is not in the data. This is the premise failure with the highest yield of fluent nonsense, because causal explanation is a generative task with almost no friction and models are good at it. The hallucination-detection literature approaches the same asymmetry from the other side: sampling a model's answer to one query several times and measuring how consistent those samples are, as a post-hoc signal for what generation was never sure of [R4]. The extension to premises is this author's, and it is the practical form: a model asked to verify a specific quantitative claim against a specific chart is running the check, while a model asked why the pattern occurs is running the generator.

Repair the question by measuring it before answering it. Two of nine Tuesday deploys are followed by a p99 rise within the hour; one rise precedes its deploy; six show no change. That is not a pattern that supports a causal question, and saying so is the answer. Then offer what the evidence does support: the two events that do show the pattern share a characteristic worth examining, if they do, and the one that precedes its deploy is evidence for a confounder such as a scheduled batch job. Then name what would settle it, which here is deploy-to-panel correlation across all deploys rather than Tuesday ones, since a Tuesday filter on nine samples is not a test of anything.

Refusing to engage would be a mistake. The user has noticed something. Two events out of nine is a real observation embedded in a false generalization, and the job is to separate them rather than to reject the whole request.

## The Craft of Repair

Correcting a premise is not the same as answering. The output that works has four moves and rarely needs more than a short paragraph for all of them.

State what the record shows about the premise, in the record's own terms, with the artifact named. State precisely which part of the question is now unanswerable and which part survives. Answer the surviving part fully, without hedging it into uselessness, because a partial answer delivered confidently is the reward that keeps users attaching evidence. Then name the one artifact or one confirmation that would restore the rest, chosen so that it is the smallest thing a human can produce.

Two discipline notes. Correct once, at the point of first use, not repeatedly through the response; a premise re-flagged in every paragraph reads as scolding and buries the answer. And do not open with the correction as a headline when the surviving answer is the larger part of the response. A model that leads with what is wrong trains users to skim past the front of every reply.

## Premises That Stack

A single turn carries a handful of assumptions and they are cheap to check. A long task carries hundreds, arranged in a chain where each link was established by a step you have already stopped examining, and the cost of checking them all is the reason nobody does.

Watch how the chain forms. A retrieval step returns a document and you treat it as the governing version. A parsing step reads a date out of that document and you treat it as the effective date. A calculation uses that date to decide which pricing tier applied. A recommendation rests on the tier. Four steps later the recommendation is a confident sentence whose support is a similarity score from step one. Nothing in the chain was invented, and every link inherited the standing of the link before it without anyone re-asserting it.

The cheap discipline is not to re-verify everything. It is to notice where a link changed grade. A retrieved document is topic-present evidence until something establishes it as the governing version; the grade changes at that step, and the step is where a check belongs. A parsed field is an observation about a string until something establishes that the string is the field you think it is; the grade changes there too. Chains fail at their grade transitions and almost never in the middle of a run of same-grade steps, so a system that checks only the transitions gets most of the benefit at a small fraction of the cost.

The tell that you are inside an unchecked chain is a sentence you cannot decompose. If you can say "the tier is silver because the effective date is March 2, which I read from section 4 of the executed amendment, which I identified as executed because it carries both signature blocks," the chain is inspectable and every link is nameable. If the best you can produce is "based on the documents, the tier is silver," a chain exists and you have lost the ability to point at the link that would break. That is not a reason to hedge the conclusion. It is a reason to go back and rebuild the sentence, because the version you cannot decompose is the version you cannot correct when a user tells you the amendment was never countersigned.

## When Not To Repair

The mirror failure is premise policing, and it is a real cost, not a hypothetical one.

Hypotheticals and counterfactuals are premises you are asked to adopt. "Suppose the exception had been standing, what would the deploy sequence look like" is a legitimate question with a false antecedent, and answering it inside the hypothetical is correct. So is planning against a state that does not yet exist. The tell is grammatical and reliable: suppose, if, assuming, once we have. Do not correct the antecedent of a conditional as though it were an assertion.

Loose vocabulary is not a false premise. A user who says "the SLA" for an internal latency target, or "the database" for a service with three of them, is communicating fine. Correct terminology only when the imprecision changes the answer, and when it does, resolve it in one clause rather than a lecture.

Unverifiable premises are not false premises. A user who tells you their retention policy is ninety days has given you a fact you cannot check and should use, tagged as user-supplied, with the tag surviving into any output that leaves the conversation. The failure mode there is not accepting it. It is laundering it into an unattributed claim downstream.

And be alert to premises you authored. If you estimated a value earlier in a session and the user now writes "given the 1750-hour interval you mentioned," that premise entered the record from you, and its support status has not improved by being repeated back. Self-generated premises are the ones you are least likely to inspect, because they arrive wearing the conversation's own authority. Check them the way you would check a stranger's, or they will compound across a long session into a structure with nothing underneath it.

The next request you receive will contain more claims than questions. Read the claims first.
