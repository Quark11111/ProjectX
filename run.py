import asyncio 
import aiohttp
from config import BOT_TOKEN
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.client.bot import DefaultBotProperties
from aiogram.types import BotCommand
from handlers import start, application, services 

TOKEN = (BOT_TOKEN)

async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(application.router)
    dp.include_router(services.router)

    await bot.set_my_commands([
        BotCommand(command='start', description='Запустить бота')
    ])

    print('Бот запущен')
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот остановлен вручную')
