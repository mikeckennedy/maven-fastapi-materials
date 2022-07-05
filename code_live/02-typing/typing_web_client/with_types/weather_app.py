import api


def main():
    print("Hello weather app")
    city = 'Boston'
    report = api.get_forecast(city, "MA")

    print(f"The weather in {city} is {report.desc} and {report.temp}F.")


if __name__ == '__main__':
    main()
