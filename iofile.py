# convert uppercase txt file to lowercase txt file


with open('input.txt', 'w') as file:
    file.write("hello there")
with open('input.txt', 'r') as file:
    txt = file.read()
var = txt.upper()
print(var)
with open('input.txt', 'w') as file:
    file.write(var)
lowercase_data = txt.lower()
with open('output.txt', 'w') as outfile:
    outfile.write(lowercase_data)







