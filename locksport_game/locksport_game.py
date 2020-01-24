from random import randint


def printIntroduction(difficulty):
    print("You've just stolen a pricelss artifact worth untold riches, you can hear the guards running towards you just around the corner.")

    print("You reach for the note torn from the scientist's journal and it all comes together...")


def playGame(difficulty):

    codeA = int(randint(1, 5))
    codeB = int(randint(1, 5))
    codeC = int(randint(1, 5))

    codeSum = int(codeA) + int(codeB) + int(codeC)
    codeProduct = int(codeA) * int(codeB) * int(codeC)

    print(
        f"You are currently on tumbler number {difficulty}.")

    print("There are three numbers in the code.")
    print(f"The numbers in the code add up to {codeSum}.")
    print(f"The product of the numbers in the code is {codeProduct}.")

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
            print("The guards have caught you, they beat you into unconsciousness...")
            return False
    except ValueError:
        print("You have entered an invalid character. Please try again.")


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
