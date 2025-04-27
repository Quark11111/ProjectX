from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states.application import ApplicationStates
from keyboards.reply import main_menu_kb
from utils.gsheet import save_to_google_sheet


router = Router()

@router.message(F.text == '📝 Оставить заявку')
async def ask_name(message: Message, state: FSMContext):
    await message.answer('Как вас зовут?')
    await state.set_state(ApplicationStates.waiting_for_name)

@router.message(ApplicationStates.waiting_for_name)
async def ask_phone(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Введите номер телефона?')
    await state.set_state(ApplicationStates.waiting_for_phone)


@router.message(ApplicationStates.waiting_for_phone)
async def finish(message: Message, state: FSMContext):
    user_data = await state.get_data()
    name = user_data['name']
    phone = message.text

    save_to_google_sheet(name, phone)

    await message.answer(
        'Спасибо! Мы скоро свяжемя с вами',
        reply_markup=main_menu_kb()

    )

    await state.clear()
