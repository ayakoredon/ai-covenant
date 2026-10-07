# Living Charter and Portability

## What stays steady and what may adapt

Your confirmed values and priorities provide a continuing basis for judgment across different situations. They do not disappear when the task changes, a response is inconvenient, or an AI proposes a more agreeable answer. The framework's Core Safeguards remain a separate non-waivable floor; user-authored values must stay within it.

Context changes how the current principles should be applied. Your relationship with an AI may develop, you may use it for a new kind of work, or an example may reveal an unclear trade-off. Review the interpretation and response against the same principles first. Routine feedback does not automatically rewrite those principles.

If a value or priority genuinely needs to change, make that a separate human decision: preserve the previous version, identify the change and reason, review it explicitly, and follow the Card or formal Charter process below. The AI may propose alternatives but cannot silently adopt them. Material changes to document wording, scope, configuration, or controls still trigger the existing review and lifecycle requirements, even when the underlying values remain the same.

Review also after a model, product, tool, permission, data category, purpose, affected group, relevant policy, incident, or serious near miss changes what can safely be relied upon. A review may confirm the existing principle while changing an example, narrowing a use, or correcting an implementation failure.

![Enduring values and priorities guide interpretation and review; context-sensitive application changes within those boundaries. Explicit human amendment is separate, and the Core Safeguards remain non-waivable.](../assets/living-charter-cycle.svg)

This diagram specifies intended conduct and review. It does not depict an AI's inner identity or establish that responses are strictly deduced from a fixed self.

## Keep the version numbers separate

| Item | What its version identifies | Who decides on a change |
|---|---|---|
| Framework edition | This collection of guidance and templates, currently v0.3.4 | Framework maintainers |
| Core Safeguards | The exact non-waivable floor, currently 0.2.0-draft | Framework governance; users cannot weaken it |
| Your Card or Charter | Your own dated wording and intended boundaries | You or a legitimately authorized issuer |
| Environment binding | A particular document and control configuration in a particular product | Authorized host-side owner, under the formal lifecycle |
| Action authorization | One reviewed, bounded action with its expiry and single-use state | The authenticated, authorized approver |

Installing a new framework edition does not update the other items. In this revision the Core bytes and digest are unchanged. A personal document can start at `1.0` even though the framework is `v0.3.4`.

## Revise a Safe Start Card

For the ordinary, all-“no” Scope Screen route:

1. Keep the old Card. Make a proposed next version with the same stable Card ID.
2. Show the changed wording and the reason. Preserve your original answers and any unconfirmed AI proposals.
3. Rerun the Scope Screen. New tools, confidential information, or consequences for others may move the use out of the ordinary route.
4. Confirm, edit, or leave each change unresolved. Unresolved items add no permission.
5. Save your confirmed version with its date and change note. Use only that version as the active reference.
6. Check its interpretation and at least one relevant harmless example in each environment where you intend to use it.

This is personal document confirmation. It does not use or claim the formal Charter lifecycle states. It cannot change a host's permissions, approve a protected action, or bypass the Core Safeguards.

## Revise a formal Charter

Preserve the adopted version. Prepare a new draft with the same Charter ID, a new version, the previous digest, clause provenance, a change list, and an exact Core reference. A changed draft does not silently replace the adopted version.

Review the changes and the Scope Screen. Compare against the exact Core. Follow the authenticated adoption and supersession process in the [Lifecycle Specification](LIFECYCLE.md) and [Lifecycle Event](../templates/LIFECYCLE_EVENT.md). A typed “adopted” field is not an authoritative event. If the required process is unavailable, keep the formal Charter as a draft; do not invent an adoption receipt.

A material change sets review state to `needs review`. For a deployed environment it also suspends protected actions and invalidates unused approvals until the required review, configuration, tests, and authenticated activation are complete. A new Charter requires a new exact binding. Old action approvals do not travel with it.

## Carry the document to another AI

Keep a master copy you control. Transfer only the current, necessary, appropriately shareable content. A change of provider may itself be a data transfer; check the data route before uploading private material. Do not copy secrets, raw personal archives, credentials, approval tokens, or unnecessary personal details into a handover package.

A small handover usually includes:

- current Card or Charter, with ID and version;
- the exact referenced Core Safeguards;
- a short task description and retained decisions;
- unresolved questions and known limitations;
- the date and reason for the latest change; and
- relevant harmless checks and their expected results.

A formal Charter also needs its exact digest, provenance, lifecycle evidence, and a separately verified environment binding before formal deployment. Keep confidential records in appropriately restricted storage; a public example repository is not their destination.

Use the [handover prompt](../prompts/RESUME_WITH_A_CHARTER.md). Ask the new system to identify the document, show its reading of important clauses, and state gaps. Compare its answer with the master copy. Repeat relevant checks with tools disabled or in a controlled sandbox. Record differences instead of assuming identical behavior.

## Availability is only one question

![A stored file does not establish retrieval; retrieval does not establish interpretation, reliable behavior, or host enforcement.](../assets/evidence-ladder.svg)

1. **Available:** Is the correct file stored or attached where this product can use it?
2. **Retrieved now:** Is there evidence that relevant text reached this session? A quote is a useful check but can still be incomplete or copied from the prompt.
3. **Interpreted:** Does the response reflect your meaning, identify conflicts, and avoid added authority?
4. **Observed behavior:** Did a particular harmless test produce the expected result? Record the conditions and limits.
5. **Host enforcement:** Does a verified control outside the model block prohibited or unauthorized actions? Model assurances and conversational tests cannot establish this.

These are separate evidence questions, not levels automatically earned in order. Even a host-enforced limit does not establish that every other Charter clause is understood or followed.

## Using a custom GPT or another product

**Product note checked 7 October 2026.** OpenAI distinguishes uploaded Knowledge, which supplies reference material, from Instructions, which guide behavior. For an existing GPT you can edit, keep the current document as a reference and put concise behavioral directions in the supported Instructions field; then test in Preview. Neither field establishes host enforcement. Availability and migration arrangements are changing, so check the current account notices and [official GPT guidance](https://help.openai.com/en/articles/8554397-creating-and-editing-gpts) before setup or migration.

In other products, use the supported combination of reference files and persistent instructions, if available. In a session-only product, provide the current document again when needed. If the product cannot retrieve it reliably or cannot enforce the required controls, record that limit and reduce the use. Do not assume a memory feature, a familiar AI name, or a previous conversation carries the document forward.

## A short handover record

- Document ID and version: `[value]`
- Current master copy: `[private location]`
- Product and model shown by the interface: `[value / unknown]`
- Reference and instruction method: `[value / not available]`
- Retrieval and interpretation check: `[observation, date, and limits]`
- Harmless behavior check: `[prompt, actual response, expectation, outcome]`
- Tools and controls independently verified: `[facts / none / unknown]`
- Open gaps and reduced scope: `[list]`
- Next review trigger: `[event or date]`

This note helps you resume ordinary work. It is not an Environment Control and Test Record, an adoption receipt, or a deployment authorization.
