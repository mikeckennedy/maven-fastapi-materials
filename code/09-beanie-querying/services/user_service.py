from typing import Optional

import bson
from passlib.handlers.sha2_crypt import sha512_crypt as crypto

from models.user import User


async def user_count() -> int:
    return await User.count()


async def create_account(name: str, email: str, password: str) -> User:
    user = User(email=email, name=name)
    user.hash_password = crypto.hash(password, rounds=172_434)

    await user.save()
    return user


async def login_user(email: str, password: str) -> Optional[User]:
    user = await get_user_by_email(email)
    if not user:
        return user

    try:
        if not crypto.verify(password, user.hash_password):
            return None
    except ValueError:
        return None

    return user


async def get_user_by_id(user_id: bson.ObjectId) -> Optional[User]:
    return await User.find_one(User.id == user_id)


async def get_user_by_email(email: str) -> Optional[User]:
    return await User.find_one(User.email == email)
