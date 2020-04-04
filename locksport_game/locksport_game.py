from random import randint
from math import ceil


def print_introduction(max_level, attempts):
    print("\nYou've just stolen a pricelss artifact worth a fortune, it won't be long until you're caught.")
    print("You find a locked door barring your escape. You pull out your lockpicking kit and get to work.\n")
    if attempts == 1:
        print(
            f"This lock has {max_level} tumblers and you only have {attempts} lockpick you can use, try not to break it!\n")
    else:
        print(
            f"This lock has {max_level} tumblers and you have {attempts} lockpicks you can use, try not to break them!\n")


def generate_random_code(difficulty):
    code_a = randint(1, 2 + difficulty)
    code_b = randint(1, 2 + difficulty)
    code_c = randint(1, 2 + difficulty)

    # print(f"current code: {code_a} {code_b} {code_c}\n")

    code_sum = code_a + code_b + code_c
    code_product = code_a * code_b * code_c

    return code_sum, code_product


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("\n***INVALID INPUT***\n")


def get_str(prompt):
    while True:
        try:
            return str(input(prompt))
        except ValueError:
            print("\n***INVALID INPUT***\n")


def play_game(code_sum, code_product, difficulty, max_level):

    if difficulty == max_level:
        print(
            f"You're on the last tumbler!\n")
    else:
        if max_level - difficulty == 1:
            print(
                f"You are currently on tumbler number {difficulty}.\n{max_level - difficulty} tumbler left.\n")
        else:
            print(
                f"You are currently on tumbler number {difficulty}.\n{max_level - difficulty} tumblers left.\n")

    print("You must guess a three number code in order to successfully fit each tumbler into place.")
    print(f"The sum of the numbers in the code is {code_sum}.")
    print(f"The product of the numbers in the code is {code_product}.\n")

    guess_a = get_int("Please guess the first digit of the code: ")
    guess_b = get_int("Please guess the second digit of the code: ")
    guess_c = get_int("Please guess the third digit of the code: ")

    print(f"Your guess: {guess_a} {guess_b} {guess_c}\n")

    guess_sum = guess_a + guess_b + guess_c
    guess_product = guess_a * guess_b * guess_c

    return guess_sum == code_sum and guess_product == code_product


def main():
    print("\n--WELCOME TO LOCKSPORT--\n")
    difficulty = 1
    max_level = 0
    while True:
        try:
            max_level = get_int("Please enter a number from 3 to 10: ")
            if max_level not in range(3, 11):
                raise ValueError
            break
        except ValueError:
            print("\n***INVALID INPUT***\n")

    attempts = int(ceil(max_level * 0.25))

    print_introduction(max_level, attempts)

    code_sum, code_product = generate_random_code(difficulty)

    while difficulty <= max_level:
        try:
            level_complete = play_game(
                code_sum, code_product, difficulty, max_level)
        except ValueError:
            print(
                "\n***INVALID INPUT***\n")
            continue

        if level_complete:
            difficulty += 1
            code_sum, code_product = generate_random_code(difficulty)
            print(
                f"SUCCESS!\nYou feel the tumbler slide into place.\n")
        else:
            attempts -= 1
            if attempts == 1:
                print(
                    f"FAIL.\nYou have broken one of your lock picks. You have {attempts} lockpick left.\n")
            else:
                if attempts == 0:
                    print(
                        "FAIL.\nYou have broken all of your lockpicks, you have no way to escape.\n")
                    return
                print(
                    f"FAIL.\nYou have broken one of your lock picks. You have {attempts} lockpicks left.\n")

    print(
        "WIN!\nYou pop the lock, and throw open the door at a dead sprint into the night!\n")
    return


def reset():

    while True:
        reset = input("Would you like to play again? (y/n) ")
        reset = reset.lower()
        if reset == "yes" or reset == "y":
            main()
        elif reset == "no" or reset == "n":
            print("GAME OVER.\n")
            return
        else:
            continue


main()
reset()
