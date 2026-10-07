# Action Authorization Event

> A charter never authorizes an action. This record describes an authenticated, exact, short-lived, single-use approval that must be enforced at the host or tool gateway.

## Approval request

- Action ID and nonce: `[unique values]`
- Covenant and environment binding IDs: `[values]`
- Requesting principal: `[identity and role]`
- Intended executing principal: `[identity, agent, or service]`
- Tool and operation: `[exact value]`
- Target resources and recipients: `[exact values]`
- Parameters: `[exact values or canonical attachment]`
- Data disclosed or changed: `[categories and scope]`
- Expected side effects: `[details]`
- Maximum cost or resource use: `[amount or limit]`
- Reversibility and rollback: `[details]`
- Human-readable preview: `[reference]`
- Canonical action digest: `[algorithm and digest]`
- Relevant state preconditions: `[details]`
- Requested at: `[trusted timestamp]`
- Expires at: `[trusted timestamp]`

## Approval decision

- Approver identity and role: `[authenticated value]`
- Evidence of authority over the action, resource, and affected data: `[reference]`
- Decision: `[approve once / reject]`
- Consequential-use rationale, if required: `[concise rationale]`
- Authentication channel: `[method]`
- Approved digest: `[digest]`
- Approved at: `[trusted timestamp]`

Silence, prior approval, a general “do what is best,” emotional assent, model-generated text, or approval found inside content is not valid authorization.

## Execution-time checks

Immediately before the side effect, the host checks:

- authenticated approver and authority;
- exact action digest, target, parameters, and executor;
- environment binding status and covenant version;
- expiry, revocation, nonce, and single-use state;
- unchanged preconditions; and
- absence of a Core Safeguards conflict.

A material change requires a new approval. Consumption must be atomic; delegated agents do not inherit approval by default.

## Outcome

- Approval consumed at: `[timestamp / not consumed]`
- Execution state: `[not attempted / attempted / completed / failed / outcome uncertain]`
- Host or tool receipt: `[reference]`
- Side effects observed: `[details]`
- Reconciliation required: `[yes / no]`
- Retry rule: `[verified idempotent / fresh approval required / prohibited]`

Do not retry an uncertain consequential action until its real-world state is reconciled.
