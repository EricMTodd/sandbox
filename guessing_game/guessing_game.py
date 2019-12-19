from random import randrange
n = randrange(1, 100)
min = 1
max = 100


def guessing_game():
    guess = input("Guess a number between 1 and 100: ")
    guess = int(guess)

    if guess < n:
        print("Sorry, you guessed too low. Try again.")
        min = guess + 1
    elif guess > n:
        print("Sorry, you guessed too high. Try again.")
        max = guess - 1
    else:
        print(f"You found the number! {n}")


guessing_game()
