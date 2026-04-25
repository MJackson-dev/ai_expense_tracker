import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

from main import process_expense, transcribe_audio

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    print("\n📩 Message received:", user_text)

    try:
        process_expense(user_text)

        await update.message.reply_text(
            f"✅ Added: {user_text}"
        )

    except Exception as e:
        print("Error:", e)

        await update.message.reply_text(
            "❌ Error processing expense"
        )

async def handle_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("🎤 Voice message received")

    voice = update.message.voice
    file = await context.bot.get_file(voice.file_id)

    file_path = "voice.ogg"
    await file.download_to_drive(file_path)

    print("✅ Voice downloaded:", file_path)

    text = transcribe_audio(file_path)

    print("📝 Transcription:", text)

    process_expense(text)

    await update.message.reply_text(f"📝 {text}")

    os.remove(file_path)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(MessageHandler(filters.VOICE, handle_voice))

    print("🤖 Bot running...")
    app.run_polling()


if __name__ == "__main__":
    main()