import asyncio
import logging

from aiogram import Bot, Dispatcher

from configs.config_reader import config

logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.BOT_TOKEN.get_secret_value(), parse_mode=None)
dp = Dispatcher()


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
