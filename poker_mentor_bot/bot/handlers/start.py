from telegram import Update
from telegram.ext import ContextTypes
from bot.keyboards import get_main_menu

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /start"""
    user = update.effective_user
    welcome_text = f"""
Привет, {user.first_name}! 👋

Я - Poker Mentor, твой персональный тренер по покеру! 

Что я умею:
🎮 Быстрая игра - сыграй против AI оппонентов
📊 Анализ руки - получи детальный разбор своей раздачи  
📚 Обучение - изучи основы и стратегии покера
👤 Профиль - отслеживай свой прогресс

Выбери действие ниже 👇
    """
    
    await update.message.reply_text(
        welcome_text,
        reply_markup=get_main_menu()
    )