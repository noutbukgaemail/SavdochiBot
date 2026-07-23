from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text == "📞 Admin bilan bog'lanish")
async def contact_admin(message: Message):
    await message.answer(
        "📞 Admin bilan bog'lanish:\n\n"
        "Telegram: @s_712vv"
    )