import asyncio
from typing import Optional

import beanie
import motor.motor_asyncio

from models import core_models


async def global_init(server='localhost', port=27017, username=None, password=None, use_ssl=False):
    server = server or 'localhost'
    port = port or 27017

    await _motor_init(db='pypi', password=password, port=port, server=server,
                      use_ssl=use_ssl, username=username, models=core_models.all_db_models)


async def _motor_init(db: str, password: Optional[str], port: int, server: str,
                      use_ssl: bool, username: Optional[str], models):
    conn_string = get_connection_string(password, port, server, use_ssl, username)
    print(f'Initializing motor connection for db {db} on {server}:{port}')
    print(f'Connection string: {conn_string.replace(password or "NO_PASSWORD", "***********")}')

    # Crete Motor client
    loop = asyncio.get_running_loop()
    client = motor.motor_asyncio.AsyncIOMotorClient(conn_string, io_loop=loop)

    # Init beanie with the Product document class
    await beanie.init_beanie(database=client[db], document_models=models)
    print(f"Init done for db {db}")


def get_connection_string(password, port, server, use_ssl, username):
    if username or password:
        use_ssl = str(use_ssl).lower()
        return f"mongodb://{username}:{password}@{server}:{port}/?authSource=admin&tls={use_ssl}&tlsInsecure=true"
    else:
        return f"mongodb://{server}:{port}"
