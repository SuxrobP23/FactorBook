
from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery
from aiogram.utils.i18n import gettext as _

from utils.conf import Config as conf


order_router = Router()

@order_router.message(Command('invoice'))
async def invoice(message: Message):
    prices = [
        LabeledPrice(label='Iphone 15 pro', amount=1000*1 * 100),
        LabeledPrice(label='Iphone 14 pro', amount=2000*1 * 100)
    ]
    await message.answer_invoice(_('Products'), "Jami 3 product order qilindi", '1', conf.bot.PAYMENT_CLICK_TOKEN,'UZS',prices= prices)

@order_router.pre_checkout_query()
async def success_handler(pre_checkout_query: PreCheckoutQuery) -> None:
    await pre_checkout_query.answer(True)

@order_router.message(lambda message: bool(message.successful_payment))
async def confirm_handler(message: Message, state: FSMContext):
    if message.successful_payment:
        total_amount = message.successful_payment.total_amount//100
        order_id = int(message.successful_payment.invoice_payload)
        # await Order.update(id_=order_id, status=Order.OrderStatusEnum.APPROVED , total_amount = total_amount)
        await message.answer(text=f"To'lo'vingiz uchun raxmat 😊 \n{total_amount}\n{order_id}")



