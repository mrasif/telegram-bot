chatKnowledge=[]

def forAssistant(text: str):
    chatKnowledge.append({'role': 'assistant', 'metadata': None, 'content': text, 'options': None})

def forUser(text: str):
    chatKnowledge.append({'role': 'user', 'metadata': None, 'content': text, 'options': None})

def getHistory() -> list:
    return chatKnowledge
