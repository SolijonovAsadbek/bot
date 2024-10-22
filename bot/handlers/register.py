from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State, StatesGroup

register_router = Router()


class Form(StatesGroup):
    name = State()
    phone = State()
    address = State()


@register_router.message(Command('register'))
async def start_register(message: Message, state: FSMContext):
    await message.answer("Ro'yxatdan o'tish ismingizni kiriting:")
    await state.set_state(Form.name)


@register_router.message(Form.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Telefon raqamni kiriting:")
    await state.set_state(Form.phone)


@register_router.message(Form.phone)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await message.answer("Manzilingizni kiriting:")
    await state.set_state(Form.address)


@register_router.message(Form.address)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(address=message.text)

    datas = await state.get_data()
    name = datas['name']
    phone = datas['phone']
    address = datas['address']
    await message.answer(f"Sizning ma'lumotlaringiz:\n\n<b>Name: </b> {name}\n"
                         f"<b>Phone: </b> {phone}\n"
                         f"<b>Address: </b> {address}")
    await state.clear()
