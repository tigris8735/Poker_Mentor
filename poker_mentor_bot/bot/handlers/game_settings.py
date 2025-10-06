from telegram import Update
from telegram.ext import ContextTypes

async def game_settings(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Заглушка для настроек игры"""
    await update.message.reply_text(
        "⚙️ Настройки игры появятся в следующем обновлении!"
    )