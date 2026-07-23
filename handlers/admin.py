from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from config import ADMIN_ID
from handlers.database.db import get_users_count, get_all_users
from handlers.states import BroadcastState
from keyboards.admin_menu import admin_menu
from keyboards.menu import main_menu

router = Router()


# Admin panel
@router.message(F.text == "⚙️ Admin panel")
async def admin_panel(message: Message):
    if message.from_user.id != ADMIN_ID:
        await message.answer("❌ Siz admin emassiz!")
        return

    users = get_users_count()

    await message.answer(
        f"""⚙️ ADMIN PANEL

👥 Foydalanuvchilar soni: {users}
""",
        reply_markup=admin_menu
    )


# Reklama yuborish
@router.message(F.text == "📢 Reklama yuborish")
async def start_broadcast(message: Message, state: FSMContext):
    if message.from_user.id != ADMIN_ID:
        return

    await state.set_state(BroadcastState.waiting_for_message)
    await message.answer("📨 Yubormoqchi bo'lgan xabaringizni yuboring.")


# Reklamani barcha foydalanuvchilarga yuborish
@router.message(BroadcastState.waiting_for_message)
async def send_broadcast(message: Message, state: FSMContext, bot: Bot):
    users = get_all_users()

    success = 0

    for user in users:
        try:
            await bot.send_message(user[0], message.text)
            success += 1
        except:
            pass

    await state.clear()

    await message.answer(
        f"✅ Reklama {success} ta foydalanuvchiga yuborildi.",
        reply_markup=main_menu
    )


# Asosiy menyuga qaytish
@router.message(F.text == "🏠 Asosiy menyu")
async def back_menu(message: Message):
    await message.answer(
        "🏠 Asosiy menyu",
        reply_markup=main_menu
    )
    from aiogram.types import CallbackQuery


@router.callback_query(F.data.startswith("approve_"))
async def approve_payment(callback: CallbackQuery, bot: Bot):
    user_id = int(callback.data.split("_")[1])

    await bot.send_message(
        chat_id=user_id,
        text="✅ To'lovingiz tasdiqlandi!\n\nRahmat! Buyurtmangiz qabul qilindi."
    )

    await callback.message.edit_caption(
        caption=callback.message.caption + "\n\n✅ TASDIQLANDI"
    )

    await callback.answer("Tasdiqlandi!")


@router.callback_query(F.data.startswith("reject_"))
async def reject_payment(callback: CallbackQuery, bot: Bot):
    user_id = int(callback.data.split("_")[1])

    await bot.send_message(
        chat_id=user_id,
        text="❌ To'lovingiz rad etildi.\n\nIltimos, chekni qayta yuboring yoki admin bilan bog'laning."
    )

    await callback.message.edit_caption(
        caption=callback.message.caption + "\n\n❌ RAD ETILDI"
    )

    await callback.answer("Bekor qilindi!")