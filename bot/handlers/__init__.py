from bot.dispatcher import dp
from bot.handlers.private.payment import order_router
from bot.handlers.start import main_router
from bot.handlers.private.book import book_router

dp.include_routers(*[
    main_router,
    book_router,
    order_router
])
