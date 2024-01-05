from functools import cache
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


@cache
def get_choice_keyboard():
    keyboard = [
        [KeyboardButton(text='new word')],
        [KeyboardButton(text='training')]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)