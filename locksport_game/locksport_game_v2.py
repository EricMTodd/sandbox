from random import randint
from math import ceil

# Print introduction


def printIntroduction(maxLevel, attempts):
    print("\nYou've just stolen a pricelss artifact worth a fortune, it won't be long until you're caught.")
    print("You find a locked door barring your escape. You pull out your lockpicking kit and get to work.\n")
    print(
        f"This lock has {maxLevel} tumblers and you have {attempts} lockpicks you can use, try not to break them!\n")


# Take user input

def playerGuess(codeSum, codeProduct):
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

# Generate code


def generateRandomCode(difficulty):
    codeA = int(randint(1, 2 + difficulty))
    codeB = int(randint(1, 2 + difficulty))
    codeC = int(randint(1, 2 + difficulty))

    codeSum = codeA + codeB + codeC
    codeProduct = codeA * codeB * codeC

    currentCode = f"{codeA} {codeB} {codeC}"
    print(f"currentCode: {currentCode}")


# Check user input
# If correct, advance difficulty. If Incorrect, deplete attempts. If user input is invalid, alert player.


def main():
    difficulty = int(1)
    maxLevel = int(5)
    attempts = int(ceil(maxLevel * 0.25))

    printIntroduction(maxLevel, attempts)
    generateRandomCode(difficulty)
    if difficulty == maxLevel:
        print(
            f"You're on the last tumbler!\n")
    else:
        print(
            f"You are currently on tumbler number {difficulty}.\n{maxLevel - difficulty} tumblers left.\n")


main()
