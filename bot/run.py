import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from bot.data.config import BOT_TOKEN
from bot.handlers.register import register_router

# routers
from bot.handlers.start import start_router

TOKEN = BOT_TOKEN

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


async def main():
    dp.include_router(start_router)
    dp.include_router(register_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format="%(filename)s %(lineno)d  [%(asctime)s]    %(levelname)s   %(message)s")
    asyncio.run(main())
