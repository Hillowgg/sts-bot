import dotenv
import os

from aiogram import Bot, Dispatcher, executor, types

dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    """Send a message when the command /start is issued."""

    await message.reply("Привет, я помогу тебе посчитать налоги) \n (C) Hillow")


@dp.message_handler(commands=['count'])
async def count(message: types.Message):
    """gets 2 numbers and returns the taxes"""

    args = message.get_args().split()
    if len(args) < 2:
        return await message.reply("Нет аргументов")

    income = float(args[0])
    outcome = float(args[1])

    if income < outcome:
        return await message.reply("Ты в минусе")

    profit = income - outcome

    tax_type1 = income * 0.06
    tax_type2 = profit * 0.15

    message_text = (
        f'Ваш доход: {income:,.2f}\n'
        f'Ваши расходы: {outcome:,.2f}\n'
        f'Ваша прибыль: {profit:,.2f}\n'
        f'"Доходы": {tax_type1:,.2f}\n'
        f'"Доходы - Расходы": {tax_type2:,.2f}\n'
        f'Чистая max прибыль: {profit - min(tax_type1, tax_type2):,.2f}\n'
    )

    await message.reply(message_text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
