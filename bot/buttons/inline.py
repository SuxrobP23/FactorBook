from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from db.models import Category, Book


def categories_btn(categories: list[Category]):
    ikb = InlineKeyboardBuilder()
    btns = [InlineKeyboardButton(text=category.name, callback_data=f"category_{category.id}") for category in
            categories]
    btns.append(InlineKeyboardButton(text="🔎 search", switch_inline_query_current_chat=''))
    ikb.add(*btns)
    ikb.adjust(2, repeat=True)
    return ikb.as_markup()


def books_btn(books: list[Book]):
    ikb = InlineKeyboardBuilder()
    btns = [InlineKeyboardButton(text=book.title, callback_data=f"book_{book.id}") for book in books]
    btns.append(InlineKeyboardButton(text="🔎 search", switch_inline_query_current_chat=''))
    btns.append(InlineKeyboardButton(text="🔙 Back", callback_data='book_back'))
    ikb.add(*btns)
    ikb.adjust(2, repeat=True)
    return ikb.as_markup()
