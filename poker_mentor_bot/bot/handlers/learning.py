from telegram import Update
from telegram.ext import ContextTypes

async def learning(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Заглушка для обучения"""
    await update.message.reply_text(
        "📚 Раздел 'Обучение' готовится!\n"
        "Скоро здесь будут уроки и стратегии."
    )