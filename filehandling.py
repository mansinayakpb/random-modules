# Read
# read a single line from the file

file = open('file7.txt', 'r')
print(file.readline())

# read all lines into a list where each line is an element

file = open('file7.txt', 'r')
print(file.readlines()) 

# write

file = open('file7.txt', 'w')
file_name = file.write("Hello There!")  # how much long the character is
file.close()

# append

file = open('file7.txt', 'a')
file.write("\n be careful")
file.close()

# with

with open('file7.txt', 'r') as file:
    content = file.read()

# split the words using with statement

with open("file7.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)

