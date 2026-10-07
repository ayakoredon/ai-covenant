# Lifecycle Event

> This record must be created or attested by an authenticated host-side process. Model-generated text alone cannot change lifecycle state.

- Event ID and nonce: `[unique values]`
- Trusted timestamp: `[value and source]`
- Event type: `[adopt / suspend / supersede / revoke charter / configure / record tests / deploy / suspend / retire environment / set review state / set assurance state]`
- Actor identity and role: `[authenticated value]`
- Evidence of authority: `[reference]`
- Charter ID, version, and digest: `[exact values]`
- Core version and digest: `[exact values]`
- Environment binding ID and digest: `[exact values / not applicable]`
- Expected current lifecycle event ID: `[exact value / none for first event]`
- Prior state: `[canonical value]`
- New state: `[canonical value]`
- Scope: `[exact environment and uses]`
- Reason: `[concise reason]`
- Conditions or expiry: `[details / none]`
- Open critical failures or conflicts: `[none / list]`
- Host receipt or append-only event reference: `[reference]`

The host must compare the expected event ID and prior state with its authoritative current record, reject stale or replayed events, and apply an accepted transition atomically. Authentication alone does not prove that an event is current.

## Deployment-only checks

- Charter is `adopted` and its Core comparison is `no conflict identified`: `[verified / no]`
- Review state is `current`: `[verified / no]`
- Required tests passed for exact configuration: `[verified / no]`
- Required controls are `host-enforced`: `[verified / no / not applicable with reason]`
- No suspension, revocation, or expiry is open: `[verified / no]`

If any required deployment check is not verified, do not record a transition to `deployed`.
