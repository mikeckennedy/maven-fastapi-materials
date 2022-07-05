class Forecast:
    def __init__(self, data):
        loc = data['location']
        forecast = data['forecast']
        w = data['weather']

        self.city = loc["city"]
        self.state = loc["state"]
        self.temp = float(forecast["temp"])
        self.description = w["description"]
