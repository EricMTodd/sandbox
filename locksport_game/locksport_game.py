from random import randint


def printIntroduction(difficulty):
    print("\nYou've just stolen a pricelss artifact worth a fortune, it won't be long until you're caught.")

    print("You find a locked door barring your escape. You pull out your lockpicking kit and get to work.\n")


def playGame(difficulty):

    codeA = int(randint(1, 5))
    codeB = int(randint(1, 5))
    codeC = int(randint(1, 5))

    codeSum = int(codeA) + int(codeB) + int(codeC)
    codeProduct = int(codeA) * int(codeB) * int(codeC)

    print(
        f"You are currently on tumbler number {difficulty}.\n")

    print("You must guess a three number code in order to successfully fit each tumbler into place.")
    print(f"The numbers in the code add up to {codeSum}.")
    print(f"The product of the numbers in the code is {codeProduct}.\n")

    try:
        guessA = int(input("Please guess the first digit of the code: "))
        guessB = int(input("Please guess the second digit of the code: "))
        guessC = int(input("Please guess the third digit of the code: "))

        print(f"Your guess: {guessA} {guessB} {guessC}")

        guessSum = guessA + guessB + guessC
        guessProduct = guessA * guessB * guessC

        if (guessSum == codeSum and guessProduct == codeProduct):
            print(
                f"You feel the tumbler slide into place, {5 - difficulty} tumblers left.")
            return True
        else:
            print("The guards have caught you, they beat you into unconsciousness...\n")
            return False
    except ValueError:
        print("\n***You have entered an invalid character. Please try again.***\n")


def main():
    levelDifficulty = int(1)
    maxLevel = int(5)
    printIntroduction(levelDifficulty)

    while (levelDifficulty <= maxLevel):
        levelComplete = playGame(levelDifficulty)

        if (levelComplete == True):
            levelDifficulty += 1

    print(
        "You pop the lock, and throw open the door at a dead sprint into the night!")
    return 0


main()
