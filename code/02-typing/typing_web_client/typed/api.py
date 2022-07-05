from typing import Any

import requests

from forecast_model import Forecast


# def get_weather(city: str, state: int) -> dict[str, Any]:
def get_weather(city: str, state: str) -> Forecast | None:
    city = city.lower().strip()
    state = state.lower().strip()

    url = f'https://weather.talkpython.fm/api/weather?city={city}&state={state}&country=US&units=imperial'
    resp = requests.get(url)
    try:
        resp.raise_for_status()
    except Exception as x:
        print(f"Error calling API: {x}")
        return None

    data = resp.json()
    return Forecast(data)
