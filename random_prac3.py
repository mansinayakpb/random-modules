import random

def random_unique(n, start, end):
    return random.sample(range(start, end + 1), n)

print(random_unique(5, 1, 20))

#a function that generates a list of n unique random numbers between a given range start and end.