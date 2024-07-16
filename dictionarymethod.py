# retrieve the value associated with the key 'name' in the dictionary

dictionary = {"name": "Alice", "age": 25}
print(dictionary["name"])

# change the value associated with the key 'age' to 26 in the dictionary

dictionary = {"name": "Alice", "age": 25}
dictionary["age"] = 26
print(dictionary)

# Removing Items: How do you remove the key 'age' from the dictionary

dictionary = {"name": "Alice", "age": 25}
del dictionary["age"]
print(dictionary)

# How do you check if the key 'name' exists in the dictionary

dictionary = {"name": "Alice", "age": 25}
print("name" in dictionary)

# How do you get a list of all keys in the dictionary

dictionary = {"name": "Alice", "age": 25}
print(list(dictionary.keys()))

# How do you get a list of all values in the dictionary
dictionary = {"name": "Alice", "age": 25}
print(list(dictionary.values()))

# How do you remove all items from the dictionary

dictionary = {"name": "Alice", "age": 25}
print(dictionary.clear())

# How do you create a copy of the dictionary

dictionary = {"name": "Alice", "age": 25}
d_copy = dictionary.copy()
print(d_copy)

# How do you get a list of all key-value pairs in the dictionary

dictionary = {"name": "Alice", "age": 25}
print(list(dictionary.items()))

# How do you get the value associated with the key 'gender' in the dictionary
# d = {'name': 'Alice', 'age': 25}, returning 'Unknown' if the key doesn't exist?

dictionary = {"name": "Alice", "age": 25}
print(dictionary.get("gender", "unknown"))

# How do you add the key 'gender' with the value 'Female' to the dictionary if it doesn't already exist?

dictionary = {"name": "Alice", "age": 25}
dictionary["gender"] = "Female"
print(dictionary)

# How do you merge the dictionary
# d2 = {'city': 'New York', 'age': 26} into the dictionary d = {'name': 'Alice', 'age': 25}?

dictionary = {"name": "Alice", "age": 25}
dictionary2 = {"city": "New York", "age": 26}
dictionary.update(dictionary2)
print(dictionary)

# create a dictionary with keys from 1 to 5 and values equal to the square of the keys?

dictionary = {digit: digit**2 for digit in range(1, 6)}
print(dictionary)

# create a dictionary with keys from the list ['a', 'b', 'c'] and all values set to 0?

dictionary = dict.fromkeys(["a", "b", "c"], 0)
print(dictionary)

# remove the key 'age' and return its value from the dictionary

dictionary = {"name": "Alice", "age": 25}
print(dictionary.pop("age"))

# remove and return the last inserted key-value pair from the dictionary

dictionary = {"name": "Alice", "age": 25, "city": "New York"}
last_item = dictionary.popitem()
print(last_item)
print(dictionary)

# print all keys in the dictionary using a for loop

dictionary = {"name": "Alice", "age": 25}
for key in dictionary:
    print(key)

# print all values in the dictionary using a for loop?

ddictionary = {"name": "Alice", "age": 25}
for value in dictionary.values():
    print(value)

# print all key-value pairs in the dictionary using a for loop?

dictionary = {"name": "Alice", "age": 25}
for key, value in dictionary.items():
    print(key, value)

# retrieve the value 'Math' from the nested dictionary

dictionary = {
    "student": {
        "name": "Alice",
        "age": 25,
        "subjects": {"primary": "Math", "secondary": "Science"},
    }
}
dict_2 = dictionary["student"]["subjects"]["primary"]
print(dict_2)

# update the value of 'age' to 26 in the nested dictionary

dictionary = {"student": {"name": "Alice", "age": 25}}
dictionary["student"]["age"] = 26
print(dictionary)

# add a new key 'subjects' with the value {'primary': 'Math', 'secondary': 'Science'}
# to the nested dictionary?

dictionary = {"student": {"name": "Alice", "age": 25}}
dictionary["student"]["subjects"] = {"primary": "Math", "secondary": "Science"}
print(dictionary)

# create a deep copy of the nested dictionary
# 1

dictionary = {
    "student": {
        "name": "Alice",
        "age": 25,
        "subjects": {"primary": "Math", "secondary": "Science"},
    }
}
dictionary_copy = dictionary.copy()
print(dictionary_copy)

# 2

import copy

dictionary = {
    "student": {
        "name": "Alice",
        "age": 25,
        "subjects": {"primary": "Math", "secondary": "Science"},
    }
}
d_copy = copy.deepcopy(dictionary)
print(d_copy)

# How do you create a dictionary where each key's value is a list and
# then append 'Math' to the list associated with the key 'subjects'?

from collections import defaultdict

# Create a defaultdict where each key's value is a list
dictionary = defaultdict(list)
# Append 'Math' to the list associated with the key 'subjects'
dictionary["subjects"].append("Math")
print(dictionary)

# How do you count the frequency of each character in the string 'car' using a dictionary?

vehicle = "car"
freq = {}
for char in vehicle:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

# How do you group the elements of the list ['apple', 'banana', 'pear', 'peach', 'apricot']
# by their first letter using a dictionary?

words = ["apple", "banana", "pear", "peach", "apricot"]
grouped = {}
for word in words:
    key = word[0]
    if key in grouped:
        grouped[key].append(word)
    else:
        grouped[key] = [word]


# positional arguments


def greet(name, age):
    print(f"hello this is {name} and i am {age} year old")


greet("Alice", 36)

# keyword arguments


def greet(name, age):
    print(f"hello this is {name} and i am {age} year old")


greet(age=36, name="Alice")
