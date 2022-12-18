from aiogram.dispatcher.filters.state import State, StatesGroup


class SendMessage(StatesGroup):
    id = State()
    xabar = State()

class SendReklama(StatesGroup):
    rek = State()
