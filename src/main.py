from fastapi import FastAPI

from src.common.containers import Container
from src.routes import routers


def create_app() -> FastAPI:
    container = Container()

    try:
        database = container.db()
        database.create_database()
    except Exception as ex:
        print(ex)

    app = FastAPI()
    app.container = container
    for router in routers:
        app.include_router(router=router)

    return app


app = create_app()
