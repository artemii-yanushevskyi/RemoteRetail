"""
This is a echo bot.
It echoes any incoming text messages.
"""
import asyncio
import logging, time

from aiogram import Bot, Dispatcher, executor, types, exceptions
# to run aiogram we should create
# a new environment 'conda create --name py36 python=3.6' (/anaconda3/envs/py37)
# to activate it 'conda activate py37'
from bot_token import bot_token as BOT_TOKEN

# Configure logging
logging.basicConfig(level=logging.INFO)
log = logging.getLogger('broadcast')

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN, parse_mode='Markdown')
dp = Dispatcher(bot)

# User Settings
CHAT_ID = -378550435 # the PythonTelegram Group
affirmative = ['мерси', 'thanks', 'ok', '👌', '👍']
messages_bot = []

current_time = time.asctime(time.localtime(time.time()))


# Handlers
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when client send `/start` or `/help` commands.
    """
    intro_message = '*The bot had been started.* Current date and time\n_%s_' % current_time
    await message.reply(intro_message)

async def send_message(user_id: int, text: str, disable_notification: bool = False) -> types.Message:
    """
    Safe messages sender
    :param user_id:
    :param text:
    :param disable_notification:
    :return:
    """
    try:
        msg = await bot.send_message(user_id, text, disable_notification=disable_notification)
    except exceptions.BotBlocked:
        log.error(f"Target [ID:{user_id}]: blocked by user")
    except exceptions.ChatNotFound:
        log.error(f"Target [ID:{user_id}]: invalid user ID")
    except exceptions.RetryAfter as e:
        log.error(f"Target [ID:{user_id}]: Flood limit is exceeded. Sleep {e.timeout} seconds.")
        await asyncio.sleep(e.timeout)
        return await send_message(user_id, text)  # Recursive call
    except exceptions.UserDeactivated:
        log.error(f"Target [ID:{user_id}]: user is deactivated")
    except exceptions.TelegramAPIError:
        log.exception(f"Target [ID:{user_id}]: failed")
    else:
        log.info(f"Target [ID:{user_id}]: success")
        return msg
    return msg


@dp.message_handler(regexp='(^dog[s]?$|hound)')
async def dog(message: types.Message):
    with open('data/dog.jpg', 'rb') as photo:
        await bot.send_photo(message.chat.id, photo, caption='Dog is here 🐶',
                             reply_to_message_id=message.message_id)

@dp.message_handler(regexp='(^timer ?$)')
async def timer(message: types.Message):
    timer = 300
    msg = await send_message(message.chat.id, 'Start timer: %d' % timer)
    try:
        while True:
            if await bot.edit_message_text('timer: %d' % timer, msg.chat.id, msg.message_id):
                timer -= 1
            # await asyncio.sleep(1)
            if timer == 0:
                break
    finally:
        timer = 300
        log.info(f"{timer} messages successful sent.")

@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)