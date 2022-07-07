import asyncio

import pymongo.errors

from models import mongo_setup
from models.release import Release
from services import user_service, package_service


async def main():
    await mongo_setup.global_init(database='pypi')
    p = await package_service.get_package_by_id('requests')

    print("--------------------------")
    print(" PyPI CLI ")
    print("--------------------------")
    print()

    pc = await package_service.package_count()
    rc = await package_service.release_count()
    print(f"We have {pc:,} packages with {rc:,} releases.")

    latest = await package_service.latest_packages()
    print("The latest 5 packages are:")
    for p in latest:
        r: Release = package_service.get_latest_release_for_package(p)
        if not r:
            print(f'* {p.id}')
        else:
            print(f'* {p.id:<10} with latest release on {r.created_date.isoformat().replace("T", " ")}')
    print()
    print("Boto package:")
    print(await package_service.get_package_by_id('boto3'))
    print()
    print(f"We have {await user_service.user_count():,} users.")

    print("Let's create one more:")
    while True:
        try:
            name = input("What's there name? ").strip()
            email = name.replace(' ', '-') + '@gmail.com'
            await user_service.create_account(name, email, "a")
            break
        except pymongo.errors.DuplicateKeyError:
            print("Oops, we already have a user with that name, try another.")

    print(f"Now there are {await user_service.user_count():,} users.")
    user = await user_service.get_user_by_email(email)
    print(f"We added {user}!")


async def init_db():
    await mongo_setup.global_init(database='pypi')


if __name__ == '__main__':
    asyncio.run(main())
