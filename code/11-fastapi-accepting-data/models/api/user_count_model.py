import pydantic


class UserCountModel(pydantic.BaseModel):
    user_count: int
