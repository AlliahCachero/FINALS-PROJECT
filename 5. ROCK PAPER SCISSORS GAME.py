
# ICT 09 – Programming 1

# FINAL PROJECT

# 5. Rock paper scissors game:
# - This game will have a mechanics of best of three (3). The player who won two times is the winner.

import random

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    player_wins = 0
    computer_wins = 0

    while player_wins < 2 and computer_wins < 2:
        player_choice = input("Enter rock, paper, or scissors: ").lower()
        if player_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            player_wins += 1
            print("You win this round!")
        else:
            computer_wins += 1
            print("Computer wins this round!")

    if player_wins == 2:
        print("You won the game!")
    else:
        print("Computer won the game!")

if __name__ == "__main__":
    rock_paper_scissors()