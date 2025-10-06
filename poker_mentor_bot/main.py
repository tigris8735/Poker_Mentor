from fastapi import FastAPI
import uvicorn
from config import BOT_TOKEN
from telegram.ext import Application, CommandHandler, MessageHandler, filters

app = FastAPI(title="Poker Mentor Bot")

# Инициализируем бота
bot_app = Application.builder().token(BOT_TOKEN).build()

# Простой обработчик для тестирования
async def start(update, context):
    from bot.keyboards import get_main_menu
    await update.message.reply_text(
        "🤖 Бот работает! Это тестовая версия.",
        reply_markup=get_main_menu()
    )

async def echo(update, context):
    await update.message.reply_text(f"Вы сказали: {update.message.text}")

# Настраиваем обработчики
bot_app.add_handler(CommandHandler("start", start))
bot_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

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
    # Временно отключаем вебхук для локального тестирования
    # await bot_app.bot.set_webhook(WEBHOOK_URL)
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