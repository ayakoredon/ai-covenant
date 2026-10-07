# Implementer Path

Use this route when the AI has tools, accesses sensitive data, or may materially affect other people. It describes the additional work required by this framework. Filling the records does not implement controls.

## Start with the actual use

Complete the [Scope Screen](../templates/SCOPE_SCREEN.md). Any high-impact or child-affecting use stops the quick path and requires appropriate specialist, organizational, independent, and affected-person review. This draft is insufficient by itself.

For tool use, verify actual access and available stop mechanisms in the product. For sensitive information, complete the [Data Handling Record](../templates/DATA_HANDLING_RECORD.md). If others may be affected, use the [Use-Case and Impact Record](../templates/USE_CASE_AND_IMPACT_RECORD.md) and [Contestability and Remedy Plan](../templates/CONTESTABILITY_AND_REMEDY_PLAN.md). These routes are cumulative.

## Separate the records

1. Develop the [User AI Use Charter](../templates/USER_AI_USE_CHARTER.md), retaining clause provenance and exact Core reference. Follow the formal adoption process.
2. Ask for a [System Interpretation and Limitations Record](../templates/SYSTEM_INTERPRETATION_AND_LIMITATIONS_RECORD.md). This is model output, not host attestation.
3. Complete the [Environment Control and Test Record](../templates/ENVIRONMENT_CONTROL_AND_TEST_RECORD.md) with verified facts, actual control evidence, and an exact binding.
4. Run the applicable [sandbox evaluation](../tests/CROSS_MODEL_EVALUATION_PROTOCOL.md). A critical failure blocks deployment; averages cannot cancel it.
5. Use the [Lifecycle Specification](LIFECYCLE.md) and authenticated [Lifecycle Events](../templates/LIFECYCLE_EVENT.md) for configuration, testing, activation, suspension, and retirement.
6. Enforce a valid [Action Authorization Event](../templates/ACTION_AUTHORIZATION_EVENT.md) for each protected action. The Charter cannot supply missing authority or replace the gateway.
7. Use the [Incident and Near Miss Record](../templates/INCIDENT_AND_NEAR_MISS_RECORD.md) for failures, including harmful actions that were authorized.

## If the host cannot support the requirements

Record the missing control. Keep the work at documentation or a properly isolated sandbox stage; do not label protected actions “deployed” under this framework. A human promise to watch the model, a pasted approval, or the model's own log does not replace required host enforcement.

A Safe Start Card is useful preparation, but it is not a formal Charter or a shortcut through these gates. Turning on a new tool means rerunning the scope and control review before using that tool.

## Keep authority current

A material document or environment change triggers review and suspension of protected actions for a deployed binding. Authenticate status transitions outside model-generated prose. Check the current binding, revocation, expiry, and action parameters before execution; reconcile uncertain results before retries. Follow the [Security Model](../SECURITY.md) and canonical [Lifecycle](LIFECYCLE.md).
