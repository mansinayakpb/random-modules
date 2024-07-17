import random
import time


class DiceRoll:
    def __init__(self, rounds=10):
        self.rounds = rounds

    def play(self):
        ramesh = random.randint(1, 6)
        suresh = random.randint(1, 6)
        return ramesh, suresh

    def rolldice(self):
        self.ramesh_total = 0
        self.suresh_total = 0
        self.ramesh_win = 0
        self.suresh_win = 0

        print("Ramesh and Suresh are playing 10 rounds:\n")

        for num in range(1, self.rounds + 1):
            ramesh, suresh = self.play()
            self.ramesh_total += ramesh
            self.suresh_total += suresh

            input(f"Press Enter to play round {num}")
            print("Dice rolling..")
            time.sleep(1)  
            print(f"Ramesh - {ramesh}, Suresh - {suresh} ", end="")

            if ramesh == suresh:
                print(f"{num}th round: DRAW")
            elif ramesh > suresh:
                print(f"{num}th round: Ramesh Wins \n")
                self.ramesh_win += 1
            else:
                print(f"{num}th round: Suresh Wins \n")
                self.suresh_win += 1

    def results(self):
        if self.ramesh_win == self.suresh_win:
            print("\nAverage Result: DRAW\n")
        elif self.ramesh_win > self.suresh_win:
            print(
                f"\nRamesh WINS\nWinning Counts are:\nRamesh won {self.ramesh_win} times.\nSuresh won {self.suresh_win} times."
            )
        else:
            print(
                f"\nSuresh WINS\nWinning Counts are:\nRamesh won {self.ramesh_win} times.\nSuresh won {self.suresh_win} times."
            )

        print(f"Ramesh Total Points = {self.ramesh_total}")
        print(f"Suresh Total Points = {self.suresh_total}")


game = DiceRoll()
while True:
    game.rolldice()
    game.results()
        
    ch = input("\nWant to play Again? (Y/N): ")
    if ch.lower() != 'y':
        break
