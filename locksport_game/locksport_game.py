from random import randint
from math import ceil


def printIntroduction(maxLevel, attempts):
    print("\nYou've just stolen a pricelss artifact worth a fortune, it won't be long until you're caught.")
    print("You find a locked door barring your escape. You pull out your lockpicking kit and get to work.\n")
    if attempts == 1:
        print(
            f"This lock has {maxLevel} tumblers and you only have {attempts} lockpick you can use, try not to break it!\n")
    else:
        print(
            f"This lock has {maxLevel} tumblers and you have {attempts} lockpicks you can use, try not to break them!\n")


def generateRandomCode(difficulty):
    codeA = randint(1, 2 + difficulty)
    codeB = randint(1, 2 + difficulty)
    codeC = randint(1, 2 + difficulty)

    # print(f"current code: {codeA} {codeB} {codeC}\n")

    codeSum = codeA + codeB + codeC
    codeProduct = codeA * codeB * codeC

    return codeSum, codeProduct


def getInt(prompt, error_message="\n***INVALID INPUT***\n"):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(error_message)


def playGame(codeSum, codeProduct, difficulty, maxLevel):

    if difficulty == maxLevel:
        print(
            f"You're on the last tumbler!\n")
    else:
        print(
            f"You are currently on tumbler number {difficulty}.\n{maxLevel - difficulty} tumblers left.\n")

    print("You must guess a three number code in order to successfully fit each tumbler into place.")
    print(f"The sum of the numbers in the code is {codeSum}.")
    print(f"The product of the numbers in the code is {codeProduct}.\n")

    guessA = getInt("Please guess the first digit of the code: ")
    guessB = getInt("Please guess the second digit of the code: ")
    guessC = getInt("Please guess the third digit of the code: ")

    print(f"Your guess: {guessA} {guessB} {guessC}\n")

    guessSum = guessA + guessB + guessC
    guessProduct = guessA * guessB * guessC

    return guessSum == codeSum and guessProduct == codeProduct


def main():
    print("\n--WELCOME TO LOCKSPORT--\n")
    difficulty = 1
    maxLevel = 0
    while 3 > maxLevel or 10 < maxLevel:
        try:
            maxLevel = int(input("Please enter a number from 3 to 10: "))
        except ValueError:
            print("\n***INVALID INPUT***\n")

    attempts = int(ceil(maxLevel * 0.25))

    printIntroduction(maxLevel, attempts)

    codeSum, codeProduct = generateRandomCode(difficulty)

    while difficulty <= maxLevel:
        try:
            levelComplete = playGame(
                codeSum, codeProduct, difficulty, maxLevel)
        except ValueError:
            print(
                "\n***INVALID INPUT***\n")
            continue

        if levelComplete:
            difficulty += 1
            codeSum, codeProduct = generateRandomCode(difficulty)
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
                    return 0
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
