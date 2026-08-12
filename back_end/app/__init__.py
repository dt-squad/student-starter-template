from back_end.app.api.jobs.routes import router as jobs_router
from back_end.app.api.resource.routes import router as resource_router
from back_end.app.api.complaints.routes import router as complaints_router
from back_end.app.api.scaffolds.routes import router as scaffold_router
from back_end.app.api.front_end.routes import router as front_end_router

from fastapi import FastAPI, Request
from fastapi.exceptions import HTTPException
import os
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import ValidationError


def create_app() -> FastAPI:

    app = FastAPI(
    title="job_track",

    )
    # Then mount static files
    this_directory = os.path.abspath(os.path.dirname(__file__))
    static_files_path = os.path.join(
    this_directory, "api", "front_end", "templates", "static"
    )
    template_path = os.path.join(this_directory, "api", "front_end", "templates")
    templates = Jinja2Templates(directory=template_path)
    app.mount("/static", StaticFiles(directory=static_files_path), name="static")

    app.include_router(jobs_router, prefix="/api/jobs")
    app.include_router(complaints_router, prefix="/api/complaints")
    app.include_router(resource_router, prefix="/api/resource")
    app.include_router(scaffold_router, prefix="/api/scaffold")
    app.include_router(front_end_router)
    @app.exception_handler(404)
    def not_found_handler(request: Request, exc: HTTPException):
        return templates.TemplateResponse(
        request, "index.html", status_code=404
    )

    @app.exception_handler(ValidationError)
    async def validation_exception_handler(request: Request, exc: ValidationError):
        return dict(rc=16, message="Improperly formatted response."), 422

    return app