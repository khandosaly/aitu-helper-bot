from aiogram import types
from aiogram.types import ParseMode
from aiogram.utils.emoji import emojize
from aiogram.utils.markdown import text, bold

import config as cfg
import keyboards as kb
import translations as txt
import utils

bot = None

state = {}
rk1 = {}
rk2 = {}


def setup_handlers(dp, dp_bot):
    global bot
    bot = dp_bot
    dp.register_message_handler(send_welcome, commands=['start', 'help', 'restart', 'reboot'])
    dp.register_message_handler(calculate, text=emojize(txt.kb['bt_final']))
    dp.register_message_handler(channels, text=emojize(txt.kb['bt_chan']))
    dp.register_message_handler(subjects, text=emojize(txt.kb['bt_sub']))
    dp.register_message_handler(about, text=emojize(txt.kb['bt_about']))
    dp.register_message_handler(echo)


# Starting message
async def send_welcome(message: types.Message):
    global state
    await message.answer(emojize(txt.misc['start']), reply_markup=kb.menu_kb)
    state[message.from_user.id] = 'MENU'


# BUTTON: Расчёт файнала
async def calculate(message: types.Message):
    global state
    msg = text(emojize(txt.misc['calc_start']))
    await message.answer(msg)
    state[message.from_user.id] = 'FINAL_ONE'  # waiting input


# Channels
async def channels(message: types.Message):
    global state
    await message.answer(txt.msg['channels'], reply_markup=kb.menu_kb)  # show the menu


# Subjects photo
async def subjects(message: types.Message):
    global state
    msg = text(emojize(txt.misc['subjects']))
    await message.answer(msg, reply_markup=kb.menu_kb)  # back to the menu
    await bot.send_document(chat_id=message.from_user.id, document=cfg.SUBJECTS_DOC)


async def about(message: types.Message):
    global state
    msg = text(emojize(txt.misc['about']))
    await message.answer(msg, reply_markup=kb.menu_kb)


# All other listener
async def echo(message: types.Message):
    u = message.from_user
    global state, rk1, rk2
    if state[u.id] == 'FINAL_ONE':
        if utils.isnumeric(message.text) and 0 <= float(message.text) <= 100:
            rk1[u.id] = float(message.text)
            await message.answer(txt.msg['2nd_att'])
            state[u.id] = 'FINAL_TWO'  # going to FINAL_TWO
        else:
            await message.answer(txt.msg['1nd_att_wrong'])  # hide keyboard
    elif state[u.id] == 'FINAL_TWO':
        if utils.isnumeric(message.text) and 0 <= float(message.text) <= 100:
            rk2[u.id] = float(message.text)
            terms_mid = rk1[u.id] + rk2[u.id]
            mid_total = round(terms_mid * 0.3, 2)
            pov_final = utils.get_pov_final(terms_mid)

            msg_ret = text(emojize(':black_circle:'), bold(
                'Что бы не получить ретейк или пересдачу'),
                ' (>50) ', '\n', utils.get_ret_final(terms_mid), '% на файнале.')
            msg_sch = text(emojize(':red_circle:'), bold(
                'Для сохранения стипендии '),
                ' (>70) ', '\n', utils.get_sch_final(terms_mid), '% на файнале.')
            if pov_final > 100:
                msg_pov = text(emojize(':blue_circle:'), bold('Для получения повышенной стипендии'),
                    ' (>90) \n', 'Невозможно получить')
            else:
                msg_pov = text(emojize(':blue_circle:'), bold(
                    'Для получения повышенной стипендии'), ' (>90) \n', pov_final, '% на файнале.')

            msg_full = text(emojize(':white_circle:'),
                            'Если вы сдадите файнал на 100%, вы получите тотал:', '\n', round(mid_total + 40, 2))
            #
            if terms_mid < 100:
                await message.answer(txt.misc['retake'], reply_markup=kb.menu_kb)  # show menu keyboard
                state[u.id] = 'MENU'  # back to the menu
            else:
                await message.answer(msg_ret, parse_mode=ParseMode.MARKDOWN)
                await message.answer(msg_sch, parse_mode=ParseMode.MARKDOWN)
                await message.answer(msg_pov, parse_mode=ParseMode.MARKDOWN)
                await message.answer(msg_full, reply_markup=kb.menu_kb,
                                     parse_mode=ParseMode.MARKDOWN)  # show main menu keyboard
                state[u.id] = 'MENU'  # back to the menu
        else:
            await message.answer(txt.msg['2nd_att_wrong'])
    else:
        await message.answer(txt.msg['echo_error'],
                             reply_markup=kb.menu_kb)  # show main menu
