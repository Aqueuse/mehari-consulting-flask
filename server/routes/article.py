import os
from fastapi import Body, Request, APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from server.database import (
    add_article,
    delete_article,
    retrieve_article,
    update_article,
)
from server.models.article import (
    error_response_model,
    response_model,
    ArticleSchema,
    UpdateArticleModel,
)

templates = Jinja2Templates(directory="client/templates")
article_router = APIRouter()

###### CREATE routes #######
@article_router.get("/create", response_class=HTMLResponse)
async def load_create_article_page(request: Request):
    return templates.TemplateResponse("create_article.html", {"request":request})


@article_router.post("/create", response_description="Article data added into the database")
async def add_article_data(article: ArticleSchema = Body(...)):
    article = jsonable_encoder(article)
    # create ID for the article
    # attribute default thumbail
    # set categorie to null if None
    new_article = await add_article(article)
    return response_model(new_article, "Article added successfully.")


###### LOAD route #######
@article_router.get("/type=article&id={id}", response_description="Article data retrieved", response_class=HTMLResponse)
async def get_article_data(request: Request, id: str):
    result = await retrieve_article(id)
    if result:
        return templates.TemplateResponse("article.html", {"request": request, "result": result, "id": id})
    return error_response_model("An error occurred.", 404, "Article doesn't exist.")


###### EDIT routes #######
@article_router.get("/edit/{id}", response_class=HTMLResponse)
async def load_edit_article_page(request: Request, id: str):
    result = await retrieve_article(id)
    return templates.TemplateResponse("edit_article.html", {
        "request": request,
        "result": result,
        "baseURL": os.environ['baseURL']}
    )


@article_router.put("/{id}")
async def update_article_data(id: str, req: UpdateArticleModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_article = await update_article(id, req)
    if updated_article:
        return response_model(
            "Article with ID: {} name update is successful".format(id),
            "Article name updated successfully",
        )
    return error_response_model(
        "An error occurred",
        404,
        "There was an error updating the article data.",
    )

###### DELETE route #######
@article_router.delete("/{id}", response_description="Article data deleted from the database")
async def delete_article_data(id: str):
    deleted_article = await delete_article(id)
    if deleted_article:
        return response_model(
            "Article with ID: {} removed".format(id), "Article deleted successfully"
        )
    return error_response_model(
        "An error occurred", 404, "Article with id {0} doesn't exist".format(id)
    )
