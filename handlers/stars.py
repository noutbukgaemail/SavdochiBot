from aiogram import Router, F
from aiogram.types import Message

router = Router()


@router.message(F.text == "⭐ Stars narxlari")
async def stars_price(message: Message):
    await message.answer(
        "⭐️ Stars narxlari\n\n"
        "50 ⭐ = 10 000 so'm\n"
        "100 ⭐ = 20 000 so'm\n"
        "250 ⭐ = 50 000 so'm\n"
        "500 ⭐ = 100 000 so'm\n\n"
        "📸 To'lov qilgan bo'lsangiz, \"Chek yuborish\" tugmasini bosing."
    )