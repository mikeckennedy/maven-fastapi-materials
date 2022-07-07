from models.db.user import User


async def user_count() -> int:
    return await User.count()
