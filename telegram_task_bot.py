import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Bot token from environment variable
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! I'm your personal task assistant bot. Send me a command to begin.")

# Handle regular text messages
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text.lower()

    if "schedule" in user_input:
        await update.message.reply_text("Okay, tell me what to schedule and when?")
    elif "email" in user_input and "send" in user_input:
        await update.message.reply_text("Sure! Please provide recipient and content.")
    elif "schedule" in user_input and ("today" in user_input or "tasks" in user_input):
        await update.message.reply_text("Here’s your schedule for today: \n- Meeting at 10 AM\n- Submit report by 4 PM")
    elif "done" in user_input or "completed" in user_input:
        await update.message.reply_text("Task marked as completed ✅")
    else:
        await update.message.reply_text("Sorry, I didn't understand. Try commands like: 'schedule meeting', 'send email', or 'show today’s tasks'.")

# Main function
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    print("Bot is running...")
    app.run_polling()
