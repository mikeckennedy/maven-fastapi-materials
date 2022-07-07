import asyncio

from models import mongo_setup


async def main():
    await mongo_setup.global_init()


if __name__ == '__main__':
    asyncio.run(main())
