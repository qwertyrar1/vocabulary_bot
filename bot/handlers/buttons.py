from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from bot.settings import OrderStates
from aiogram.fsm.context import FSMContext
from bot.functions import add_to_file, get_from_file
from bot.keyboards import get_choice_keyboard
import random

router = Router()
random_word = 0


@router.message(OrderStates.choosing_action, F.text.lower() == 'new word')
async def new_word(message: Message, state: FSMContext):
    await message.answer('write new word and translate like this:\nhello,привет', reply_markup=ReplyKeyboardRemove())
    await state.set_state(OrderStates.writing_new_word)


@router.message(OrderStates.writing_new_word, F.text)
async def add_new_word(message: Message, state: FSMContext):
    add_to_file(message.text.split(','), str(message.from_user.id))
    await message.answer('whats next?', reply_markup=get_choice_keyboard())
    await state.set_state(OrderStates.choosing_action)


@router.message(OrderStates.choosing_action, F.text.lower() == 'training')
async def training(message: Message, state: FSMContext):
    global random_word
    random_word = random.choice(get_from_file(str(message.from_user.id)))
    await message.answer(f'translate this(/esc - to end):\n{random_word[0]}', reply_markup=ReplyKeyboardRemove())
    await state.set_state(OrderStates.training)


@router.message(OrderStates.training, F.text, F.text[0] != '/')
async def step_training(message: Message):
    global random_word
    if message.text in random_word[1:]:
        random_word = random.choice(get_from_file(str(message.from_user.id)))
        await message.answer(f'ok, then translate this:\n{random_word[0]}')
    else:
        await message.answer(f'wrong answer, correct word:\n{", ".join(random_word[1:])}')
        random_word = random.choice(get_from_file(str(message.from_user.id)))
        await message.answer(f'ok, then translate this:\n{random_word[0]}')

