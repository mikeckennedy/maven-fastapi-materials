import datetime

import pydantic

data = {
    "name": "Michael",
    "town": "Portland",
    "location": [45.04, "122.34"]
}


class Person(pydantic.BaseModel):
    name: str
    birthday: datetime.date = pydantic.Field(default_factory=datetime.date.today)
    last_name: str | None
    town: str
    location: list[float]


# p = Person(name=data.get('name'), last_name=data.get('last_name'), ...)
p = Person(**data)

print(p)
