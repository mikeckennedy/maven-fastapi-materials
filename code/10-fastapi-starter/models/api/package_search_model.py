import pydantic


class PackageSearchModel(pydantic.BaseModel):
    packages: list[str]
    keyword: str
