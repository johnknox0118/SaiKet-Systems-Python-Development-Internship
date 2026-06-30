"""
SaiKet Systems - Python Development Internship
Task 2: Guess the Number Game

Description:
The program generates a random number within a given range, and the user
has to guess it. Hints (higher/lower) are given after each guess, and the
number of attempts is tracked.

Skills demonstrated: Basic Python Programming, Random Number Generation,
Conditional Statements, Loops
"""

import random


def play_game(lower=1, upper=100):
    secret_number = random.randint(lower, upper)
    attempts = 0

    print("\n===== GUESS THE NUMBER GAME =====")
    print(f"I'm thinking of a number between {lower} and {upper}.")
    print("Try to guess it!\n")

    while True:
        guess_input = input("Enter your guess: ").strip()

        if not guess_input.isdigit():
            print("Please enter a valid whole number.\n")
            continue

        guess = int(guess_input)
        attempts += 1

        if guess < lower or guess > upper:
            print(f"Please guess a number within {lower}-{upper}.\n")
        elif guess < secret_number:
            print("Too low! Try a higher number.\n")
        elif guess > secret_number:
            print("Too high! Try a lower number.\n")
        else:
            print(f"\n🎉 Correct! The number was {secret_number}.")
            print(f"You guessed it in {attempts} attempt(s).\n")
            break

    return attempts


def main():
    while True:
        play_game(1, 100)
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing! Goodbye.")
            break


if __name__ == "__main__":
    main()
