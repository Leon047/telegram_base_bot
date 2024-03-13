"""
keyboards.py - Module for creating custom keyboards in the project.
"""
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Create hello button
def hello_button() -> ReplyKeyboardMarkup:
    hello = KeyboardButton(text='Hello')

    hello_btn_row = [hello,]

    return ReplyKeyboardMarkup(keyboard=[hello_btn_row], resize_keyboard=True)
