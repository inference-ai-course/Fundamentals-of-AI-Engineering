# Theme Example: Customer Feedback / Support Ticket Analyzer

Use this if your CSV contains feedback, support tickets, survey comments, or customer messages.

## Helpful Input Columns

```text
ticket_id,created_at,customer_segment,channel,message,rating
```

Your dataset does not need exactly these names, but it should include at least one text column.

## Prompt Adaptation

Ask the LLM to focus on:

- recurring themes
- urgent issues
- customer risks
- recommended support or product actions

## Theme-Specific `llm_interpretation` Fields

You may include:

```json
{
  "themes": [],
  "urgent_issues": [],
  "customer_risks": []
}
```

Keep the main `report.json` top-level schema unchanged.
