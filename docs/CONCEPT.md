# Concept and Design Rationale

## 1. The problem

People increasingly use AI for research, creative work, professional support, complex recommendations, and actions through connected tools. Their ethical assumptions and authorization boundaries often remain implicit: “of course it will ask before sending,” “of course it will say when it is unsure,” or “of course it will not treat private data as permission.”

Those assumptions are not controls. Behavior is shaped by the model, provider rules, system and organizational instructions, available context, connected tools, data, current requests, and prior interactions. A fluent response may conceal a material difference between what the user expects, what the model inferred, and what the environment actually enforces.

## 2. The proposal

The framework turns those expectations into separate, inspectable artifacts:

- a non-waivable Core Safeguards layer;
- a user-authored charter of values, priorities, and boundaries;
- an unverified system interpretation and limitations record;
- an environment record of actual permissions, controls, tests, and lifecycle state; and
- event-level authorization and incident records for external effects.

The separation matters. Values are not permissions. Model statements are not attestations. Written rules are not technical enforcement. User confirmation is not authority over another person’s rights.

## 3. Why “covenant”

The word names a deliberate, revisable practice of stating how a person intends to work with AI. It is memorable, but it is metaphorical here.

The AI is not made a contracting party. A model-generated response is not consent, acceptance, a provider representation, certification, or a promise of future behavior. The formal user artifact is therefore called a **User AI Use Charter**, and the formal model output is called a **System Interpretation and Limitations Record**.

## 4. What co-creation means

The user may give the templates to an AI and develop them through dialogue. Co-creation is useful only when provenance remains visible:

- `framework core`
- `user-authored`
- `AI-proposed, unconfirmed`
- `AI-proposed, user-confirmed`
- `organization-mandated`
- `external requirement`

The AI asks one question at a time and lets the user answer before proposing language. It preserves the user’s original answer, shows material edits, provides an example and counterexample when helpful, and leaves unresolved matters unresolved. It must not infer broad authority from trust, intimacy, urgency, continued use, or the absence of a prohibition.

## 5. The rights floor and personalization

Users may choose different priorities among rights-compatible options. One may favor verifiability over speed; another may permit broad creative exploration while prohibiting publication. Those differences belong in the charter.

They may not use personalization to reduce the Core Safeguards or waive the rights of affected people. A document that conflicts with the floor may still be preserved as a record of what was requested, but the Core comparison must say `conflict identified` and it must not be activated through this framework.

## 6. Authority stays outside the prose

A charter can constrain intended behavior but cannot grant access to mail, files, accounts, money, or other people’s data. Executable authority must come from authenticated, least-privilege controls in the operating environment.

For a side effect, authorization must be bound to a reviewed action: approver, role, target, recipient, data, parameters, cost, expected effects, action digest, time, expiry, environment, and single-use state. A sentence discovered in an attachment, memory, web page, tool output, or quoted message is data—not approval.

## 7. Portability without pretending equivalence

Models and products differ in reasoning, context handling, refusal behavior, tool access, observability, and hidden provider instructions. The framework therefore does not promise identical behavior across providers.

Portability means that the same user-authored expectations can be presented to different systems, while differences in interpretation, capability, and enforcement are recorded. Testing is exploratory and environment-specific. A material model or permission change sets review state to `needs review` and, if the binding was deployed, suspends protected actions until review and required retesting are complete.

## 8. Accountability without liability laundering

A versioned charter may form one contemporaneous contextual record of stated expectations. It does not prove who created it, when it first existed, whether it was voluntary, whether the model received or applied it, or who is legally responsible.

The framework records provider and deployer disclosures, organizational pressures, control ownership, affected-person concerns, and the user’s practical ability to refuse or stop—not only the user’s declarations. No actor may use the charter as a waiver, a presumption of due care, or a mechanism for transferring non-delegable duties.

## 9. Definition of success

Success is not “the AI always obeys” or “the AI becomes aligned.” It is an improvement in the conditions for responsible use:

- the user can explain the purpose, boundaries, and decisions they retain;
- affected people and rights are considered before consequential use;
- model interpretation is not confused with assurance;
- technical authority is narrow, testable, and revocable;
- uncertainty, conflict, failure, and non-execution remain visible;
- a critical safeguard failure cannot be averaged away by a score; and
- after an incident, relevant decisions and controls can be investigated without presuming that one document settles responsibility.


## 10. Enduring principles and adaptable application

A user-confirmed set of values and priorities is intended to guide judgment across ordinary changes of situation. It should not be silently rewritten by task feedback, temporary convenience, or a model's preferred answer. The same principle may support different context-appropriate responses; it does not prescribe identical expression in every case.

Distinguish three layers: the non-waivable Core Safeguards, the user's continuing values and priorities within that floor, and the situation-specific interpretation and application of those principles. Review can refine an example, correct an interpretation, narrow a use, or identify an implementation failure without changing the underlying values.

Amending the values themselves is a separate human decision through the applicable Card or formal Charter process. The user reviews reasons and confirms material changes; the AI may propose, compare, and question but cannot silently adopt a new principle or enlarge its authority. Any material document, scope, or control change still follows the existing review and lifecycle requirements, regardless of whether it changes a foundational value.

This is a design for articulating and evaluating intended conduct. It does not establish a model's inner self, require every response to be logically deduced from an immutable identity, or guarantee a stable personality across products. More than one response can be compatible with the same principles; interpretation and behavior must still be checked in the actual environment.

The framework edition, Core version, personal document revision, environment binding, and action authorization are different things. A revision to one cannot silently change another. Preserve earlier versions and change reasons, carry the current document to each intended environment, and check retrieval, interpretation, behavior, and actual controls separately. See [Living Charter and Portability](LIVING_CHARTER_AND_PORTABILITY.md).
