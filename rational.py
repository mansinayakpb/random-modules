class RationalAdd:

    def __init__(self, num=0, deno=1):
        self.num = num
        self.deno = deno

    def get_value(self):
        self.num = int(input("enter numerator : "))
        self.deno = int(input("enter denominator : "))

    def calculate(self, value):
        if type(self) == type(value):
            tem = RationalAdd()
            tem.deno = self.deno * value.deno
            tem.num = self.num * value.deno + value.num * self.deno

        return tem

    def show(self, value, tem):
        print(self.num, "/",self.deno,"+",value.num,"/",value.deno,"=",tem.num,"/",tem.deno,)


rational_1 = RationalAdd()
rational_2 = RationalAdd()
rational_1.get_value()
rational_2.get_value()
result = rational_1.calculate(rational_2)
rational_1.show(rational_2, result)
