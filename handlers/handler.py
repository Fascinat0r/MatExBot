from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

import messages

router = Router()


@router.message(Command("start"))
async def cmd_start(msg: Message):
    await msg.answer(messages.get("greeting", msg.from_user.language_code))


@router.message(Command("help"))
async def cmd_help(msg: Message):
    await msg.answer(messages.get("help_message", msg.from_user.language_code))
