from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎥 Просмотр аниме", callback_data='anime')],
        [InlineKeyboardButton("😂 Кринжовые видосики", callback_data='cringe')],
        [InlineKeyboardButton("🎮 Играть в компуктер", callback_data='ps5')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Любимый, чем сегодня займёмся?♥️",
        reply_markup=reply_markup
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    responses = {
        'anime': ("Уии! Давай досмотрим ГурренЛаганн 💝✨", 'CAACAgUAAxkBAAEB4MtlmOQeIvld7OBq7vRuQa1zGjMGMwAC6gEAAkp7cFYsGUXzeuAzMy4E'),
        'cringe': ("Ура, давай смореть реакты🤪", 'CAACAgUAAxkBAAEB4M1lmOQjPfBLt7PgmylqT9YeOa6r2gACmgEAAkp7cFZib9O8LUj3PS4E'),
        'ps5': ("Го каточку! 🎮💥 Пора уже лут в кс собирать😎", 'CAACAgUAAxkBAAEB4M9lmOQlgDth36s5lRZBdMpZzMPWZgACpQEAAkp7cFYqDWQ6dFA0ay4E')
    }

    text, sticker_id = responses.get(query.data, ("Неизвестный выбор 😳", None))

    await query.edit_message_text(text=text)
    if sticker_id:
        await query.message.reply_sticker(sticker=sticker_id)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Бот запущен...")
    app.run_polling()
