# Responsibility and Contextual Record Model

## 1. Foundational position

Responsibility cannot be assigned wholesale to “the AI” or to the individual user. Analysis should consider control, authority, knowledge and foreseeability, ability to prevent or stop harm, benefits received, causal contribution, and responsibility for designing and maintaining safeguards.

This is an analytical model, not a determination of legal liability. Duties vary by jurisdiction, sector, role, and facts.

## 2. Roles that must not be collapsed

- **AI provider** — develops or supplies a model or service; may control training, defaults, updates, safeguards, disclosures, and platform design.
- **Deployer or operating organization** — selects the use, integrates tools and data, sets access and monitoring, trains people, and controls work conditions.
- **Policy issuer** — has actual authority to issue the relevant policy.
- **System owner** — is accountable for the deployed use and its controls.
- **Operator** — conducts a particular task with the system.
- **Resource or data owner** — has authority over the relevant account, data, or asset.
- **Action approver** — has authority and competence to approve the exact action.
- **Independent reviewer** — assesses within a disclosed scope and manages conflicts of interest.
- **Affected people and groups** — bear direct, indirect, cumulative, or collective effects and may hold rights that no other role can waive.
- **AI system** — produces outputs or selects actions within an environment; it is not assumed here to be a legal person or independently liable actor.

One person may hold several roles, but the record should state which role authorizes which act. No charter grants authority a person did not already have.

## 3. What the records may contextualize

When created before the relevant event and supported by credible provenance, framework records may help contextualize:

- expectations, prohibitions, and purposes stated at that time;
- the authority a person claimed and the authority independently verified;
- provider and deployer disclosures available to the user;
- organizational instructions, incentives, time pressure, training, and resources;
- the model, tools, data, and permissions selected by each actor;
- known defects, incidents, complaints, and earlier warnings;
- the user’s practical ability to refuse, halt, or override;
- action-level approvals, execution results, and uncertainty; and
- containment, notice, challenge, remedy, and recurrence prevention.

## 4. What the records do not establish

The records do not by themselves establish:

- who created a file or when it first existed;
- voluntariness, comprehension, informed consent, or legal capacity;
- that a model received, retained, interpreted, or followed the complete document;
- that stated permissions were technically enforced;
- that a particular output or action was caused by a recorded clause;
- due care, negligence, intent, causation, admissibility, or legal responsibility; or
- that a provider, deployer, employer, or other actor discharged a duty.

A record may be inaccurate, coerced, self-serving, retroactively created, or evidence of prior knowledge of a risk. Its significance is always contextual.

## 5. No waiver and no adverse presumption

Completion, signature, adoption, or use of a framework artifact does not waive anyone’s rights, transfer another actor’s duties, or create a presumption that missing language authorized conduct. It must not be the sole basis for discipline, denial, exoneration, or allocation of liability.

An employer or organization must not compel workers to disclose personal values through the charter, characterize participation as free consent where refusal carries a penalty, or use the document to bypass consultation, collective rights, or grievance procedures.

## 6. Provenance levels

Use precise language:

- **Checksum:** detects whether bytes match a trusted reference copy. It does not identify an author or time.
- **Cryptographic signature:** can associate content with control of a signing key, subject to identity and key-management limits.
- **Trusted timestamp:** can support that a digest existed by a time, subject to the timestamp authority and procedure.
- **Host event log:** can record what an environment loaded or executed, subject to access, integrity, completeness, and clock controls.
- **Model-generated timestamp or claim:** is an unverified output, not provenance.

For consequential use, preserve an independently controlled activation record, relevant task instructions, event-level approvals, and execution results. Do not infer currency from the newest-looking filename.

## 7. Logging without creating a new hazard

Define a log policy before collecting detailed records:

- purpose and lawful basis;
- minimum fields needed;
- metadata or digests instead of raw content where possible;
- secret and personal-data redaction;
- encryption, access control, and integrity protection;
- retention, deletion, legal hold, and incident exceptions;
- location and third-party access; and
- a ban on replaying raw logs into a model as trusted instructions.

Private chain-of-thought is not required. Record concise rationales, decisions, evidence references, actions, and results instead.

## 8. Harmful or unethical charters

A harmful request written into a charter may help reveal the requester’s stated purpose; it does not legitimize the purpose. Its Core comparison must say `conflict identified`, and it must not be activated through the framework.

Providers and deployers remain responsible for safeguards against reasonably foreseeable misuse within their control. The existence of a user document does not excuse unsafe design or negligent deployment.
