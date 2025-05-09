from openai import OpenAI
from settings import config
from llm import kb, agent

openai = OpenAI(
    base_url=config.LLM_BASE_URL,
    api_key=config.LLM_API_KEY
)

system_message = "You are a helpful assistant. Your name is 'Alex'."
system_message += "Give short, courteous answers, no more than 1 sentence. "
system_message += "Convert time to 12 hours clock if user is asking for 12hours clock. Your current time format is '%Y-%m-%d %H:%M:%S', when user ask for time then tell time only and for date tell date."
system_message += "Always be accurate. If you don't know the answer, say so."

def chat(text: str) -> str:
    history= kb.getHistory()
    kb.forUser(text)
    messages = [{"role": "system", "content": system_message}] + history + [{"role": "user", "content": text}]
    response = openai.chat.completions.create(
    	model=config.LLM_MODEL_NAME,
     	messages=messages,
      	tools=agent.getTools(),
    )

    if response.choices[0].finish_reason=="tool_calls":
        message = response.choices[0].message
        response = agent.handle_tool_call(message)
        messages.append(message)
        messages.append(response)
        response = openai.chat.completions.create(
        	model=config.LLM_MODEL_NAME,
         	messages=messages,
        )

    res = response.choices[0].message.content or ""
    if len(res)>0:
        kb.forAssistant(res)
    return res
