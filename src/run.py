"""
run script . . .
"""
import os

import telebot
from loguru import logger

from src.my_bot.my_bot import Bot


class Telegram:

    def __init__(self):
        bot = telebot.TeleBot(os.environ["BOT_TOKEN"], parse_mode='HTMl')
        self.run_bot = Bot(bot)
        del bot

    def run(self):
        logger.info("run is called. ")
        self.run_bot()

if __name__ == "__main__":
    logger.info("run.py script is run ...")
    MY_BOT = Telegram()
    MY_BOT.run()
