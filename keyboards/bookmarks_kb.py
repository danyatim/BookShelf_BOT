from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from lexicon.lexicon import LEXICON
from services.file_handling import book


def creat_bookmarks_keyboard(*args: int) -> InlineKeyboardMarkup:
    bookmarks_kb: InlineKeyboardMarkup = InlineKeyboardMarkup()
    for button in sorted(args):
        bookmarks_kb.add(InlineKeyboardButton(
            text=f'{button} - {book[button]}',
            callback_data=str(button)
        ))
    bookmarks_kb.row(InlineKeyboardButton(text=LEXICON['edit_bookmarks_button'],
                                          callback_data='edit_bookmarks'),

                     InlineKeyboardButton(text=LEXICON['cancel'],
                                          callback_data='cancel'))
    return bookmarks_kb


def creat_edit_keyboard(*args: int) -> InlineKeyboardMarkup:
    bookmarks_kb: InlineKeyboardMarkup = InlineKeyboardMarkup()
    for button in sorted(args):
        bookmarks_kb.add(InlineKeyboardButton(
            text=f'{LEXICON["del"]} {button} - {book[button]}',
            callback_data=f'{button}del'
        ))
    bookmarks_kb.add(InlineKeyboardButton(text=LEXICON['cancel'],
                                          callback_data='cancel'))
    return bookmarks_kb
