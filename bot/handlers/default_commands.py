from aiogram import Router
from aiogram.filters import Command, StateFilter
from aiogram.types import Message
from bot.keyboards import get_choice_keyboard
from aiogram.fsm.context import FSMContext
from bot.settings import OrderStates

router = Router()


@router.message(Command(commands=["start"]))
async def cmd_start(message: Message, state: FSMContext):
    await state.set_state(OrderStates.choosing_action)
    await message.answer('Hello, what to do?', reply_markup=get_choice_keyboard())


@router.message(Command(commands=["esc"]))
async def cmd_esc(message: Message, state: FSMContext):
    await state.set_state(OrderStates.choosing_action)
    await message.answer('Ok, what to do?', reply_markup=get_choice_keyboard())