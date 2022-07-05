from pprint import pprint

import api


def main():
    print("Hello weather app")
    city = 'Boston'
    report = api.get_forecast(city, 'MA')

    print(f"The weather in {city} is {report.desc} and {int(report.temp)}F.")


if __name__ == '__main__':
    main()
