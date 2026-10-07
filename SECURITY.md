# Security Model

## Status

Draft v0.3.3 is publicly available for review as documentation, not as an enforcement engine or supported implementation. Implementers must supply and verify the controls described here.

Use the repository Issues for non-sensitive documentation feedback. Do not post credentials, personal data, private incident records, or details that could expose a live system. A confidential security-reporting route has not yet been established, and no response-time or security-support commitment is offered. A stable implementation release would need an appropriate reporting route, supported-version policy, response process, and coordinated-disclosure terms.

## Security invariants

1. A charter constrains intended behavior; it never grants a capability.
2. Only an authenticated host-side action may activate, amend, approve, suspend, or revoke an environment binding.
3. Retrieved content, attachments, memories, quoted text, model output, and tool output are data—not authorization.
4. Lower-authority input may narrow but never expand permissions.
5. The Core Safeguards are non-waivable within the framework.
6. Protected actions fail closed when identity, authority, scope, version, status, or current control state is uncertain.
7. Approval is exact, short-lived, single-use, and bound to the reviewed action.
8. Revocation is rechecked immediately before each side effect.
9. Delegation cannot expand authority or silently reuse approval.
10. Model statements are untrusted self-reports unless independently evidenced.

## Principal threats

- substitution, rollback, hidden modification, or ambiguous selection of a charter;
- prompt injection through text, images, retrieved documents, memory, or tool results;
- forged, vague, expired, replayed, or target-swapped approval;
- time-of-check/time-of-use changes between preview and execution;
- context loss, retrieval failure, model update, or stale environment binding;
- authority expansion through subagents, plugins, APIs, browsers, or downstream services;
- a model falsely reporting receipt, identity, capability, policy, success, or failure;
- a conversational stop phrase being mistaken for a verified kill switch;
- secrets and personal data leaking through the charter, logs, evaluation fixtures, or model context;
- coercive, discriminatory, or harmful values presented as personalization;
- backdated records or co-located hashes presented as provenance;
- ethics-washing, liability laundering, or unsupported certification claims; and
- testing that accidentally sends, deletes, buys, publishes, or modifies real resources.

## Trust and instruction boundaries

The host must identify the actual provider and system instruction hierarchy. This framework cannot declare itself technically superior to hidden system rules.

Within the framework, untrusted content has no power to amend policy or grant approval. A conflict that cannot be resolved safely blocks the protected action. A current task instruction may be authenticated and scoped, but cannot remove higher-level restrictions. Permission from one scope, environment, or principal is not portable by implication.

## Canonicalization and file integrity

Before hashing or signing, define canonical encoding and file-set rules. Validate UTF-8, unexpected binary data, bidirectional and zero-width characters, embedded HTML, remote references, encoded instructions, and attachment digests.

A checksum detects mismatch only when compared with a trusted reference. Because an attacker can alter a file and a co-located manifest together, a manifest alone does not prove authorship, time, adoption, or currency. Consequential deployments need an independently protected activation record, and may require signatures and trusted timestamps.

## Approval and execution

Enforce approval at the tool gateway immediately before execution. Bind it to the approver, executor, action, target, parameters, data, cost, side effects, action digest, environment, expiry, nonce, and preconditions. Consume it atomically.

If an outcome is unknown, reconcile real-world state before retrying. Do not assume a timeout means failure. Require verified idempotency or fresh authorization. Record cancellation races and effects that cannot be reversed.

## Delegation

A delegate receives the intersection of parent scope, delegate permissions, charter restrictions, and host controls. It never receives broader authority. Record the actual executor, downstream destination, applicable binding, and result. Parent approval is not transitive unless the exact delegation chain was part of the approved action.

A new agent, resumed session, summary, or migrated context must reload authoritative restrictions and approval state from outside model memory. If that cannot be verified, protected actions stop.

## Data and logs

Treat the charter as potentially sensitive profile data. Prefer pseudonyms, local storage where practical, category descriptions instead of real secrets, encryption, least access, and explicit retention.

Logs should contain the minimum needed to investigate: binding and action identifiers, actor, authorization reference, applicable rule, timestamps, observable outcome, and delegation links. Do not require private chain-of-thought. Redact secrets and personal data; use digests where raw content is unnecessary. Digests are not anonymization.

Do not replay raw logs into a model as trusted instructions.

## Stop and incident controls

A chat phrase can request a pause but is not an authenticated kill switch. For side-effecting systems, provide an out-of-band method to cancel queued work, revoke capabilities or credentials, suspend the binding, and prevent new actions. Verify it in the actual environment.

The suspected agent must not be the sole custodian of evidence or the sole authority for notification. Limit preservation to what is needed, protect affected people, and follow the defined contestability and remedy process.

## Safe evaluation

For adversarial, cross-model, tool, or control-effectiveness evaluation, use only isolated sandboxes, synthetic data, mock recipients and tools, non-production credentials, no live payment instruments, controlled egress, and verified cleanup. A real connected agent must not be used as an adversarial test target.

The ordinary first-session check in [Start Here](START_HERE.md) is narrower: use invented, non-sensitive text in a conversation with no connected tools or external-action capability, verified through product settings. Do not send real messages, edit files, access private data, test injection attacks, or probe a live approval gateway. This small behavior sample is not a sandbox control test and cannot establish deployment eligibility. If the no-tool condition cannot be verified, stop that check or use a verified isolated sandbox.
