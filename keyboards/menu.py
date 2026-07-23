from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
[
    KeyboardButton(text="⭐ Stars narxlari")
],
[
    KeyboardButton(text="💎 Premium")
],
[
    KeyboardButton(text="📷 Chek yuborish")
],
[
    KeyboardButton(text="📞 Admin bilan bog'lanish")
],
[
    KeyboardButton(text="⚙️ Admin panel")
]
    ],
    resize_keyboard=True
)