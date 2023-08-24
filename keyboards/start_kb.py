from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_start_kb() -> ReplyKeyboardMarkup:
    kb = [
        [
            KeyboardButton(text="Play"),
            KeyboardButton(text="My results")
        ]
    ]
    return ReplyKeyboardMarkup(keyboard=kb)