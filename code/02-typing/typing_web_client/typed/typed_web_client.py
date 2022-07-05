from typing import Optional

import api
from forecast_model import Forecast


def main():
    data: Optional[Forecast] = api.get_weather('Portland', 'OR')
    if data:
        report_weather(data)

    data = api.get_weather('Boston', 'MA')
    if data:
        report_weather(data)


def report_weather(f: Forecast):
    print(f'Weather in {f.city}, {f.state} is {f.temp}f and {f.description}.')


# OG dictionary version.
# def report_weather(data):
#     loc = data['location']
#     forecast = data['forecast']
#     w = data['weather']
#     msg = f'Weather in {loc["city"]}, {loc["state"]} ' \
#           f'is {forecast["temp"]}f and {w["description"]}.'
#     print(msg)


if __name__ == '__main__':
    main()
