from aiogram import Router, F, Bot
from aiogram.types import Message
from config import ADMIN_ID
from keyboards.admin import admin_keyboard

router = Router()


@router.message(F.text == "📸 Chek yuborish")
async def ask_check(message: Message):
    await message.answer("📸 To'lov chekini rasm sifatida yuboring.")


from aiogram import Router, F, Bot
from aiogram.types import Message

from config import ADMIN_ID
from keyboards.admin import admin_keyboard

router = Router()


@router.message(F.text == "📷 Chek yuborish")
async def check_info(message: Message):
    await message.answer(
        "📸 Iltimos, to'lov chekini rasm ko'rinishida yuboring."
    )


@router.message(F.photo)
async def get_check(message: Message, bot: Bot):
    photo = message.photo[-1].file_id

    await bot.send_photo(
        chat_id=ADMIN_ID,
        photo=photo,
        caption=(
            f"🧾 Yangi chek!\n\n"
            f"👤 Ism: {message.from_user.full_name}\n"
            f"🆔 ID: {message.from_user.id}"
        ),
        reply_markup=admin_keyboard(message.from_user.id)
    )

    await message.answer("✅ Chekingiz adminga jo'natildi.")