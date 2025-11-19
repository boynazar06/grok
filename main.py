from groq import Groq
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


TELEGRAM_TOKEN = "8045570656:AAF_HqZMJp6stoaEGz8b5PUx467YoCf9Kds"  # @BotFather dan
GROQ_API_KEY = "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"  # console.groq.com/keys dan


client = Groq(api_key=GROQ_API_KEY)


def query_ai(user_message):
    """Groq API bilan chat"""
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "Siz foydali yordamchi AI assistentsiz. Qisqa va aniq javob bering."
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            model="llama-3.1-8b-instant",  # Eng tez model
            temperature=0.9,
            max_tokens=400,
        )

        return chat_completion.choices[0].message.content

    except Exception as e:
        return f"❌ Xatolik: {str(e)}"



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Bot boshlash"""
    welcome = (
        "👋 Assalomu alaykum!\n\n"
        "🤖 Men AI botman\n"
        "💬 Menga savol bering!\n\n"
        "⚡ Model: Llama 3.1 (Groq)\n"
        "🆓 Bepul\n"
        "⚡ Juda tez (0.5 soniya)"
    )
    await update.message.reply_text(welcome)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Xabarga javob"""
    user_message = update.message.text

    # Typing
    await update.message.chat.send_action("typing")

    # AI javob
    bot_reply = query_ai(user_message)

    # Yuborish
    await update.message.reply_text(bot_reply)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Yordam"""
    help_text = (
        "📚 Bot haqida:\n\n"
        "🤖 Model: Llama 3.1 (8B)\n"
        "🚀 API: Groq (eng tez!)\n"
        "💬 Menga savol bering!\n\n"
        "⚙️ Buyruqlar:\n"
        "/start - Boshlash\n"
        "/help - Yordam"
    )
    await update.message.reply_text(help_text)


def main():
    """Ishga tushirish"""
    print("🤖 Bot ishga tushmoqda...")

    app = Application.builder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ Bot ishlayapti!")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":

    main()
