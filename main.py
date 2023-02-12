import logging
from aiogram import Bot, Dispatcher, executor, types
import wikipedia

bot = Bot(token='6082537401:AAH_83fEaO_1_YfwyfhrYuHpFhvGRlXMx0I')
dp = Dispatcher(bot)
wikipedia.set_lang('uz')


@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply("Salom siz siz Stady_hack tomonidan yaratilgan botni ishga tushirdingiz")


@dp.message_handler(commands=['Stady_Hack'])
async def Me(message: types.Message):
    await message.reply(" 🏛 FarPI   \n Energetika Fakulteti 2 kurs talabasi  👨‍🎓 \n  👨‍💻  Solijonov O`lmasxo`ja")


@dp.message_handler()
async def sendwiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bu mavzuga oid maqola tpilmadi")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
