import requests

from forecast import Forecast


def get_forecast(city: str, state: str) -> Forecast:
    url = f'https://weather.talkpython.fm/api/weather?city={city}&state={state}&units=imperial'
    resp = requests.get(url)
    resp.raise_for_status()

    # if resp.status_code not in {200, 201}:
    #     raise Exception(f"Error: API call failed with code {resp.status_code}")

    data = resp.json()
    temp = data['forecast']['temp']
    desc = data['weather']['description']
    return Forecast(city, state, int(temp), desc)
