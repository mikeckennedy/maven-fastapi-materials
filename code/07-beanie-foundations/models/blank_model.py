import datetime
from typing import Optional

import beanie
import pydantic
import pymongo


class Blank(beanie.Document):
    name: str
    created_date: datetime.datetime = pydantic.Field(default_factory=datetime.datetime.now)

    class Collection:
        name = "blank_test"
        indexes = [
            pymongo.IndexModel(keys=[("name", pymongo.ASCENDING)], name="name_ascend", unique=True),
        ]
