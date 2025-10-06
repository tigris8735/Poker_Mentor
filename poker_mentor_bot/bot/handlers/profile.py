from telegram import Update
from telegram.ext import ContextTypes

async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Заглушка для профиля"""
    await update.message.reply_text(
        "👤 Твой профиль скоро будет здесь!\n"
        "Мы работаем над системой статистики."
    )