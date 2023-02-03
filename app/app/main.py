from fastapi import FastAPI

from app.handler import get_people


def create_app() -> FastAPI:
    app = FastAPI(title="Job Test")
    app = setup_routes(app)
    return app


def setup_routes(app: FastAPI) -> FastAPI:
    app.router.add_api_route(
        path="/people", endpoint=get_people, methods=["GET"], status_code=200
    )
    return app
