from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.emoji import emojize

import translations as txt

bt_final = KeyboardButton(emojize(txt.kb['bt_final']))
bt_chan = KeyboardButton(emojize(txt.kb['bt_chan']))
bt_sub = KeyboardButton(emojize(txt.kb['bt_sub']))
bt_about = KeyboardButton(emojize(txt.kb['bt_about']))
menu_kb = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=False).add(
    bt_final).add(bt_chan).add(bt_sub).add(bt_about)
