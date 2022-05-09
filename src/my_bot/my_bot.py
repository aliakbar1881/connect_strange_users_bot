"""
Bot module
"""
from src.data import DATA_DIR
from src.my_bot.funcwrap import wrap_decorating
from src.utils.helper import helper
from src.utils.welcome import welcome


class Bot:
    """
    Add some feature to telebot module
    """
    def __init__(
            self,
            bot
                ):
        self.bot = bot
        self.users = {}
        self.helper = helper()
        self.welcome = welcome()

    def __call__(self):
        wrap_decorating(self)
        self.bot.infinity_polling()
