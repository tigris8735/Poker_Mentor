from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

def get_main_menu():
    """Главное меню бота"""
    keyboard = [
        ["🚀 Быстрая игра"],
        ["📊 Анализ руки", "📚 Обучение"],
        ["👤 Мой профиль", "⚙️ Настройка игры"]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)