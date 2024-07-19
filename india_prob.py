# word count

with open('INDIA.TXT', 'r') as file:
    content = file.read()
    lst = content.split()
    print("total number of words count : ", len(lst))

counts_india = 0
 
for data in lst:
    if data == "India":
        counts_india += 1

count_india = content.count('India')

count_i = content.count('i')

print(f"number of i count : {count_i}")
print("total number of India count : ", counts_india)







