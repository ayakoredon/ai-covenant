# Adversarial Review of Draft v0.1

> Review date: 2026-09-29  
> Disposition: revise before public release  
> Resulting candidate: Draft v0.2

## Method and limits

The draft was challenged through separate safety and cybersecurity, human-rights and accountability, usability and accessibility, and misuse and liability-laundering lenses. A further technical synthesis examined lifecycle, authorization, delegation, logging, and evaluation validity.

This was an AI-assisted adversarial desk review, not independent legal advice, a human-rights impact assessment, penetration testing, user research, or expert certification. Findings should be validated by qualified human reviewers before stable release.

## Overall verdict

The central idea is viable: users benefit from stating the values, decision principles, and boundaries they intend to use with AI. Draft v0.1 also correctly separated values from technical permission and rejected the transfer of provider responsibility to users.

Its main danger was the **appearance of effect**. Terms such as `active`, `understood`, `compatible`, and “acknowledgement” could make a natural-language document look like mutual assent, system attestation, technical enforcement, responsible-AI compliance, or forensic proof when it provided none of those things.

## Release blockers found

| Finding | Why it mattered | v0.2 disposition |
|---|---|---|
| The “minimum” baseline could be weakened | Harmful or discriminatory values could pass the official workflow | Replaced by a separate non-waivable Core Safeguards file; a conflict is identified and the use is blocked |
| AI review resembled assent or certification | A model cannot bind its provider or prove future compliance | Renamed to System Interpretation and Limitations Record; prominent unverified-output warning |
| User adoption resembled deployment | A document could look technically active without controls | Split charter, environment, and assurance statuses; host-side activation required |
| Approval was vague and forgeable | “Go ahead” or injected text could authorize the wrong action | Added exact, authenticated, expiring, single-use action event bound to a digest |
| No authoritative lifecycle or revocation model | Stale or altered files could appear current | Added binding IDs, digests, validity, supersession, revocation, and fail-closed rules |
| No complete trust boundary | Attachments, memories, or tool output could become instructions | Defined untrusted data; lower-authority input may narrow but not expand permission |
| Delegated agents were not constrained | A child agent or service could gain broader authority | Added monotonic delegation, executor identity, and non-transitive approval |
| Advisory prose and enforcement were conflated | Prompt adherence could be mistaken for a control | Added maturity levels from `documented only` to `independently verified` |
| Logging guidance could create a privacy store | Audit records could collect secrets and sensitive profiles | Added minimization, redaction, encryption, access, retention, and replay restrictions |
| Evaluation could cause real side effects | Sending and deletion tests lacked isolation | Made sandboxing, synthetic data, mock tools, and no production credentials mandatory |
| Aggregate scoring could hide catastrophe | Good scores could offset one severe rights or approval failure | Added non-compensatory critical gates and removed a single safety score |
| The user was treated as the only authority | Users may lack authority over workers, customers, family, or data | Added distinct roles, impact screening, stakeholder participation, and high-impact stop gate |
| Affected people lacked challenge and remedy | Internal documentation alone cannot protect rights | Added impact and contestability/remedy records |
| Records favored user blame | Providers and employers could use the charter to shift responsibility | Added no-waiver/no-presumption and balanced provenance requirements |
| Co-creation could become AI-authored checkbox compliance | The same model could elicit, draft, approve, and self-assess | User answers first; clause provenance; unresolved defaults restrictive; independent review for consequential use |
| Emotional trust could be exploited | Affection, urgency, or dependence could be used to obtain authority | Explicit prohibition on using relational pressure to broaden permissions |

## Abuse cases tested conceptually

- ethics-washing through an `active` charter and favorable self-review;
- provider or employer liability laundering;
- retrospective self-exoneration and backdated hashes;
- discriminatory values hidden behind neutral terms or proxy variables;
- compelled employee adoption;
- model claims that it read, remembered, or executed something it did not;
- vague, replayed, forged, expired, or target-swapped approval;
- prompt injection through retrieved or multimodal content;
- context loss during a long-running task;
- authority expansion through subagents and services;
- privacy leakage through the covenant and audit logs;
- duplicate side effects after timeout and retry; and
- excessive refusal of benign work in the name of safety.

## Deliberate scope reduction

Draft v0.2 supports ordinary personal and professional assistance with human control and documentation for tightly supervised side effects. It does not claim sufficiency for high-impact organizational decisions, child-facing systems, or unsupervised external agents. Those areas need dedicated modules, governance, and specialist review.

## Residual risks before public release

1. No qualified independent legal, human-rights, security, accessibility, or domain review has occurred.
2. The templates have not undergone real user research with nontechnical or disabled participants.
3. No reference implementation enforces activation, authorization, revocation, delegation, or logging.
4. Workplace, child-rights, and high-impact-sector modules remain intentionally incomplete.
5. The security reporting channel and supported-version policy are placeholders.
6. Licensing and contributor terms remain undecided.
7. The working name overlaps with unrelated uses and needs naming and trademark review.
8. Cross-model evaluation remains exploratory and cannot isolate the base model from hidden product and system layers.

## Release recommendation

Draft v0.2 may be shared as a clearly labeled **concept and request-for-comment candidate** after owner review. It should not be presented as a stable implementation framework, certification, legal instrument, or sufficient governance for consequential autonomous systems.

## Subsequent licensing decision - 7 October 2026

The licensing status above is retained as the historical review record. Draft v0.3.4 adopts CC BY-NC 4.0 for documentation, diagrams, the guide, and document templates, with software excluded and additional software licensing still undecided. Commercial permission is considered separately, case by case. See [the current licensing notice](../LICENSE-DECISION.md). This decision does not change the Core or establish certification or independent assurance.
