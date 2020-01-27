from random import randint
from math import ceil


def printIntroduction(maxLevel, attempts):
    print("\nYou've just stolen a pricelss artifact worth a fortune, it won't be long until you're caught.")
    print("You find a locked door barring your escape. You pull out your lockpicking kit and get to work.\n")
    print(
        f"This lock has {maxLevel} tumblers and you have {attempts} lockpicks you can use, try not to break them!\n")


def playGame(difficulty, maxLevel, attempts):

    codeA = int(randint(1, 2 + difficulty))
    codeB = int(randint(1, 2 + difficulty))
    codeC = int(randint(1, 2 + difficulty))

    codeSum = int(codeA) + int(codeB) + int(codeC)
    codeProduct = int(codeA) * int(codeB) * int(codeC)

    if difficulty == maxLevel:
        print(
            f"You're on the last tumbler!\n")
    else:
        print(
            f"You are currently on tumbler number {difficulty}.\n{maxLevel - difficulty} tumblers left.\n")

    print("You must guess a three number code in order to successfully fit each tumbler into place.")
    print(f"The sum of the numbers in the code is {codeSum}.")
    print(f"The product of the numbers in the code is {codeProduct}.\n")

    guessA = int(input("Please guess the first digit of the code: "))
    guessB = int(input("Please guess the second digit of the code: "))
    guessC = int(input("Please guess the third digit of the code: "))

    print(f"Your guess: {guessA} {guessB} {guessC}\n")

    guessSum = guessA + guessB + guessC
    guessProduct = guessA * guessB * guessC

    if (guessSum == codeSum and guessProduct == codeProduct):
        return True
    else:
        return False


def main():
    difficulty = int(1)
    maxLevel = int(5)
    attempts = int(ceil(maxLevel * 0.25))

    printIntroduction(maxLevel, attempts)

    while (difficulty <= maxLevel):
        try:
            levelComplete = playGame(difficulty, maxLevel, attempts)
        except ValueError:
            print(
                "\n***INVALID INPUT: You have entered an invalid character. Please try again.***\n")
            continue

        if (levelComplete == True):
            difficulty += 1
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
                        "You have broken all of your lockpicks, you have no way to escape.\n")
                    return 0
                print(
                    f"FAIL.\nYou have broken one of your lock picks. You have {attempts} lockpicks left.\n")

    print(
        "WIN!\nYou pop the lock, and throw open the door at a dead sprint into the night!\n")
    return 0


def playAgain():
    main()
    while True:
        reset = input("Would you like to play again? (y/n) ")
        reset = reset.lower()
        if (reset == "yes" or reset == "y"):
            playAgain()
        if (reset == "no" or reset == "n"):
            print("GAME OVER.")
        return 0


playAgain()
