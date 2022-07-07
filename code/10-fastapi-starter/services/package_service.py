from typing import List, Optional

from beanie.odm.operators.find.evaluation import RegEx

from models.db.package import Package, PackageTopLevelOnlyView
from models.db.release import Release
from models.db.release_analytics import ReleaseAnalytics


async def release_count() -> int:
    release_info = await ReleaseAnalytics.find_one()
    if not release_info:
        release_info = ReleaseAnalytics()
        await release_info.save()

    return release_info.total_releases


async def package_count() -> int:
    return await Package.count()


async def latest_packages(limit: int = 5, project=False) -> List[Package | PackageTopLevelOnlyView]:
    if not project:
        return await Package.find().sort('-last_updated').limit(limit).to_list()
    else:
        return await Package.find().sort('-last_updated').limit(limit).project(PackageTopLevelOnlyView).to_list()


async def get_package_by_id(package_name: str) -> Optional[Package]:
    package = await Package.find_one(Package.id == package_name)
    return package


async def get_latest_release_for_package_by_name(package_name: str) -> Optional[Release]:
    package = await Package.find_one(Package.id == package_name)
    return get_latest_release_for_package(package)


def get_latest_release_for_package(package: Package) -> Optional[Release]:
    if not package or not package.releases:
        return None

    releases = sorted(package.releases, key=lambda r: (r.major_ver, r.minor_ver, r.build_ver))
    latest = releases[-1]
    return latest


async def search_package_names(keyword: str) -> list[PackageTopLevelOnlyView]:
    if not keyword or not keyword.strip():
        return []

    keyword = keyword.strip().lower()

    return await Package \
        .find(RegEx('_id', f'{keyword}')) \
        .sort('_id') \
        .project(PackageTopLevelOnlyView) \
        .to_list()
