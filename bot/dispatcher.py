from telegram.ext import Application, MessageHandler, filters
from bot.handlers import free_message

def setup_dispatcher(application: Application):
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, free_message))
