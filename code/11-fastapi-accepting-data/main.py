import fastapi
import uvicorn
from starlette.staticfiles import StaticFiles

from api import package_api
from api import user_api
from models.db import mongo_setup
from views import home

api = fastapi.FastAPI()
api.mount("/static", StaticFiles(directory="static"), name="static")


def main():
    print('Setting up FastAPI app (accepting data)')

    init_routes()

    # noinspection PyTypeChecker
    uvicorn.run(api)


@api.on_event("startup")
async def startup_event():
    # Must be done within the context of FastAPIs event loop
    await mongo_setup.global_init(database='pypi')


def init_routes():
    api.include_router(package_api.router)
    api.include_router(user_api.router)
    api.include_router(home.router)


if __name__ == '__main__':
    main()
else:
    init_routes()
