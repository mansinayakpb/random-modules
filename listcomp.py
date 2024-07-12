#squares of the numbers 1 to 10
squares = [digit**2 for digit in range(1, 10)]
print(squares)

#flatten the 2D matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattend = [item for sublist in matrix for item in sublist]
print(flattend)

#palindromic numbers between 1 and 100
palindrome = [num for num in range(1, 100) if str(num) == str(num)[::-1]]
print(palindrome)

#list of words, create a new list contain only the words that start with the letter 'a'
words = ["ant", "apple", "bad", "cross"]
a_word = [word for word in words if word.startswith('a')]
print(a_word)

#