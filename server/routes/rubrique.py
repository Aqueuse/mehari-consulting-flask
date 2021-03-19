from fastapi import APIRouter
from app.server.database import (
    retrieve_articles
)
from app.server.models.article import (
    response_model
)
import app.server.app

router = APIRouter()

@router.get("/all", response_description="Articles retrieved")
async def get_articles():
    articles = await retrieve_articles()
    if articles:
        return app.templates.TemplateResponse(articles, "Articles data retrieved successfully")
    return response_model(articles, "Empty list returned")
