from telegram.ext import ApplicationBuilder
from config.settings import TELEGRAM_TOKEN
from bot.dispatcher import setup_dispatcher



def main():

    if not TELEGRAM_TOKEN:
        raise ValueError("TELEGRAM_TOKEN is not set. Please set it in the .env file.")
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    setup_dispatcher(app)

    print("Bot is running...")
    app.run_polling()


if __name__ == '__main__':
    main()
