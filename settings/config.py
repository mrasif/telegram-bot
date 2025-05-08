import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = os.getenv("DEBUG", "False") == "True"
ALLOWED_USERS = os.getenv("ALLOWED_USERS", "")
ALLOWED_USERS = [int(uid.strip()) for uid in ALLOWED_USERS.split(",") if uid.strip()]
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "")
SECRET = os.getenv("SECRET", "")
BIND_HOST = os.getenv("BIND_HOST","0.0.0.0")
BIND_PORT = int(os.getenv("BIND_PORT",3000))
DOMAIN_URL = os.getenv("DOMAIN_URL","")
WEBHOOK_URL = DOMAIN_URL + "/" + SECRET

LLM_MODEL_NAME = os.getenv("LLM_MODEL_NAME", "")
LLM_BASE_URL = os.getenv("LLM_BASE_URL", "")
LLM_API_KEY = os.getenv("LLM_API_KEY", "")
