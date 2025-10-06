from fastapi import FastAPI
import uvicorn
from bot.handlers import setup_handlers
from config import BOT_TOKEN, WEBHOOK_URL
from telegram.ext import Application

app = FastAPI(title="Poker Mentor Bot")

# Инициализируем бота
bot_app = Application.builder().token(BOT_TOKEN).build()

# Настраиваем обработчики
setup_handlers(bot_app)

@app.post("/webhook")
async def webhook(update: dict):
    """Эндпоинт для вебхука Telegram"""
    await bot_app.update_queue.put(update)
    return {"status": "ok"}

@app.on_event("startup")
async def on_startup():
    """Настройка при запуске"""
    await bot_app.initialize()
    await bot_app.start()
    await bot_app.bot.set_webhook(WEBHOOK_URL)
    print("🤖 Бот запущен и готов к работе!")

@app.on_event("shutdown")
async def on_shutdown():
    """Очистка при завершении"""
    await bot_app.stop()
    await bot_app.shutdown()

@app.get("/")
async def health_check():
    return {"status": "healthy", "message": "Poker Mentor Bot is running!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)