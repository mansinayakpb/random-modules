# map 1

def mapping(number):
    return number * number


numbers = [1, 2, 3, 4, 5]

square_the_numbers = map(mapping, numbers)

print(list(square_the_numbers))

# map 2


def cube(number):
    return number + number


addition = [1, 2, 3, 4, 5]

add_the_number = map(cube, addition)

print(list(add_the_number))

# map 3


def func(num):
    return num - num


subtract = [1, 3, 4, 5, 7]

subtract_num = map(func, subtract)

print(list(subtract_num))

# map 4


def division(num):
    return num // num


divide = [3, 5, 7, 8, 4]

divided = map(division, divide)

print(list(divided))

# map 5


def mapping(num):
    return num**2


number = [1, 2, 3, 4, 5]

define = map(mapping, number)

square_the_value = list(define)
print(square_the_value)

# map 6

integers = ["1", "2", "3", "4", "5"]

convert = map(int, integers)

lists = list(convert)
print(lists)

# lambda

digit = lambda num: num + 10
print(digit(5))

# lambda 1

digit = lambda num: num - 10
print(digit(5))

# lambda 2 

digit = lambda num1, num2: num1 * num2
num1 = int(input("enter the num1...  "))
num2 = int(input("enter the num2...  "))
print(digit(num1, num2))

# lambda 3

digit = lambda num1, num2: num1 / num2
num1 = int(input("enter the num1..  "))
num2 = int(input("enter the num2..  "))
print(digit(num1, num2))

# map and lambda

numbers = [1, 2, 3, 4, 5]
squared_the_values = map(lambda num: num**2, numbers)
print(list(squared_the_values))

# filter even


def is_even(num):
    return num % 2 == 0


numbers = [1, 2, 3, 4, 5]
filter_out = filter(is_even, numbers)

print(list(filter_out))

# filter odd


def is_odd(num):
    return num % 2 != 0


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filter_out = filter(is_odd, numbers)

print(list(filter_out))


# filter out squared even number


number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filter_out = map(lambda num: num**2, filter(lambda num: num % 2 == 0, number))

print(list(filter_out))

# take input from user


def get_input():
    user_input = input("enter numbers separated by spaces  ")
    return list(map(int, user_input.split()))


def squared(num):
    return num ** 2


def is_even(num):
    return num % 2 == 0


numbers = get_input()

squared_num = map(squared, numbers)

filter_even = filter(is_even, squared_num)

print(list(filter_even))
