from openai import OpenAI

client = OpenAI(
    base_url="https://extra-8000-8000-1774475741172722.cluster3.service-inference.ai/v1",
    api_key="AAAAC3NzaC1lZDI1NTE5AAAAIMt7uZpUkd/VDwtg5peTe59BB62edS5fRrGn7N5Sc3ur"
)

response = client.chat.completions.create(
    model="Jackrong/Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)
