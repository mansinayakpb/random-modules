# number_1 = int(input("enter the number... "))
# number_1 = int(input("enter the number... "))
# number_2 = int(input("enter the other number... "))

# if number_2 > number_1:
#     minimum = number_1

# else:
#     minimum = number_2

p = int(input("enter the number... "))
q = int(input("enter the number... "))

while (q != 0):

    r = p % q
    p = q
    q = r

print(p)
print(q)
print(r)

    