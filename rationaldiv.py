class RationalDiv:

    def __init__(self, num=0, deno=1):
        self.num = num
        self.deno = deno

    def get_value(self):
        self.num = int(input("Enter numerator: "))
        self.deno = int(input("Enter denominator: "))

    def calculate(self, value):
        if type(self) is type(value):
            tem = RationalDiv()
            tem.deno = self.deno * value.num
            tem.num = self.num * value.deno
            return tem

    def show(self, value, tem):
        print(
            f"{self.num}/{self.deno} / {value.num}/{value.deno} = {tem.num}/{tem.deno}"
        )


def menu():
    rational_1 = RationalDiv()
    rational_2 = RationalDiv()
    while True:
        print(
            """
        1. Change Values"
        2. Calculate"
        3. Exit
        
        """
        )

        choice = input("Choose an option: ")

        if choice == "1":
            print("Change values for the first rational number: ")
            rational_1.get_value()
            print("Change values for the second rational number: ")
            rational_2.get_value()
        elif choice == "2":
            result = rational_1.calculate(rational_2)
            rational_1.show(rational_2, result)
        elif choice == "3":
            print("Exiting the program.")
            break
        

menu()
