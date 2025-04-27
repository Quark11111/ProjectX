from aiogram import Router, F 
from aiogram.types import Message
from keyboards.reply import main_menu_kb
from aiogram.enums import ParseMode

router = Router()

@router.message(F.text == '/start')
async def cmd_start(message: Message):
    await message.answer(
        "<b>Привет! Я бот-консультант Quarks Motors.</b>\n\n"
        "Выберите, что вас интересует:",
        reply_markup=main_menu_kb()
  
    )