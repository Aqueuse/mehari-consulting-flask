from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from server.routes import article, news

fastapp = FastAPI()

fastapp.mount("/public", StaticFiles(directory="client/public"), name="public")

fastapp.include_router(article.article_router, tags=["Article"])
fastapp.include_router(news.news_router, tags=["News"])


@fastapp.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
