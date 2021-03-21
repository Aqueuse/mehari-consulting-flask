import os
from fastapi import Body, Request, APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from server.database import retrieve_all_articles

templates = Jinja2Templates(directory="client/templates")
admin_router = APIRouter()


@admin_router.get("/admin")
async def load_admin_page(request: Request):
    search_result = await retrieve_all_articles()
    return templates.TemplateResponse('admin.html', {
        "request": request,
        "search_result": search_result,
        "baseURL": os.environ['baseURL']
    })


# login

# upload