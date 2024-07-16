import random


def play():
    return random.randint(1, 6)


def dice():
    print("please enter")

    player1 = 0
    player2 = 0
    rounds = 10

    for attempt in range(1, rounds + 1):
        print(f"\n rounds {attempt}:")

        # player 1

        player_1 = play()
        print(f"player1 roll {player_1}")
        player1 += player_1

        # player 2

        player_2 = play()
        print(f"player2 roll {player_2}")
        player2 += player_2

        if player1 > player2:
            print("player 1 wins")
        elif player1 < player2:
            print("player 2 wins")
        else:
            print("draw")

    print("final score")
    print(f"player_1 {player1}")
    print(f"player_2 {player2}")
  
    if player1 > player2:
        print("player 1 wins")
    elif player1 < player2:
        print("player 2 wins")
    else:
        print("draw")


dice()
