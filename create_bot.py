from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from dotenv import load_dotenv

import os

load_dotenv()
admin = os.getenv("ADMIN")
bot = Bot(os.getenv("TOKEN"), parse_mode=ParseMode.HTML)
dp = Dispatcher()
