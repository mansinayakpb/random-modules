# error 

def division_num():
    try:
        num1 = int(input("enter the num1:  "))
        num2 = int(input("enter the num2:  "))
        result = num1 / num2
        if num1 < 0 or num2 < 0:
            raise ValueError

    except ZeroDivisionError:
        print("cannot divide with zero... ")
    
    except ValueError:
        print("invalid input... ")

    else:
        print(f"{result}")

    finally:
        print("execute")


division_num()
