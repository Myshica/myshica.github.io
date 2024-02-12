from aiogram import Router
from aiogram.filters import CommandStart

from aiogram.types import *
from aiogram.utils.keyboard import InlineKeyboardBuilder

start_router = Router()


@start_router.message(CommandStart())
async def start(message: Message):
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text="Открыть преложение", web_app=WebAppInfo(url="https://myshica.github.io/site.html")))
    await message.answer("Здравствуйте!", reply_markup=keyboard.as_markup())


@start_router.callback_query()
async def get_data(call: CallbackQuery):
    print(call.data)