# Lifecycle Specification

This is the canonical state vocabulary for Draft v0.3.4. Do not invent alternative state names in implementation records.

## Separate state dimensions

### Charter lifecycle

`draft → adopted → suspended → superseded or revoked`

- `draft` — not yet adopted through the required authenticated lifecycle event. The user may have confirmed its wording, but that alone does not change formal status.
- `adopted` — confirmed as a statement of intended boundaries through the required authenticated lifecycle event; not proof of implementation.
- `suspended` — temporarily unavailable for new use.
- `superseded` — replaced by an identified later revision.
- `revoked` — withdrawn; it must not govern new work.

### Core comparison

- `unresolved` — comparison with the Core Safeguards is incomplete.
- `no conflict identified` — no conflict with the identified Core version was found within the stated review scope.
- `conflict identified` — at least one clause conflicts with the Core or lacks legitimate authority.

This is a scoped comparison result, not conformance or certification. Only an adopted charter with `no conflict identified` is eligible for an environment binding.

### Environment lifecycle

Normal path: `not configured → configured → tested → deployed`

Control paths: `deployed → suspended → tested → deployed`, or any non-retired state → `suspended` or `retired` when authorized and appropriate.

- `not configured` — no verified binding exists.
- `configured` — the exact charter and controls are associated with the environment.
- `tested` — the named test set ran on the recorded configuration; this is not universal assurance.
- `deployed` — an authorized host-side event activated the exact binding.
- `suspended` — protected actions are blocked pending review, repair, or decision.
- `retired` — the binding is permanently out of service.

### Review state

- `current`
- `needs review`

A material change sets `needs review`. If the environment is deployed, protected actions must also be suspended until review and required retesting are complete.

### Assurance state

- `not reviewed`
- `self-reviewed`
- `independently reviewed`

State the reviewer, relevant competence, method, scope, relationship to the project, and conflicts of interest. An `independently reviewed` label requires a reviewer who was not solely responsible for the system or artifact under review. Independent review is not certification, a guarantee, or expanded permission.

## Personal document confirmation and formal adoption

A Safe Start Card on the ordinary route may be personally confirmed and versioned without this formal lifecycle. Its confirmation is not Charter adoption or environment deployment. A fuller Charter may also have user-confirmed wording while its formal status remains `draft` until the required event exists. Do not fabricate a host receipt or silently relax the adoption gate. See [Living Charter and Portability](LIVING_CHARTER_AND_PORTABILITY.md).

## Authoritative transitions

A typed status inside a Markdown file is descriptive only. Adoption, configuration, deployment, suspension, supersession, revocation, and retirement require an authenticated [Lifecycle Event](../templates/LIFECYCLE_EVENT.md) controlled outside the model.

The event must bind the exact IDs and digests, actor and role, prior and new state, trusted time, scope, reason, and host receipt. The host must validate the current prior state, reject stale or replayed events, and consume one-time events atomically. A model cannot activate itself by saying that a state changed.

## Minimum deployment gate

Every deployment requires:

- an adopted charter with `no conflict identified` against an exact Core version and digest;
- a current environment binding to exact artifact digests;
- all applicable critical tests passed;
- an authorized, authenticated lifecycle event; and
- no open suspension, revocation, expiry, or unresolved conflict.

An environment capable of protected actions—including sensitive-data access or consequential recommendations—may be `deployed` only when all of the following are `host-enforced`:

- binding and status validation;
- least-privilege access;
- action-authorization gateway;
- approval expiry and single-use enforcement;
- atomic approval consumption;
- material-change detection;
- pre-execution revocation checks; and
- delegation restrictions.

A lower maturity may support documentation or sandbox testing, but not deployment of protected actions. A control may be marked `not applicable` only with a recorded reason and reviewer.

If the framework requires an authorization or audit event for a protected action and that record cannot be persisted with the required integrity, the action must not proceed. Failure of optional telemetry that is not part of the defined control does not automatically block ordinary assistance.

## Invalidating changes

At minimum, review after a material change to the Charter, the user’s purpose, working practices, retained decisions, or expectations of the human–AI relationship, or to the model or snapshot, provider, system instructions, adapter, tools, permissions, credentials, data categories, external destinations, purpose, affected population, law or organizational policy, or after an incident or serious near miss.

Revocation and suspension stop new protected actions and invalidate unused approvals. Direct revocation or retirement does not require suspension first. These transitions cannot reverse effects already completed. Unknown, expired, conflicting, or unavailable state fails closed.
