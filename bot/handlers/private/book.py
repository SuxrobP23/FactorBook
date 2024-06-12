from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InputMediaPhoto
from aiogram.utils.i18n import lazy_gettext as __
from aiogram.utils.i18n import gettext as _
from sqlalchemy import select
from sqlalchemy.orm import Session, Query

from bot.buttons.inline import categories_btn, books_btn
from bot.utils import caption_book
from db.models import Category, Book

book_router = Router()



@book_router.message(F.text == __('📚 Books'))
async def books_handler(message: Message, session: Session) -> None:
    categories: list[Category] = list(session.execute(select(Category)).scalars())
    await message.answer(_('Choose Categories'), reply_markup=categories_btn(categories))


@book_router.callback_query(F.data.startswith('category_'))
async def category_handler(callback: CallbackQuery, session) -> None:
    category_id = int(callback.data.split('_')[1])
    books = session.execute(select(Book).where(Book.category_id == category_id)).scalars()
    await callback.message.edit_text(text = 'Choose Books', reply_markup=books_btn(books))

@book_router.callback_query(F.data.startswith('book_'))
async def book_handler(callback: CallbackQuery, session) -> None:
    value = callback.data.split("_")[1]
    if value == 'back':
        categories: list[Category] = list(session.execute(select(Category)).scalars())
        await callback.message.edit_text(_('Choose Categories'), reply_markup=categories_btn(categories))
    else:
        book_id = int(value)
        book = session.execute(select(Book).where(Book.id == book_id)).scalar()
        await callback.message.delete()
        await callback.message.answer_photo(photo=book.photo_url, caption=caption_book(book))