import os
import json

kb={}

def forAssistant(text: str, uid: str):
	if kb.get(uid) is not None:
		kb[uid].append({'role': 'assistant', 'metadata': None, 'content': text, 'options': None})
		# print("UID exists!")
	else:
		kb[uid]=[{'role': 'assistant', 'metadata': None, 'content': text, 'options': None}]
		# print("UID not found.")
    # chatKnowledge.append({'role': 'assistant', 'metadata': None, 'content': text, 'options': None})

def forUser(text: str, uid: str):
	if kb.get(uid) is not None:
		kb[uid].append({'role': 'user', 'metadata': None, 'content': text, 'options': None})
		# print("UID exists!")
	else:
		kb[uid]=[{'role': 'user', 'metadata': None, 'content': text, 'options': None}]
		# print("UID not found.")
    # chatKnowledge.append({'role': 'user', 'metadata': None, 'content': text, 'options': None})

def getHistory(uid: str):
	if uid not in kb:
		kb[uid] = []
	return kb[uid]

KB_FILE = "kb_store.json"  # Path to your storage file

def save_kb():
	with open(KB_FILE, "w") as f:
		json.dump(kb, f, indent=2)

def load_kb():
    global kb
    if os.path.exists(KB_FILE):
    	with open(KB_FILE, "r") as f:
     		kb = json.load(f)
