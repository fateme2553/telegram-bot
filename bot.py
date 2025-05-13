from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! ربات Fateme بدون VPN کار می‌کنه!")

app = ApplicationBuilder().token("توکن خودتو اینجا بذار").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
