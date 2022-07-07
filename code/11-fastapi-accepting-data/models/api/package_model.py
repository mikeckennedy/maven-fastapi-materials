import datetime
from typing import Optional

import pydantic

from models.db.release import Release


class PackageModel(pydantic.BaseModel):
    id: str
    created_date: datetime.datetime
    last_updated: datetime.datetime
    summary: Optional[str]
    description: Optional[str]

    home_page: Optional[str]
    docs_url: Optional[str]
    package_url: Optional[str]

    author_name: Optional[str]
    author_email: Optional[str]

    license: Optional[str]
    releases: list[Release]
