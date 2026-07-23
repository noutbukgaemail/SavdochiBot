import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from config import BOT_TOKEN
from keyboards.menu import main_menu
from handlers.stars import router as stars_router
from handlers.check import router as check_router
from handlers.premium import router as premium_router
from handlers.admin import router as admin_router
from handlers.database.db import add_user
from aiogram.fsm.storage.memory import MemoryStorage
from handlers.contact import router as contact_router

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())
dp.include_router(stars_router)
dp.include_router(check_router)
dp.include_router(premium_router)
dp.include_router(admin_router)
dp.include_router(contact_router)

@dp.message(Command("start"))
async def start(message: Message):
    add_user(
        message.from_user.id,
        message.from_user.full_name
    )

    await message.answer(
        "🤖 Savdochi Botga xush kelibsiz!",
        reply_markup=main_menu
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())