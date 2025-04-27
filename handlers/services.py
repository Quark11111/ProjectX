from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from states.application import ApplicationStates

router = Router()

SERVICES_TEXT = """🚗 *Наши услуги Quarks Motors:*

🛢 *Замена масла* — Быстрая замена масла и фильтра с гарантией качества.

🔍 *Диагностика авто* — Комплексная проверка состояния автомобиля с использованием сканера.

🔧 *Ремонт двигателя* — Точный ремонт любой сложности с оригинальными запчастями.

🛑 *Тормозная система* — Проверка и замена колодок, дисков, тормозной жидкости.

📐 *Сход-развал* — Профессиональная регулировка углов установки колёс.
"""

@router.message(F.text == '📋 Услуги')
async def show_services(message: Message, state: FSMContext):
    current_state = await state.get_state()

    if current_state == ApplicationStates.viewing_services:
        await message.answer('Вы уже смотрите наши услуги 😉')
        return


    await message.answer(SERVICES_TEXT, parse_mode='Markdown')
    await state.set_state(ApplicationStates.viewing_services)