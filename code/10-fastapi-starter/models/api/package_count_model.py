import pydantic


class PackageCountModel(pydantic.BaseModel):
    package_count: int
