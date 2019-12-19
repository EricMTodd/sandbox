from random import randint

n = randint(1, 100)
l = list(range(1, 101))
print(l)


def guess_engine():
    guess = int(input("Please enter a number between 1 and 100: "))
    if guess < n:
        print(f"Please guess a higher number than {guess}.")
        guess_engine()
    elif guess > n:
        print(f"Please guess a lower number than {guess}.")
        guess_engine()
    else:
        print("You guessed the correct number!")


guess_engine()
