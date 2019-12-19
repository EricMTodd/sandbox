from random import randint
n = randint(1, 100)
print(n)
numbers_list = []

for i in range(1, 101):
    numbers_list.append(i)
print(numbers_list)


def guess_engine():
    guess = int(input("Please enter a number between 1 and 100: "))
    if guess < n:
        print("Please guess a higher number.")
        del numbers_list[:guess]
        print(numbers_list)
        guess_engine()
    elif guess > n:
        print("Please guess a lower number.")
        del numbers_list[guess - 1:]
        print(numbers_list)
        guess_engine()
    else:
        print("You guessed the correct number!")


guess_engine()
