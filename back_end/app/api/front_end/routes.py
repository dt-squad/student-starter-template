from fastapi import APIRouter, Request
import os

router = APIRouter()
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates

this_directory = os.path.abspath(os.path.dirname(__file__))
path_to_templates = os.path.join(this_directory, "templates")
templates = Jinja2Templates(directory=path_to_templates)

@router.get("/", response_class=HTMLResponse)
@router.get("/index", response_class=HTMLResponse)
def index(request: Request):
    response = templates.TemplateResponse(
        request, "index.html",
    )
    response.headers["Cache-Control"] = "no-cache"
    return response

# Favicon routes
@router.get("/favicon.png")
@router.get("/favicon.ico")
def favicon():
    favicon_path = os.path.join(this_directory, "templates", "favicon.png")
    return FileResponse(
        favicon_path,
        media_type="image/vnd.microsoft.icon"
    )