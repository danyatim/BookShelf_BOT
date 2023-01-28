from aiogram import Dispatcher
from aiogram.types import Message

from lexicon.lexicon import LEXICON


async def send_other_message(message: Message):
    await message.answer(text=LEXICON['other_message'])


def register_echo_handler(dp: Dispatcher):
    dp.register_message_handler(send_other_message)
