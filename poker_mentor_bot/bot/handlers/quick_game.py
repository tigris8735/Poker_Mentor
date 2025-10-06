from telegram import Update
from telegram.ext import ContextTypes

async def quick_game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Заглушка для быстрой игры"""
    await update.message.reply_text(
        "🎮 Функция 'Быстрая игра' скоро будет доступна!\n"
        "Сейчас мы работаем над игровым движком."
    )

async def handle_ai_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Заглушка для выбора AI"""
    await update.callback_query.answer()
    await update.callback_query.edit_message_text(
        "🤖 Выбор оппонента скоро будет доступен!"
    )