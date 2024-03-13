"""
views.py - Module for defining view functions and handling user
interactions in the project.
"""
from aiogram import F, Router, types
from aiogram.filters import CommandStart
from aiogram.utils.markdown import hbold

from .messages import hello_world_msg
from .keyboards import hello_button

# All handlers should be attached to the Router.
router = Router(name=__name__)

@router.message(CommandStart())
async def send_welcome(message: types.Message):
    """
    This handler receives messages with `/start` command
    """
    await message.reply(
        text = hello_world_msg,
        reply_markup = hello_button()
    )

@router.message(F.text=='Hello')
async def send_hello(message: types.Message):
    """Hello request handler"""
    await message.answer(f'Hello, {hbold(message.from_user.full_name)}!')
