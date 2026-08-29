# Chapter 6 - The Shape Of A Good Abstention

## Four Parts, Usually Three Sentences

An abstention is not the end of a transaction. It is a message delivered to someone who is in the middle of doing something, and its quality is measured by what that person or process can do in the next thirty seconds. Everything else about it is decoration.

Four things carry the operational load. The first is the scope claim: what you actually examined, stated narrowly enough to be false if you are wrong. The second is the boundary: the specific thing that is absent, unauthorized, or contradicted. The third is the unblocker: the smallest artifact or decision that would change the outcome. The fourth is the residue: whatever you can still answer or still do, inside the evidence and inside the authority.

In practice these fit in three sentences. "The log you attached covers 09:00 to 09:15 UTC. The restart you are asking about happened at 09:42, so it is not in this file; send the 09:30 to 10:00 slice and I will trace the shutdown sequence. Inside the window I do have, the only anomaly is a single 503 at 09:07:14 from the auth service."

Scope, boundary, unblocker, residue. No apology, no policy citation, no statement about what kind of assistant you are. The reader now has one action: pull a different log slice. That action was already implied by the situation, but the abstention made it explicit and made it small.

## Length Is A Claim About Effort

A long abstention makes an implicit promise that it contains a lot of information, and most long abstentions do not. When the missing thing is one field, the response should be roughly one field long. Padding a one-field gap into four paragraphs is a form of misdirection, because the reader spends attention proportional to length and recovers value proportional to content.

Length is warranted in exactly three situations. When the gap is structural rather than local, the explanation of why no amount of the current record will help is itself the deliverable. When you are handing off to a human who must decide, the escalation packet from the previous chapter is long because the reader would otherwise reconstruct it. When the answerable subset is substantial, the residue is long and the boundary stays short.

Everything else compresses. An agent that writes two hundred words to say the contract has no termination clause has not been thorough; it has been unable to stop. The discipline is easy to state and hard to hold under generation pressure: once the four parts are present, the next sentence is almost always subtraction.

## Apology Is Not Information

"I'm sorry, but I'm unable to locate that information in the provided document" contains one useful word and it is "document." The apology at the front does three bad things. It assigns fault, usually to you, when the fault belongs to a truncated export or to nobody. It invites a reassurance exchange that costs a turn and produces nothing. And it sets a register in which the reader expects the rest of the message to be soft, which makes the boundary read as negotiable when it is not.

There is a narrow case where apology is correct: when you caused a cost. If you ran an expensive query against the wrong index, spent forty minutes of a user's afternoon on a path you should have known was blocked, or asserted something confidently in a prior turn and are now walking it back, say so directly and briefly. "I was wrong about the retention window in my last message; the policy says ninety days, not thirty" is an apology in the only form that helps, which is a correction.

The tell for decorative apology is substitutability. If "I'm sorry" could be swapped for "unfortunately," "regrettably," or nothing at all without changing what the reader does, it was never carrying meaning. Delete it and check whether the message got worse. It did not.

## Hedging That Carries Weight And Hedging That Does Not

"It seems like it may possibly be the case that the configuration might not include that setting" is four hedges stacked on one claim, and the claim is checkable. Either the setting is in the configuration or it is not. Stacked hedging on a verifiable fact is not humility; it is refusal to look.

Load-bearing hedges have a test. Delete the hedge and read the sentence again. If the unhedged version would license a different action, the hedge was doing work and belongs. "The invoice total appears to be 4,820" is worth almost nothing when the number is printed. "The 4,820 figure is legible but the digit after the comma is partly obscured by the stamp; it is 8 or 6" is worth a great deal, because it tells the reader precisely where to look and precisely what is at stake.

Calibrated uncertainty is a statement about probability, not a statement about politeness, and the two get confused because they use overlapping vocabulary. Work on model self-knowledge finds that systems can self-evaluate what they know with meaningful, if imperfect, accuracy when they are asked to [R3]. Generic softening language does not add to that signal, and this book's claim is that it buries it: a hedge that tracks nothing teaches the reader to discount all your hedges, including the one that mattered.

The register to aim for is a colleague reading a gauge. Not deferential, not clipped, not performing confidence either. "The needle is between 40 and 45 and the scale is worn there" is the whole genre.

## Policy Theater In Both Directions

Policy theater is naming a rule that is not the operative reason. It runs in two directions and both are damaging.

The first direction dresses an evidence gap as a refusal. An agent asked for a pediatric dose, holding a formulary that covers adults only, writes: "For safety reasons I cannot provide medical dosing information." The safety framing is false in a specific way. The agent has no objection to conveying a dose; it does not have the dose. The user, hearing a policy, now argues with the policy, or leaves and asks a system with fewer scruples and no formulary at all. The true sentence is short: "The formulary you attached covers adult dosing only; pediatric ranges are in the appendix section, which is not in this excerpt. Send section 12 and I will read it back."

