from aiogram import Bot,Dispatcher,executor,types
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from buttons import *
from states import *
from api import create_feedback
from config import *

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot,storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(f'Salom {message.from_user.full_name}',reply_markup=keyboard,parse_mode='HTML')


@dp.message_handler(Text(startswith="Adminga ma'lumot jo'natish"))
async def feedback_1(message: types.Message):
    await message.answer('Xabarni junating')
    await FeedbackState.body.set()


@dp.message_handler(state=FeedbackState.body)
async def feedback_2(message: types.Message,state:FSMContext):
    body = message.text
    await state.update_data({'body':body})
    await message.answer("yoshingizni kiriting!")
    await FeedbackState.next()


@dp.message_handler(state=FeedbackState.age)
async def get_age(message: types.Message,state:FSMContext):
    age = message.text
    await state.update_data({'age':age})
    await message.answer("Ismingizni kiriting")
    await FeedbackState.next()


@dp.message_handler(state=FeedbackState.name)
async def get_age(message: types.Message,state:FSMContext):
    name = message.text
    await state.update_data({'name':name})
    data = await state.get_data()
    await message.answer(create_feedback(message.from_user.id,data['body'],data['age'],data['name']))
    await state.finish()


@dp.message_handler(text = 'Buyurtma')
async def buyurtma(message:types.Message):
    await message.answer('Taom tanlang!')
    await Register.food.set()

@dp.message_handler(state=Register.food)
async def feedback_2(message: types.Message,state:FSMContext):
    food = message.text
    await state.update_data({'food':food})
    await message.answer("Salat tanlang")
    await Register.next()

@dp.message_handler(state=Register.salad)
async def feedback_2(message: types.Message,state:FSMContext):
    salad = message.text
    await state.update_data({'salad':salad})
    await message.answer("Telefon raqam")
    await Register.next()

@dp.message_handler(state=Register.phone)
async def feedback_2(message: types.Message,state:FSMContext):
    phone = message.text
    await state.update_data({'phone':phone})
    data1 = await state.get_data()
    await message.answer("Raxmat")
    await state.finish()



if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)