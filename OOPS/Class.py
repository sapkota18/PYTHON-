class Car:
    
    total_car=0
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model =model
        Car.total_car+=1
    
    def get_brand(self):
        return self.__brand +"!"
    
    def name(self):
        return f"{self.__brand} {self.__model}"
    
    def fule_type(self):
        return "petrol or Disel"
    
    
    @staticmethod
    def general_description():
        return "Cars are good"
    
    
    @property
    def model(self):
        return self.__model
        
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def name(self):
        return f"{super().name()} with a {self.battery_size} battery"
    
    def fule_type(self):
       return "Electric charge"

My_tesla = ElectricCar("Tesla", "X", "85kWh")
safari =Car("tata","safari")
print(isinstance(My_tesla,Car))
# print(My_tesla.name())
# # print(My_tesla.__brand)
# print(My_tesla.get_brand())
# print(safari.model)
# print(safari.fule_type())
# print(My_tesla.fule_type())
# print(Car.total_car)
# print(safari.general_description())
# print(My_tesla.general_description())
# print(My_tesla.model())

