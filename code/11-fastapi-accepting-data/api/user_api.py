import json

import fastapi
import pymongo.errors
from starlette.responses import JSONResponse

from models.api.new_user_model import NewUserModel
from models.api.user_count_model import UserCountModel
from services import user_service

router = fastapi.APIRouter()


@router.get('/api/users/count', response_model=UserCountModel)
async def count_users():
    count = await user_service.user_count()

    resp = UserCountModel(user_count=count)
    return resp.dict()


@router.post('/api/users')
async def create_user(new_user: NewUserModel):
    try:
        await user_service.create_account(
            name=new_user.name, email=new_user.email, password=new_user.password)

        return JSONResponse(content={'created': True}, status_code=201)
    except pymongo.errors.DuplicateKeyError:
        msg = f"Cannot create a user with email {new_user.email}, one already exists."
        return JSONResponse(content={'error': msg}, status_code=409)
