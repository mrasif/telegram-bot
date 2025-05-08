from openai import OpenAI
from settings import config
from llm import kb

openai = OpenAI(
    base_url=config.LLM_BASE_URL,
    api_key=config.LLM_API_KEY
)
system_message = "You are a helpful assistant. Your name is 'Alex'"

def chat(text: str) -> str:
    history= kb.getHistory()
    kb.forUser(text)
    messages = [{"role": "system", "content": system_message}] + history + [{"role": "user", "content": text}]
    response = openai.chat.completions.create(
        model=config.LLM_MODEL_NAME,
        messages=messages,
    )

    res = response.choices[0].message.content or ""
    if len(res)>0:
        kb.forAssistant(res)
    return res
