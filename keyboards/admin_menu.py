from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📢 Reklama yuborish")],
        [KeyboardButton(text="📊 Statistika")],
        [KeyboardButton(text="🏠 Asosiy menyu")]
    ],
    resize_keyboard=True
)