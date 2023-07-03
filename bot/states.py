from aiogram.dispatcher.filters.state import State,StatesGroup

class FeedbackState(StatesGroup):
    body = State()
    age = State()
    name = State()


class Register(StatesGroup):
    food = State()
    salad = State()
    phone = State()
    