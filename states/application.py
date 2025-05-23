from aiogram.fsm.state import StatesGroup, State

class ApplicationStates(StatesGroup):
    waiting_for_name = State()  
    waiting_for_phone = State()
    viewing_services = State()