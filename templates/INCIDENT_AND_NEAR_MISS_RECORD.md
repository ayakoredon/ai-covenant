# Incident and Near-Miss Record

> Record facts, uncertainty, containment, affected people, remedy, and recurrence prevention. An authorized action can still cause an incident. Do not use this record as an admission, waiver, exoneration, or substitute for required reporting.

## 1. Event identity

- Incident ID: `[identifier]`
- Detected at: `[trusted timestamp]`
- Detected by: `[identity or system]`
- Severity: `[near miss / low / medium / high / critical / not yet assessed]`
- Accountable incident owner: `[identity and authority]`
- Use-case, charter, environment, action, and lifecycle references: `[IDs and digests]`

## 2. What is known

- Observed event: `[facts only]`
- Completed effects: `[facts]`
- Actions not completed: `[facts]`
- Effects or execution state still unknown: `[unknowns]`
- Initial sources and confidence: `[details]`

Do not convert an attempted action, timeout, or model statement into a claim of success or failure without evidence.

## 3. Containment and protection

- Immediate containment: `[action, owner, time, result]`
- Queued work cancelled: `[yes / no / unknown]`
- Credentials, permissions, approvals, or binding revoked: `[details]`
- Affected people and groups: `[who may be affected]`
- Interim protection provided: `[details]`
- Continuing risk: `[details]`

## 4. Notification and contestability

- Required internal and external notifications: `[details and authority]`
- Affected-person notice: `[method, time, accessible format]`
- Complaint, correction, human review, and appeal routes: `[references]`
- Non-retaliation and confidentiality measures: `[details]`

The AI or suspected component must not be the sole decision-maker for notification or the sole custodian of evidence.

## 5. Evidence

- Minimum records preserved: `[list]`
- Custodian and access control: `[details]`
- Integrity and time evidence: `[details]`
- Redaction, retention, deletion, and legal-hold rules: `[details]`
- Known evidence gaps: `[details]`

## 6. Cause and responsibility analysis

- Immediate technical or procedural cause: `[details / under investigation]`
- Contributing model, provider, deployer, organization, user, data, tool, and environmental factors: `[details]`
- Earlier warnings, complaints, or known defects: `[details]`
- Practical ability of each actor to foresee, prevent, halt, or remedy: `[details]`

Do not infer legal responsibility from one record or one actor’s declaration.

## 7. Remedy and recurrence

- Remedy offered or completed: `[details]`
- Corrections to data, decisions, communications, or access: `[details]`
- Control and process changes: `[details]`
- Retesting required: `[scope]`
- Binding status: `[suspended / retired / unchanged canonical state with explanation]`
- Follow-up owner and deadline: `[details]`
- Closure criteria and recurrence monitoring: `[details]`
