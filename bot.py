# Imports
from aiogram import Bot, Dispatcher, executor
from handlers import setup_handlers
import config as cfg

# Launching
bot = Bot(token=cfg.BOT_TOKEN)
dp = Dispatcher(bot)
setup_handlers(dp, bot)


if __name__ == '__main__':
    executor.start_polling(dp)
