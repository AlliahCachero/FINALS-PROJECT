
# ICT 09 – Programming 1

# FINAL PROJECT

# 1. Number guessing game:
# Number-guessing game written in Python. The basic idea is to have the computer produce a
# random number between 1 and 100 and then have the user try to guess it. If the user
# guesses correctly, they win! If not, the computer tells them whether their guess was too
# high or too low, and they get another chance.

import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    guess = None
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("Guess a number between 1 and 100")

    while guess != number_to_guess:
        guess = int(input("Please enter your guess: "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again!")
        elif guess > number_to_guess:
            print("Too high! Try again!")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")

if __name__ == "__main__":
    number_guessing_game()
