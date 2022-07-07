from typing import Optional

import pydantic


class NewUserModel(pydantic.BaseModel):
    name: str
    email: pydantic.EmailStr
    password: Optional[str]
    country: str = pydantic.Field(max_length=3, min_length=2, default='USA')
