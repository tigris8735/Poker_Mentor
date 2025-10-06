import os
from dotenv import load_dotenv

load_dotenv()

# Обязательные настройки
BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL", "https://your-app-name.railway.app") + "/webhook"

# Настройки по умолчанию
DEFAULT_STAKE = "1/2"
DEFAULT_STACK = 100
AI_TYPES = ["Fish", "TAG", "LAG", "Nit"]

# Проверка обязательных переменных
if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN не установлен! Добавьте его в .env файл")