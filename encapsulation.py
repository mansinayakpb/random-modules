#Encapsulation 1

class School:
    """Represents a school with a name and type."""

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def get_name(self):
        """Returns the name of the school."""
        return self.name
    
    def get_type(self):
        """Returns the type of the school."""
        return self.type

school_1 = School("DPS", "Higher Secondary")
print(school_1.get_name())
print(school_1.get_type())

#Encapsulation 2

class BankAccount:
    def __init__(self, owner, balance=0):
        self.__owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdraw amount.")

    def get_balance(self):
        return self.__balance

#Encapsulation 3
class Book:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author
        self.__is_checked_out = False

    def check_out(self):
        if not self.__is_checked_out:
            self.__is_checked_out = True
        else:
            print("The book is already checked out.")

    def return_book(self):
        if self.__is_checked_out:
            self.__is_checked_out = False
        else:
            print("The book is not checked out.")

    def is_checked_out(self):
        return self.__is_checked_out

    def get_details(self):
        return f"Title: {self.__title}, Author: {self.__author}, Checked Out: {self.__is_checked_out}"
