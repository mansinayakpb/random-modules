# operator overloading
class RationalNum:

    def __init__(self, num=0, deno=1):
        self.num = num
        self.deno = deno

    def get_value(self):
        self.num = int(input("Enter numerator: "))
        self.deno = int(input("Enter denominator: "))

    def __add__(self, value):
        if type(self) is type(value):
            tem = RationalNum()
            tem.deno = self.deno * value.deno
            tem.num = self.num * value.deno + value.num * self.deno
            return tem

    def __sub__(self, value):
        if type(self) is type(value):
            tem = RationalNum()
            tem.deno = self.deno * value.deno
            tem.num = self.num * value.deno - value.num * self.deno
            return tem

    def __mul__(self, value):
        if type(self) is type(value):
            tem = RationalNum()
            tem.num = self.num * value.num
            tem.deno = self.deno * value.deno
            return tem

    def __truediv__(self, value):
        if type(self) is type(value):
            tem = RationalNum()
            tem.num = self.num * value.deno
            tem.deno = self.deno * value.num
            return tem

    def get_hcf(self, num1, num2):

        while num2 != 0:
            remain = num1 % num2
            num1 = num2
            num2 = remain

        return num1

    def simplify(self, num1, num2):
        hcf = self.get_hcf(num1, num2)
        return num1 // hcf, num2 // hcf

    def show(self, operator, value, result):
        self.num, self.deno = self.simplify(self.num, self.deno)
        value.num, value.deno = self.simplify(value.num, value.deno)
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
                result = rational_1 + rational_2
            elif operation == "subtract":
                result = rational_1 - rational_2
            elif operation == "multiply":
                result = rational_1 * rational_2
            elif operation == "divide":
                result = rational_1 / rational_2
            rational_1.show(operation, rational_2, result)
        elif choice == "3":
            print("Returning to main menu.")
            break


def menu():
    rational_1 = RationalNum()
    rational_2 = RationalNum()
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
