# inheritance 
class Car:
    """A class representing a car with make, model, and year attributes."""

    def __init__(self, make, model, year):
        """Initialize the car with make, model, and year."""
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        """Display the car's information."""
        print(f"{self.year} {self.make} {self.model}")


class ElectricCar(Car):
    """A class representing an electric car, inheriting from Car and including battery size."""

    def __init__(self, make, model, year, battery_size):
        """Initialize the electric car with make, model, year, and battery size."""
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def display_battery(self):
        """Display the battery size of the electric car."""
        print(f"Battery size: {self.battery_size}-kWh")


my_electric_car = ElectricCar("Tesla", "Model S", 2021, 100)
my_electric_car.display_info()
my_electric_car.display_battery()

# inheritance 


class Bank:
    def __init__(self, name):
        self.name = name

    def bank_n(self):
        return "bank name"


class BankName(Bank):
    def bank_n(self):
        return f" {self.name} is a bank"


bank_1 = BankName("SBI")
print(bank_1.bank_n())


# inheritance 


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year}, {self.make}, {self.model}")

    def start_engine(self):
        print(f"{self.make}, {self.model}")

    def stop_engine(self):
        print(f"{self.make}, {self.model}")


class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()

    def honk_horn(self):
        print(f"{self.make}, {self.model}")


vehicle = Vehicle("generic", "vehicle", 2020)
vehicle.display_info()
vehicle.start_engine()
vehicle.stop_engine()
print("\n")

car = Car("tesla", "model S", 2021, 4)
car.display_info()
car.start_engine()
car.stop_engine()
car.honk_horn()
