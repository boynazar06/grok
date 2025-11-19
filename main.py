from groq import Groq
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TELEGRAM_TOKEN = "8045570656:AAF_HqZMJp6stoaEGz8b5PUx467YoCf9Kds"
GROQ_API_KEY = "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"

client = Groq(api_key=GROQ_API_KEY)


def query_ai(user_message):
    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "Siz foydali AI assistentsiz."},
                {"role": "user", "content": user_message}
            ],
            model="llama-3.1-8b-instant",
            temperature=0.7,
            max_tokens=300
        )
        return response.choices[0].message["content"]

    except Exception as e:
        return f"❌ Xatolik: {str(e)}"


def start(update, context):
    update.message.reply_text(
        "👋 Assalomu alaykum!\n"
        "Groq AI botiga xush kelibsiz!"
    )


def help_command(update, context):
    update.message.reply_text(
        "/start - Boshlash\n"
        "/help - Yordam"
    )


def handle_message(update, context):
    user_text = update.message.text
    reply = query_ai(user_text)
    update.message.reply_text(reply)


def main():
    print("🤖 Bot ishga tushmoqda...")

    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    print("✅ Bot ishlayapti!")
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
