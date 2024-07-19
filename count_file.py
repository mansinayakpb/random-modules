

with open('countchar.txt', 'r') as file:
    content = file.read()

vowels = "aieouAIEOU"
digits = "0123456789"
special_char = "@#_."
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

vowels_count = 0
digits_count = 0
special_count = 0
consonant_count = 0

for char in content:
    if char in vowels:
        vowels_count += 1
    elif char in digits:
        digits_count += 1
    elif char in special_char:
        special_count += 1
    elif char in consonants:
        consonant_count += 1

# Total character count
total_char_count = len(content)

# Print the results
print(f"VOWELS Count: {vowels_count}")
print(f"CONSONANTS Count: {consonant_count}")
print(f"DIGITS Count: {digits_count}")
print(f"SPECIAL CHARS Count: {special_count}")
print(f"TOTAL CHAR Count: {total_char_count}")
