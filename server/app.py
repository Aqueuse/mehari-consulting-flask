import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from server.routes import article, news, rubrique, admin

fastapp = FastAPI()

fastapp.mount("/public", StaticFiles(directory="client/public/"), name="public")

fastapp.include_router(article.article_router)
fastapp.include_router(news.news_router)
fastapp.include_router(rubrique.rubrique_router)
fastapp.include_router(admin.admin_router)

os.environ['baseURL'] = "http://mehari-consulting.com:3002/"


@fastapp.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
