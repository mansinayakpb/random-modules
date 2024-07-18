# hcf

def get_hcf(num1, num2):
    while (num2 != 0):
        remain = num1 % num2
        num1 = num2
        num2 = remain
    return num1


def simplify(num1, num2):
    hcf = get_hcf(num1, num2)
    simplified_num1 = num1 // hcf
    simplified_num2 = num2 // hcf
    return simplified_num1, simplified_num2, hcf


num1 = int(input("enter the num... "))
num2 = int(input("enter the deno... "))

simplified_num, simplified_deno, hcf = simplify(num1, num2)
print(f"{simplified_num}/{simplified_deno}")

print(f"hcf : {hcf}")

    