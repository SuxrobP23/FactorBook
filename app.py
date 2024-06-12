import uvicorn
from sqlalchemy import create_engine
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
from starlette_admin.contrib.sqla import Admin, ModelView

from db.config import engine
from db.models import User, Category, Book
from routes import UsernameAndPasswordProvider

middleware = [
    Middleware(SessionMiddleware, secret_key=None)
]

app = Starlette(middleware=middleware)

logo_url = 'https://fiverr-res.cloudinary.com/images/q_auto,f_auto/gigs/346993714/original/d524eed3a6df4f37fe7e5f81d4c717b601117736/do-telegram-bot-with-python-aiogram.png'
admin = Admin(
    engine=engine,
    title="Aiogram Web Admin",
    logo_url=logo_url,
    auth_provider=UsernameAndPasswordProvider(),
    middlewares=middleware
)


# Create admin

# Add view
admin.add_view(ModelView(User))
admin.add_view(ModelView(Category))
admin.add_view(ModelView(Book))

# Mount admin to your app
admin.mount_to(app)
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8080)

