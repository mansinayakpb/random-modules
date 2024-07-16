# random number

import random


def guess_number():
    number_to_guess = random.randint(1, 200)
    attempts = 0

    print("Guess the number between 1 and 200!")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(
                    f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts."
                )
                break

        except ValueError:
            print("Please enter a valid integer.")

        continue_game = (
            input("Do you want to continue guessing? (y/n): ").strip().lower()
        )
        if continue_game != "y":
            print(f"The number was {number_to_guess}. Better luck next time!")
            break


if __name__ == "__main__":
    guess_number()