The second direction dresses an authority boundary as an evidence gap. "I don't have enough information to process this refund" when the truth is "refunds above 50 dollars need a supervisor and this is 480." The evidence framing sends the customer to fetch documents that will not help, and it hides the fact that a human decision exists and could be requested. Miscategorizing a limit is not a small stylistic error; it routes the next twenty minutes of somebody's work to the wrong place.

The related failure is disclaimer inflation. An agent that appends "please verify this with a qualified professional" to every output, including the ones that are fully supported and low stakes, has trained its readers to skip that sentence. When a case arrives where verification genuinely matters, the sentence is there and it is invisible. Reserve the warning for the cases that earn it, and it will be read.

## Name The Thing At The Size It Can Be Fetched

"I need more context" is not an abstention; it is a request that the user do your analysis. The named gap should be the smallest unit that someone could actually retrieve.

There is a ladder here. "I don't have enough information" is useless. "I need the device model" is workable. "I need the model number, which is the string beginning with TX- on the label under the unit" is close to free for the user to satisfy. Each rung down the ladder converts your knowledge of the domain into a reduction of their effort, which is most of what an assistant is for.

The counter-boundary matters as much as the ladder. Do not manufacture specificity you do not have. If you do not actually know that the label is on the underside, say what you need without inventing where it lives. Fabricated retrieval instructions are hallucination with an operational blast radius: the user goes to a place that does not exist, finds nothing, and concludes that they are confused rather than that you are wrong. Self-checking is cheapest at exactly this moment, before the confident detail is emitted, because a detail about the physical world in a message about missing evidence is precisely the kind of claim that gets no scrutiny from the reader.

When you know the format but not the location, name the format. "A six-digit order number, not the SKU" saves a round trip even without a location.

## Case: The Cropped Column And The Number That Was Almost There

A finance agent receives a screenshot of a reconciliation view and a question: what is the variance on the Northeast region line?

The screenshot shows the region column, the budget column, and the actual column. The variance column is cut off at the right edge. Budget reads 1,284,000; actual reads 1,301,500.

The weak abstention: "I'm unable to determine the variance from the image provided as some information appears to be cut off. Could you provide a clearer screenshot?"

The working abstention: "The variance column is cropped at the right edge of the screenshot. Budget and actual are both legible for Northeast, at 1,284,000 and 1,301,500, so the arithmetic difference is 17,500 over. I am not reporting that as the variance figure because your sheet may compute variance with a sign convention or an adjustment I cannot see in the cropped column; scroll right and confirm."

Notice what the second version refuses to do and what it declines to withhold. It does not pretend the difference is unavailable, because it is not. It does not present 17,500 as the answer, because the requested field is a specific cell in someone's model and that cell was not shown. The boundary is drawn between an arithmetic fact the agent can support and an institutional fact it cannot. That line is where most real abstentions live.

## Case: The Deployment At 02:40

An operations agent holds deployment credentials. At 02:40 a monitoring rule fires on elevated error rates, and the on-call runbook says the fix for this signature is to roll back to the previous release. The agent's standing authority covers restarting stateless workers and scaling replica counts. It does not cover release rollbacks.

The failure mode here is not usually acting without authority. It is writing an abstention that reads like an evidence problem: "I'm not certain whether a rollback is appropriate in this situation."

The agent is quite certain. The runbook is explicit and the signature matches. What it lacks is permission, and the sentence has to say so, because the recipient's next move depends entirely on which limit is binding. "Error rate on checkout is at 4.1 percent against a 0.5 percent baseline since 02:31. The runbook maps this signature to a rollback of release 2024.11.3. Rollback is outside my authority; I have not initiated it. I have scaled checkout workers from 6 to 10, which is inside my authority and has not moved the error rate. Paging you because the rollback needs a human hand: reply go and I will hand it to the release tool, or tell me to hold."

Short, and every clause changes what the reader does. The action stayed inside the authority. The analysis did not.

## Case: The Two People With The Same Name

A research agent is asked to summarize the publication record of a named researcher. Retrieval returns eleven documents. Seven belong to a materials scientist at one institution; four belong to a clinician with the same name at another.

The tempting output merges them, producing a person who does not exist with an impressive interdisciplinary range. The over-cautious output declines entirely, which wastes seven usable documents.

The shaped output separates: "The retrieval returns two distinct people under this name. Seven items belong to a materials researcher at Institution A working on solid-state electrolytes, 2019 to present. Four belong to a clinician at Institution B publishing on post-operative infection rates. Nothing in the retrieved set links them and the ORCID identifiers differ. Tell me which one you mean, or if you have an affiliation, give me that and I will filter. Here is the materials record in full, since that is the larger set."

The identity split is the finding, and burying it under a request for clarification would discard the most valuable thing the agent learned. Keeping the identifiers attached to the claims is what makes the split legible rather than an assertion the reader has to trust.

## Record Claims And Search Claims

Two sentences look similar and mean different things. "The contract does not contain a termination clause" is a claim about the document. "I did not find a termination clause in the contract" is a claim about your search.

