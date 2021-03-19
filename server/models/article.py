from typing import Optional

from pydantic import BaseModel, Field


class ArticleSchema(BaseModel):
    title: str = Field(...)
    content: str = Field(...)
    date: str = Field(...)
    typeIsArticle: bool = Field(...)
    categorie: str = Field(...)
    id: str = Field(...)


class UpdateArticleModel(BaseModel):
    title: Optional[str]
    content: Optional[str]
    date: Optional[str]
    typeIsArticle: Optional[bool]
    categorie: Optional[str]
    id: Optional[str]


def response_model(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def error_response_model(error, code, message):
    return {"error": error, "code": code, "message": message}
