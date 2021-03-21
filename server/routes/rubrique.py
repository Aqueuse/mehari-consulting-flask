import os
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from server.database import (
    retrieve_articles
)
from server.models.article import (
    response_model
)

templates = Jinja2Templates(directory="client/templates")
rubrique_router = APIRouter()


@rubrique_router.get("/type=rubrique&name={name}", response_description="Article data retrieved", response_class=HTMLResponse)
async def get_article_data(request: Request, name: str):
    brut_result = await retrieve_articles(key="categorie", value=name)
    search_result = brut_result[0]
    return templates.TemplateResponse('rubrique.html', {
        "request": request,
        "search_result": search_result,
        "index_articles_suivants": brut_result[1],
        "index_articles_precedents": brut_result[2],
        "count_articles": brut_result[3],
        "baseURL": os.environ['baseURL']
    })