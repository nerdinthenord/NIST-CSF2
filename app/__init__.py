from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .config import settings
from .web import router_views


def create_app() -> FastAPI:
    app = FastAPI(title=settings.app_name)

    app.mount("/static", StaticFiles(directory="app/static"), name="static")
    templates = Jinja2Templates(directory="app/templates")
    app.state.templates = templates

    app.include_router(router_views.router)

    return app


app = create_app()
