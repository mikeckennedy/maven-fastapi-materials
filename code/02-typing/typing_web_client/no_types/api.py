import requests

from forecast_model import Forecast


def get_weather(city, state):
    city = city.lower().strip()
    state = state.lower().strip()

    url = f'https://weather.talkpython.fm/api/weather?city={city}&state={state}&country=US&units=imperial'
    resp = requests.get(url)
    resp.raise_for_status()

    data = resp.json()
    return Forecast(data)
