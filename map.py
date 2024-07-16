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


def add(a, b):

     return b - a
div = [1, 3, 5, 6, 7]

addition = map(add, div)

print(list(addition))

# gfggy


# Define a function to subtract two numbers
def subtract(a, b):
    return b - a

# List of numbers


numbers = [1, 3, 5, 6, 7]

# Use zip to create pairs of consecutive elements
pairs = zip(numbers[:-1], numbers[1:])

# Use map to apply the subtract function to each pair
differences = map(lambda pair: subtract(pair[0], pair[1]), pairs)

# Convert the map object to a list to see the results
print(list(differences))


