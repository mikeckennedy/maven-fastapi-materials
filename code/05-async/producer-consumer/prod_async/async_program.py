import asyncio
import datetime
from asyncio import AbstractEventLoop

import colorama
import random


async def main():
    t0 = datetime.datetime.now()
    print(colorama.Fore.WHITE + "App started.", flush=True)

    data = asyncio.Queue()  # maybe a better data structure?

    # Run these with asyncio.gather()

    task = asyncio.gather(
        generate_data(10, data),
        generate_data(10, data),
        process_data(5, data),
        process_data(5, data),
        process_data(5, data),
        process_data(5, data)
    )

    await task

    dt = datetime.datetime.now() - t0
    print(colorama.Fore.WHITE + f"App exiting, total time: {dt.total_seconds():,.2f} sec.", flush=True)


async def generate_data(num: int, data: asyncio.Queue):
    for idx in range(1, num + 1):
        item = idx * idx
        # Use queue
        work = (item, datetime.datetime.now())
        # data.append(work)
        await data.put(work)

        print(colorama.Fore.YELLOW + f" -- generated item {idx}", flush=True)
        # Sleep better
        # time.sleep(random.random() + .5)
        await asyncio.sleep(random.random() + .5)


async def process_data(num: int, data: asyncio.Queue):
    processed = 0
    while processed < num:
        # Use queue
        # item = data.pop(0)
        # if not item:
        #     time.sleep(.01)
        #     continue
        item = await data.get()
        # item is a tuple

        processed += 1
        value = item[0]
        t = item[1]
        dt = datetime.datetime.now() - t

        print(colorama.Fore.CYAN +
              f" +++ Processed value {value} after {dt.total_seconds():,.2f} sec.", flush=True)
        # Sleep better
        # time.sleep(.5)
        # await asyncio.sleep(.05)


if __name__ == '__main__':
    # Create the asyncio loop
    loop: AbstractEventLoop = asyncio.new_event_loop()
    loop.run_until_complete(main())
