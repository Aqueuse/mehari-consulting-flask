import os
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from server.database import retrieve_articles

templates = Jinja2Templates(directory="client/templates")
news_router = APIRouter()


@news_router.get("/infos", response_class=HTMLResponse)
async def get_articles(request: Request):
    brut_result = await retrieve_articles(key="typeIsArticle", value=True)
    search_result = brut_result[0]
    return templates.TemplateResponse('news.html', {
        "request": request,
        "search_result": search_result,
        "index_articles_suivants": brut_result[1],
        "index_articles_precedents": brut_result[2],
        "count_articles": brut_result[3],
        "baseURL": os.environ['baseURL']
    })
