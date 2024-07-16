##  append()
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)

# extend()
my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)

# insert()
my_list = [1, 2, 3]
my_list.insert(1, "a")
print(my_list)

# remove()
my_list = [1, 2, 3, 2]
my_list.remove(2)
print(my_list)

# pop()
my_list = [1, 2, 3]
poped_element = my_list.pop()
print(poped_element)
print(my_list)

# clear()
my_list = [1, 2, 3]
my_list.clear()
print(my_list)

# index()
my_list = [1, 2, 3, 2]
index = my_list.index(2)
print(index)

# count()
my_list = [1, 2, 3, 2]
count = my_list.count(2)
print(count)

# sort()
my_list = [3, 1, 2]
my_list.sort()
print(my_list)

# reverse()
my_list = [1, 2, 3]
my_list.reverse()
print(my_list)

# copy()
my_list = [1, 2, 3]
new_list = my_list.copy()
print(new_list)
