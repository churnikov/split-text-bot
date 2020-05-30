import os

from aiogram import Bot, Dispatcher, executor, types
from dotenv import find_dotenv, load_dotenv
from loguru import logger

load_dotenv(find_dotenv())
API_TOKEN = os.getenv("API_TOKEN")

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def process(message: types.Message):

    logger.info("Processing {}", message)
    text: str = message.text
    text = text.replace("\n", " ")
    for txt in text.split("."):
        await message.answer(txt)


def main():
    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    main()
