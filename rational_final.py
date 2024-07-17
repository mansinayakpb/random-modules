class RationalAdd:

    def __init__(self, num=0, deno=1):
        self.num = num
        self.deno = deno

    def get_value(self):
        self.num = int(input("Enter numerator: "))
        self.deno = int(input("Enter denominator: "))

    def add(self, value):
        if type(self) is type(value):
            tem = RationalAdd()
            tem.deno = self.deno * value.deno
            tem.num = self.num * value.deno + value.num * self.deno
            return tem

    def subtract(self, value):
        if type(self) is type(value):
            tem = RationalAdd()
            tem.deno = self.deno * value.deno
            tem.num = self.num * value.deno - value.num * self.deno
            return tem

    def multiply(self, value):
        if type(self) is type(value):
            tem = RationalAdd()
            tem.num = self.num * value.num
            tem.deno = self.deno * value.deno
            return tem

    def divide(self, value):
        if type(self) is type(value):
            tem = RationalAdd()
            tem.num = self.num * value.deno
            tem.deno = self.deno * value.num
            return tem

    def show(self, operator, value, result):
        print(
            f"{self.num}/{self.deno} {operator} {value.num}/{value.deno} = {result.num}/{result.deno}"
        )


def operation_menu(rational_1, rational_2, operation):
    while True:
        print("\n1. Change Values\n2. Calculate\n3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            print("Change values for the first rational number: ")
            rational_1.get_value()
            print("Change values for the second rational number: ")
            rational_2.get_value()
        elif choice == "2":
            if operation == "add":
                result = rational_1.add(rational_2)
            elif operation == "subtract":
                result = rational_1.subtract(rational_2)
            elif operation == "multiply":
                result = rational_1.multiply(rational_2)
            elif operation == "divide":
                result = rational_1.divide(rational_2)
            rational_1.show(operation, rational_2, result)
        elif choice == "3":
            print("Returning to main menu.")
            break


def menu():
    rational_1 = RationalAdd()
    rational_2 = RationalAdd()
    while True:
        print(
            "\n1. Rational Addition\n2. Rational Subtraction\n3. Rational Multiplication\n4. Rational Division\n5. Exit"
        )
        choice = input("Choose an option: ")

        if choice == "1":
            operation_menu(rational_1, rational_2, "add")
        elif choice == "2":
            operation_menu(rational_1, rational_2, "subtract")
        elif choice == "3":
            operation_menu(rational_1, rational_2, "multiply")
        elif choice == "4":
            operation_menu(rational_1, rational_2, "divide")
        elif choice == "5":
            print("Exiting the program.")
            break


menu()
