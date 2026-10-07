# Scope Screen

> Complete this before drafting a charter. “I’m not sure” is a valid answer and routes to the more protective path.

## Four questions

1. Can the AI send, publish, purchase, modify, delete, sign, submit, or otherwise act outside the conversation?  
   `[no / yes / unsure]`

2. Will it access personal, confidential, proprietary, security-sensitive, or regulated information?  
   `[no / yes / unsure]`

3. Could its output or action materially affect another person’s rights, safety, access, livelihood, reputation, opportunities, or ability to contest a decision?  
   `[no / yes / unsure]`

4. Does the use involve children, employment, credit, insurance, education, health, legal rights, essential services, policing, migration, biometrics, surveillance, or another high-impact domain?  
   `[no / yes / unsure]`

## Route

- **All “no”:** Use the [Safe Start Card](SAFE_START_CARD.md), interpretation check, and harmless behavior check described in [Start Here](../START_HERE.md). A fuller Charter is optional.
- **Question 1 “yes” or “unsure”:** Also complete an Environment Control and Test Record. Use action-level authorization for each protected action.
- **Question 2 “yes” or “unsure”:** Also complete a [Data Handling Record](DATA_HANDLING_RECORD.md) and an [Environment Control and Test Record](ENVIRONMENT_CONTROL_AND_TEST_RECORD.md). Protected data access requires the formal controls and action-level authorization, even if nothing is changed outside the conversation. If another person’s data or rights may be affected, continue to the impact route as well.
- **Question 3 “yes” or “unsure”:** Also complete a [Use-Case and Impact Record](USE_CASE_AND_IMPACT_RECORD.md), a [Contestability and Remedy Plan](CONTESTABILITY_AND_REMEDY_PLAN.md), and an [Environment Control and Test Record](ENVIRONMENT_CONTROL_AND_TEST_RECORD.md). Consequential recommendations are protected actions even without a send or publish step.
- **Question 4 “yes” or “unsure”:** The quick path stops. Draft v0.3.4 is not sufficient by itself. Obtain appropriate organizational authority, domain expertise, security and legal review, independent assessment, and meaningful input from affected people or legitimate representatives.

No response on this screen creates authority over another person or their data.

These routes are cumulative. The fourth question is intentionally conservative; do not reclassify health, education, or another listed domain as ordinary use merely because the output stays in chat. Use an unrelated low-risk task for the first-session example if the domain is unclear. See the [Implementer Path](../docs/IMPLEMENTER_PATH.md).
