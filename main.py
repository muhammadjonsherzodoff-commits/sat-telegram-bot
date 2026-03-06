from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random

TOKEN = "TOKENINGIZNI BU YERGA QO'YING"

WORDS = [
 {"word": "Abandon", "meaning": "leave completely"},
 {"word": "Benevolent", "meaning": "kind and generous"},
 {"word": "Candid", "meaning": "honest and direct"},
 {"word": "Daunt", "meaning": "make afraid"}
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! /newword yozing")

async def newword(update: Update, context: ContextTypes.DEFAULT_TYPE):
    w = random.choice(WORDS)
    await update.message.reply_text(f"{w['word']} - {w['meaning']}")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("newword", newword))

app.run_polling()
