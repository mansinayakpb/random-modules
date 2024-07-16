import random
import string


def random_pw(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for i in range(length))


print(random_pw(14))

# a function that generates a random password of a given length. The password should include uppercase, lowercase, digits, and special characters.
