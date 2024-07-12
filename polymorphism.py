#polymorphism 1
class Employee1:
    def work(self):
        return "task1"

class Employee2:
    def work(self):
        return "task2"

def work_completion(company):
    return company.work()

#polymorphism 2
class Bird:
    def fly(self):
        return "Flies in the sky"

class Fish:
    def swim(self):
        return "Swims in the water"

def move(animal):
    if hasattr(animal, 'fly'):
        return animal.fly()
    elif hasattr(animal, 'swim'):
        return animal.swim()

#polymorphism with commoninterface
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

