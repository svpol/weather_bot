import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.exceptions import MessageTextIsEmpty
from weather import Weather


logging.basicConfig(level=logging.INFO)


BOT_API_TOKEN = 'XXXXXXXXXXXX' # a valid telegram bot token provided by BotFather
WEATHER_API_KEY = 'YYYYYYYYYYYYYYYY' # a valid open weather map API token


bot = Bot(token=BOT_API_TOKEN)
dp = Dispatcher(bot)


def get_weather(text):
    try:
        extended_weather = Weather.get_current_weather(text, WEATHER_API_KEY)
        main_weather = Weather.get_weather_main(extended_weather)
        temperature = Weather.get_temperature(extended_weather)
        return [main_weather, temperature]
    except KeyError:
        print('KeyError: city name is absent in the database.')


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
   await message.reply("Hi! Type a city name to see the weather.")


@dp.message_handler()
async def text_message(message: types.Message):
    try:
        weather_list = get_weather(message.text)
        if weather_list:
            await message.answer(f"{weather_list[0]}\n{weather_list[1]}")
        else:
            await message.answer("Looks like this city is absent in our database. Check spelling or type the nearest city.")
    except MessageTextIsEmpty:
        print('MessageTextIsEmpty: city name is absent in the database.')


if __name__ == '__main__':

    executor.start_polling(dp, skip_updates=True)
