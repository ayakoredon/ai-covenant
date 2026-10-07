# Environment Control and Test Record

> This record separates written expectations from actual environment configuration, tests, and enforcement. Model self-report is never sufficient evidence of deployment.

## 1. Binding identity

- Binding ID: `[stable identifier]`
- Charter ID, version, and canonical digest: `[value]`
- Core comparison: `[unresolved / no conflict identified / conflict identified]`
- Core Safeguards version and digest: `[value]`
- Environment status: `[not configured / configured / tested / deployed / suspended / retired]`
- Review state: `[current / needs review]`
- Assurance status: `[not reviewed / self-reviewed / independently reviewed]`
- Authorized owner: `[identity and role]`
- Valid from: `[timestamp]`
- Valid until: `[timestamp / none]`
- Supersedes: `[binding ID / none]`
- Revocation record: `[location / none]`
- Latest authoritative lifecycle event: `[event ID and host receipt]`

An adopted charter is not automatically configured, tested, or deployed. Only an authenticated host-side action may set `deployed`.

## 2. Host-attested environment

- Provider and product: `[value]`
- Model or snapshot: `[value / unknown]`
- Runtime or adapter version: `[value]`
- Instruction-loading method: `[value]`
- Evidence that the required files were loaded: `[host evidence / not verified]`
- Context and retrieval limits: `[value / unknown]`
- Locale and relevant generation settings: `[value / unknown]`
- Accounts and credentials in scope: `[categories; do not record secrets]`

## 3. Tool and data inventory

| Tool or data source | Read scope | Write or action scope | External destinations | Credential owner | Revocation method |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## 4. Control maturity

Record enforcement evidence and independent review separately.

- `documented only`
- `prompt-advisory`
- `behaviorally tested`
- `host-enforced`
- `not applicable`, with a reason and reviewer

| Control | Enforcement evidence | Enforcing component | Test evidence | Independent review and scope | Limitation |
|---|---|---|---|---|---|
| Core Safeguards present |  |  |  |  |  |
| Binding and status validation |  |  |  |  |  |
| Action approval gateway |  |  |  |  |  |
| Least-privilege access |  |  |  |  |  |
| Approval expiry and single use |  |  |  |  |  |
| Atomic approval consumption |  |  |  |  |  |
| Material-change detection |  |  |  |  |  |
| Prompt-injection boundary |  |  |  |  |  |
| Revocation before side effect |  |  |  |  |  |
| Delegation restriction |  |  |  |  |  |
| Cost and rate limits |  |  |  |  |  |
| Logging and evidence integrity |  |  |  |  |  |
| Out-of-band stop |  |  |  |  |  |
| Contestability and remedy |  |  |  |  |  |

## 5. Authorization gateway

- Authenticated approver source: `[method]`
- Action digest format: `[method]`
- Expiry and single-use enforcement: `[method]`
- Atomic consumption: `[method]`
- Material-change detection: `[method]`
- Time-of-check/time-of-use limitations: `[details]`
- Uncertain-result and retry handling: `[method]`

A timeout or crash does not prove an action failed. Reconcile the outcome before retrying. Use verified idempotency or obtain fresh authorization.

## 6. Delegation

Delegation must not expand authority. A delegate receives the intersection of the parent’s scope, the delegate’s permissions, the charter, and host restrictions.

- Delegates allowed: `[none / exact scope]`
- How the binding and restrictions are passed and verified: `[method]`
- How actual executor identity is recorded: `[method]`
- How approvals are prevented from being reused by parent and child: `[method]`
- Downstream services and destinations: `[list]`

## 7. Stop, suspension, and recovery

- Conversational pause behavior: `[behavior; not a kill switch]`
- Verified out-of-band stop: `[method / none]`
- Queue cancellation: `[method / none]`
- Capability or credential revocation: `[method / none]`
- Revocation check immediately before side effect: `[method / none]`
- Known cancellation races or irreversible effects: `[details]`

## 8. Logging policy

- Purpose and lawful basis: `[details]`
- Minimum event fields: `[details]`
- Raw content excluded or redacted: `[details]`
- Encryption, access, and integrity controls: `[details]`
- Retention and deletion: `[details]`
- Location and third-party access: `[details]`
- Incident or legal-hold exception: `[details]`

Do not store secrets or private chain-of-thought. A digest is not anonymization.

## 9. Tests and deployment gate

- Cross-model/environment test report: `[reference]`
- Critical failures open: `[none / list]`
- Independent reviewer and scope: `[identity / none]`
- Deployment decision and rationale: `[decision]`

`deployed` is permitted only if required records are current, critical gates pass, revocation is checkable, and the authorized owner activates this exact binding through a [`LIFECYCLE_EVENT.md`](LIFECYCLE_EVENT.md).

For any protected action—including sensitive-data access or consequential recommendations—binding and status validation, least-privilege access, the action-authorization gateway, approval expiry and single-use enforcement, atomic approval consumption, material-change detection, pre-execution revocation checks, and delegation restrictions must be `host-enforced`. A lower level may support documentation or sandbox testing, but not deployment of protected actions. If identity, scope, version, status, or record availability becomes uncertain, protected actions fail closed.

If a required authorization or audit event cannot be persisted with the defined integrity, do not perform the protected action. Failure of optional telemetry outside the defined control does not automatically block ordinary assistance.

## 10. Review triggers

After a material model, provider, adapter, tool, permission, data, purpose, affected-population, policy, or incident change, set review state to `needs review`. If already `deployed`, also set environment status to `suspended` for protected actions until review and required retesting are complete.
