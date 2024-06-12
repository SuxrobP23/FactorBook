from aiogram import html, Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup
from aiogram.utils.i18n import gettext as _
from sqlalchemy import select, insert
from sqlalchemy.orm import Session
from aiogram.utils.i18n import lazy_gettext as __
from bot.buttons.reply import main_button
from db.models import User
main_router = Router()


@main_router.message(CommandStart())
async def command_start_handler(message: Message, session: Session) -> None:
    is_exists = session.execute(select(User).where(User.user_id == message.from_user.id)).scalar()
    if not is_exists:
        user = {
            "user_id": message.from_user.id,
            "username": message.from_user.username,
            "full_name": message.from_user.full_name
        }
        session.execute(insert(User).values(**user))
        session.commit()
    await message.answer(text = "{} {}".format(_('Hello'),message.from_user.full_name) , reply_markup=main_button())
@main_router.message(F.text == __('🇺🇿/🇬🇧 Language'))
async def language_handler(message: Message, session: Session) -> None:
    if message.text == __('��🇿/🇬🇧 Language'):
        await message.answer(text = "🇺🇿/��🇧 Language", reply_markup=main_button())
