class Battery:
    def battery_info(self):
        return "Battery is fully charged fully"

class Engine:
     def engine_info(self):
         return "Engine is running"

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

class ElectricCar(Battery, Engine, Car):
    def __init__(self, make, model):
        Car.__init__(self, make, model)

# Create an instance of ElectricCar
c2 = ElectricCar("Tesla", "Model S")

# Call the engine_info method
print(c2.engine_info())
print(c2.battery_info())
