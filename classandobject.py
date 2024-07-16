# class and objects 1


class Students:
    """A class representing a student with name, age, and student ID attributes."""

    def __init__(self, name, age, studentid):
        """Initialize the student with name, age, and student ID."""
        self.name = name
        self.age = age
        self.studentid = studentid

    def information(self):
        """Return the student's information as a formatted string."""
        return f"student_name: {self.name}, student_age: {self.age}, student_id: {self.studentid}"


# Creating an instance of the Students class
student_1 = Students("Joy", 14, "205116")
print(student_1.information())


# class and objects 2
class Animal:
    def __init__(self, species, sound):
        self.species = species
        self.sound = sound

    def make_sound(self):
        return f"The {self.species} goes '{self.sound}'"