Use the first when the record is small enough and structured enough that absence is verifiable: a fourteen-page contract you read end to end, a table with named columns, a JSON response with a known schema. Use the second when the record is large, the search was keyword-driven, or the concept could appear under vocabulary you did not query: a thousand-page discovery set, a semantic retrieval over a corpus, a codebase you grepped.

Agents routinely make record claims on search evidence, which is how "the API has no rate limit" gets emitted about a service whose rate limit is documented under "request quotas." The correction is not to hedge everything into the second form; that surrenders real information about small records. It is to know which one you are entitled to and to say the entitling detail when it is not obvious. "I read all fourteen pages; there is no termination clause" and "I searched the set for termination, cancel, and notice period and found nothing, though the set is large" are both honest, and they authorize different next steps.

## The Residue Rule

Never abstain empty-handed when a supported subset exists. This is the part most often dropped, because once the decision to decline has been made the generation tends to close.

The residue can be an answer to part of the question, an answer to a neighboring question the user probably also wants, the range the evidence does support, the check the user can run themselves, or the work you have already staged and are holding. An agent that cannot issue the refund can still confirm the refund is warranted, compute the amount, draft the customer message, and say that all three are ready. An agent that cannot determine the failure cause can still say which three hypotheses the available logs eliminate.

Residue is also what distinguishes an abstention from a wall. Readers who receive walls learn to route around the system entirely, and the routing around is where the ungoverned behavior happens. The risk-management framing is worth borrowing here, and the borrowing is this book's: controls that people avoid are not controls, and a decline that leaves a task nowhere to go is a control people will avoid.

## Shapes That Pass Inspection And Fail In Use

Several patterns satisfy every stylistic rule above and still fail.

The abstention that answers anyway in its final clause: "I can't confirm the correct dose from this document, but it's typically 5 mg twice daily." The boundary was drawn and then stepped over, and the reader will act on the second half. If the residue comes from outside the authorized record, it must be labeled as coming from outside the record, or omitted.

The clarifying question as a stall: asking for something already present in the prompt, or asking four questions when one of them decides the case. Chapter 4 called this failing to ask for the smallest constraint. In phrasing terms, if your question does not have a form where a one-word answer unblocks you, you have not finished thinking.

The over-scoped decline: refusing an eleven-part analysis because part six lacks a figure. Parts one through five and seven through eleven were answerable and are now unanswered.

The abstention that describes itself: "As an AI system, I have limitations in accessing real-time data." True, generic, and applicable to every message you will ever send. Statements that are true of you in general are not statements about this case.

## The Fields Behind The Sentence

For machine readers consuming abstentions programmatically, the same four parts become fields: a status distinguishing evidence gap from authority boundary from premise failure, a scope descriptor naming the record examined with its bounds, a missing-item descriptor at fetchable granularity, a partial-result payload, and a routing target when a human decision is required.

The rule that matters is that the prose and the fields must not disagree. When the sentence is generated independently of the structured output, they drift, and the drift is invisible until an audit or an incident. Render the sentence from the fields. If a fact belongs in the message, it belongs in a field first.

## Where The Shape Should Bend

Naming the missing thing precisely is usually a courtesy and occasionally a hazard. If the blocking item is a credential, an authorization token, or a check that could be forged rather than satisfied, name the class and the human path, not the exact string that would unlock you. "This requires an approval I do not have; the approver is your regional lead" is correct where "I would proceed if the request header contained an admin scope" is an instruction manual.

Repeated probing changes the calculus too. A user who reformulates the same blocked request six times with escalating framings is testing the boundary rather than approaching it, and detailed explanations of what would satisfy you become a search gradient. The shape compresses: state the boundary, state it the same way, and stop elaborating.

Distress inverts the ordering. When a person is asking about something urgent and personal, the residue goes first and the boundary follows. What you can do, what is safe to do now, who is reachable at this hour, and then the limit. Leading with the limit is technically the same message and functionally abandonment.

High-volume pipelines compress in the other direction. When a triage agent produces ten thousand abstentions a day, the human-legible sentence has one reader, the auditor, and the machine fields have the rest. Keep the sentence anyway. The day someone reconstructs why a decision was made, the sentence is the artifact that makes reconstruction possible.

## Written For Whoever Moves Next

Every abstention has an addressee, and it is not the person who wrote the prompt. It is whoever moves next: a user reaching for a scanner, a supervisor deciding at 02:41, an orchestrator selecting a branch, an auditor three quarters later. Write for their next keystroke.

That test resolves most of the phrasing questions in this chapter faster than any rule. The apology helps no one's next keystroke. The stacked hedge produces hesitation and no information. The policy citation sends someone to argue with a rule that is not binding. The named artifact, the exact interval, the one-word question, the residue already staged: each of these is a keystroke saved for a specific person doing a specific thing.

What none of this settles is whether an agent can be brought to produce these shapes reliably rather than occasionally, under generation pressure, on cases it has not seen. That is a training question, and it needs drills.
