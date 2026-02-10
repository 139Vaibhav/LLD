class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def StartEngine(self):
        print("Engine Started")

    def StopEngine(self):
        print("Engine Stopped")

class EletricCar(Car):
    def chargeBattery(self):
        print("Battery Charged")

class GasCar(Car):
    def fill_tank(self):
        print("Gas tank filled")

if __name__ == "__main__":
    tesla = EletricCar("Tesla", "Model S")
    ford = GasCar("Ford", "Mustang")

    tesla.StartEngine()
    tesla.chargeBattery()
    tesla.StopEngine()

    ford.StartEngine()
    ford.fill_tank()
    ford.StopEngine()