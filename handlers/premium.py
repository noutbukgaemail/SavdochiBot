from aiogram import Router, F
from aiogram.types import Message

router = Router()


@router.message(F.text == "💎 Premium")
async def premium(message: Message):
    await message.answer("""
🛸 PREMIUM XIZMATI 🛸

⭐️ 1 Oylik ➠ 45.000 so'm ✅

⭐️ 1 Yillik ➠ 290.000 so'm ✅

📕 AKKGA KIRIB OLINADI 📗

⭐️ 3 Oylik ➠ 185.000 so'm ✅

⭐️ 6 Oylik ➠ 221.000 so'm ✅

⭐️ 1 Yillik ➠ 390.000 so'm ✅

📷 AKKGA KIRMASDAN OLINADI 📗
""")