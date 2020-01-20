def printIntroduction(difficulty):
    print("You've just stolen a pricelss artifact worth untold riches, you can hear the guards running towards you just around the corner.")
    print(
        f"You are desperately trying to undo the level {difficulty} lock to the door that bars your only escape from imminent doom.")
    print("You reach for the note torn from the scientist's journal and it all comes together...")


def playGame(difficulty):
    printIntroduction(difficulty)

    codeA = int(4)
    codeB = int(3)
    codeC = int(2)

    codeSum = int(codeA) + int(codeB) + int(codeC)
    codeProduct = int(codeA) * int(codeB) * int(codeC)

    print("There are three numbers in the code.")
    print(f"The numbers in the code add up to {codeSum}.")
    print(f"The product of the numbers in the code is {codeProduct}.")

    guessA = input("Please guess the first digit of the code: ")
    guessB = input("Please guess the second digit of the code: ")
    guessC = input("Please guess the third digit of the code: ")

    print(f"Your guess: {guessA} {guessB} {guessC}")

    guessSum = int(guessA) + int(guessB) + int(guessC)
    guessProduct = int(guessA) * int(guessB) * int(guessC)

    print(f"The sum of your guess is {guessSum}.")
    print(f"The product of your guess is {guessProduct}.")

    if (guessSum == codeSum and guessProduct == codeProduct):
        print("You pop the lock, and throw open the door at a dead sprint into the night!")
        return True
    else:
        print("The guards have caught you, they beat you into unconsciousness...")
        return False


def main():
    levelDifficulty = int(1)
    maxLevel = int(5)

    while (levelDifficulty <= maxLevel):
        levelComplete = playGame(levelDifficulty)

        if (levelComplete == True):
            levelDifficulty += 1

    return 0


main()
