import asyncio
from asyncio import AbstractEventLoop

import bs4
import httpx

from colorama import Fore


def main():
    # Create loop
    loop = asyncio.new_event_loop()
    loop.run_until_complete(get_title_range(loop))
    print("Done.")


async def get_html(episode_number: int) -> str:
    print(Fore.YELLOW + f"Getting HTML for episode {episode_number}", flush=True)

    url = f'https://talkpython.fm/{episode_number}'
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, follow_redirects=True)
        resp.raise_for_status()

        return resp.text


def get_title(html: str, episode_number: int) -> str:
    print(Fore.CYAN + f"Getting TITLE for episode {episode_number}", flush=True)
    soup = bs4.BeautifulSoup(html, 'html.parser')
    header = soup.select_one('h1')
    if not header:
        return "MISSING"

    return header.text.strip()


async def get_title_range(loop: AbstractEventLoop):
    # Please keep this range pretty small to not DDoS my site. ;)
    tasks = []
    for n in range(350, 368):
        tasks.append((loop.create_task(get_html(n)), n))

    for task, n in tasks:
        html = await task
        title = get_title(html, n)
        print(Fore.WHITE + f"Title found: {title}", flush=True)


if __name__ == '__main__':
    main()
