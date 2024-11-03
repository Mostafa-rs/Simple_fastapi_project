from fastapi import FastAPI

from accounts.urls import router as accounts_router
from posts.urls import router as posts_router
from db import create_db_and_tables

app = FastAPI()


@app.on_event('startup')
def on_startup():
    create_db_and_tables()


app.include_router(accounts_router, prefix='/accounts')
app.include_router(posts_router, prefix='/posts')
