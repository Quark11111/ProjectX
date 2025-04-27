from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='📋 Услуги')],
            [KeyboardButton(text='📝 Оставить заявку')],
        ],
        resize_keyboard=True
    )