import fastapi
import pymongo.errors
from pydantic import ValidationError

from models.api.package_count_model import PackageCountModel
from models.api.package_model import PackageModel
from models.api.package_search_model import PackageSearchModel
from models.db.package import Package, PackageTopLevelOnlyView
from services import package_service

router = fastapi.APIRouter()


@router.get('/api/packages/count', response_model=PackageCountModel)
async def count_packages():
    count = await package_service.package_count()

    resp = PackageCountModel(package_count=count)
    return resp.dict()


@router.get('/api/packages/details/{package_name}', response_model=PackageModel)
async def package_details(package_name: str):
    try:
        package = await package_service.get_package_by_id(package_name)
        if not package:
            msg = f"Package with name {package_name} was not found."
            return fastapi.Response(content=msg, status_code=404)

        resp = PackageModel.parse_obj(package.dict())
        return resp.dict()

    except ValidationError as ve:
        print(f"We ran into a problem converting DB data to models: {ve}")
        return fastapi.Response(content=str(ve), status_code=500)

    except pymongo.errors.PyMongoError as se:
        print(f"We can't connect to our DB right now: {se}")
        return fastapi.Response(content="We can't connect to our DB right now", status_code=500)

    except Exception as x:
        print(f"General exception: {x}")
        return fastapi.Response(content="Looks like our site is having trouble", status_code=500)


@router.get('/api/packages/search/{keyword}', response_model=PackageSearchModel)
async def package_search(keyword: str) -> dict:
    packages: list[PackageTopLevelOnlyView] = await package_service.search_package_names(keyword)

    package_names = [package.id for package in packages]
    resp = PackageSearchModel(packages=package_names, keyword=keyword)

    return resp.dict()
