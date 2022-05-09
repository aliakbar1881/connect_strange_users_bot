from telebot import types

from src.utils.constants import constants


def reply_mark():
    item = constants()
    markup = types.ReplyKeyboardMarkup(row_width=2)
    markup.add(*item)
    return markup
