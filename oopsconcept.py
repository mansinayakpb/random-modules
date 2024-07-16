# oops concept

class Base:
    def __init__(self):
        self.public = "public"
        self.private = "private"
        self.protected = "protected"


class Derived(Base):
    def access_base_variables(self):
        return (self.public, self.private, self.protected)


objective = Derived()
print(objective.access_base_variables())

# how can you modify ClassC to access the protected variable _y from ClassA


class ClassA:
    def __init__(self):
        self._y = 10


class ClassB(ClassA):
    pass


class ClassC(ClassB):
    def access_protected(self):
        return self._y


objective = ClassC()
print(objective.access_protected())

# How can you modify the Derived class to include a method that prints all variables (public, _protected, __private) from the Base class?


class Base:
    def __init__(self):
        self.public = "public"
        self.private = "private"
        self.protected = "protected"


class Derived(Base):
    def print_all(self):
        return (self.public, self.private, self.protected)


objective = Derived()
print(objective.print_all())
