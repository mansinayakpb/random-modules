class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size
    
    
    def display_battery(self):
        print(f"Battery size: {self.battery_size}-kWh")

my_electric_car = ElectricCar("Tesla", "Model S", 2021, 100)
my_electric_car.display_info()
my_electric_car.display_battery()


