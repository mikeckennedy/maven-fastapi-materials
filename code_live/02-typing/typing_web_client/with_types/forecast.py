class Forecast:

    def __init__(self, city: str, state: str, temp: int, desc: str):
        self.desc: str = desc
        self.temp: int = temp
        self.city: str = city
        self.state: str = state
