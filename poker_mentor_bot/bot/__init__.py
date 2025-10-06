from telegram.ext import CommandHandler, MessageHandler, filters, CallbackQueryHandler
from .start import start
from .quick_game import quick_game, handle_ai_selection
from .hand_analysis import hand_analysis
from .learning import learning
from .profile import profile
from .game_settings import game_settings

def setup_handlers(application):
    """Настройка всех обработчиков бота"""
    
    # Команды
    application.add_handler(CommandHandler("start", start))
    
    # Основное меню
    application.add_handler(MessageHandler(filters.Text("🚀 Быстрая игра"), quick_game))
    application.add_handler(MessageHandler(filters.Text("📊 Анализ руки"), hand_analysis))
    application.add_handler(MessageHandler(filters.Text("📚 Обучение"), learning))
    application.add_handler(MessageHandler(filters.Text("👤 Мой профиль"), profile))
    application.add_handler(MessageHandler(filters.Text("⚙️ Настройка игры"), game_settings))
    
    # Callback обработчики
    application.add_handler(CallbackQueryHandler(handle_ai_selection, pattern="^ai_"))
    
    # Обработчик неизвестных команд
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, unknown_command))

async def unknown_command(update, context):
    """Обработчик неизвестных команд"""
    await update.message.reply_text(
        "🤔 Не понимаю эту команду. Используйте меню ниже 👇",
        reply_markup=context.bot_data.get('main_menu')
    )