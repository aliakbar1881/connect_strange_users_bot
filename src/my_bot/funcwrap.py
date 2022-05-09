import json

from src.utils.reply_mark import reply_mark
from src.IO import io
from src.utils.users import create_user

def wrap_decorating(self):
    """
    wrap Bot class functions
    """

    @self.bot.message_handler(commands=["start"])
    def send_message(message):
        create_user(self, message)
        self.bot.reply_to(
            message,
            self.welcome.format(message.from_user.first_name)
        )

    @self.bot.message_handler(commands=["help"])
    def helper(message):
        self.bot.reply_to(
            message,
            self.helper.format(message.from_user.first_name)
        )

    @self.bot.message_handler(func=lambda m: True)
    def show_mark(message):
        markup = reply_mark()
        self.bot.send_message(
            message.from_user.id,
            "Choose one option",
            reply_markup=markup
                         )
