from random import randint

n = randint(1, 100)
l = list(range(1, 101))
print(l)


def guess_engine():
    guess = int(input("Please enter a number between 1 and 100: "))
    index = l.index(guess)
    print(index)


guess_engine()
