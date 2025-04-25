from telegram import Update
from telegram.ext import ContextTypes
from api.get_next_race import get_next_race
from api.driver_standings import driver_standings
from ai.classifier  import classify_intention


async def free_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    intention = None
    if update.message and update.message.text:
        text = update.message.text
        intention = classify_intention(text)
    
    if intention == "next_race":
        race_info = get_next_race()
        if update.message:
            await update.message.reply_text(f"Te paso toda la info de la fecha...\n\n{race_info}")
    
    if intention == "driver_standings":
        standings = driver_standings()
        if update.message:
            await update.message.reply_text(f"Te paso como viene el campeonato...\n\n{standings}")
    
    if intention == "colapinto":
        if update.message:
            await update.message.reply_text(f"Colapa no corre")