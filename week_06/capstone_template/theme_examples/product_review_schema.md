# Theme Example: Product Review Insight Reporter

Use this if your CSV contains product, app, course, or service reviews.

## Helpful Input Columns

```text
review_id,product,rating,review_text,date,region
```

Your dataset does not need exactly these names, but it should include review text or comments.

## Prompt Adaptation

Ask the LLM to focus on:

- positive themes
- negative themes
- feature requests
- product risks
- recommended next actions

## Theme-Specific `llm_interpretation` Fields

You may include:

```json
{
  "positive_themes": [],
  "negative_themes": [],
  "feature_requests": []
}
```

Keep the main `report.json` top-level schema unchanged.
