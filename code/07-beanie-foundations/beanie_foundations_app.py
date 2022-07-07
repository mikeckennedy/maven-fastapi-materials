import asyncio

from models import mongo_setup


async def main():
    await mongo_setup.global_init(database='beanie_foundations')


if __name__ == '__main__':
    asyncio.run(main())
