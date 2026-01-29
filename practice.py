class car:
    def __init__(self, brand, model):
        self._brand = brand
        self._model = model
        self._speed = 0

    def accelerate(self, increment):
        self._speed += increment

    def display_status(self):
        print(f"{self._brand} is running at {self._speed} km/h")