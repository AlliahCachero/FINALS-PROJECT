
# ICT 09 – Programming 1

# FINAL PROJECT

# 6. Dice rolling simulator:
# - Create a game of dice rolling. This game should have 2 players and each player should be
#   able to roll a dice (this should only use random number representing the dice). The game
#   will have a best of three (3) mechanics, meaning the player who won 2 of the three
#   instances is the winner.

import random

def dice_rolling_game():
    player1_wins = 0
    player2_wins = 0

    for _ in range(3):
        player1_roll = random.randint(1, 6)
        player2_roll = random.randint(1, 6)
        print(f"Player 1 rolled: {player1_roll}")
        print(f"Player 2 rolled: {player2_roll}")

        if player1_roll > player2_roll:
            player1_wins += 1
            print("Player 1 wins this round!")
        elif player2_roll > player1_roll:
            player2_wins += 1
            print("Player 2 wins this round!")
        else:
            print("It's a tie!")

    if player1_wins > player2_wins:
        print("Player 1 wins the game!")
    else:
        print("Player 2 wins the game!")

if __name__ == "__main__":
    dice_rolling_game()
