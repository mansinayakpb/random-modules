# user file

while True:
    take_input = input("Enter text.. ")

    with open("userinput.txt", "a") as file:
        take_input = take_input + "\n"
        file.write(take_input)
    ask_user = input('Do you want to add more content ? (Y/N)')
    if ask_user not in "Yy":
        break
