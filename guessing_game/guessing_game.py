from random import randrange
n = randrange(1, 100)
print(n)


def guess_engine():
    guess = int(input("Please enter a number between 1 and 100: "))
    if guess < n:
        print("Please guess a higher number.")
        guess_engine()
    elif guess > n:
        print("Please guess a lower number.")
        guess_engine()
    else:
        print("You guessed the correct number!")


guess_engine()
