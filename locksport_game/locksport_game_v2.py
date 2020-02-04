def playGame(codeSum, codeProduct, difficulty, maxLevel):
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


def generateRandomCode(difficulty, maxLevel):
    codeA = int(4)
    codeB = int(3)
    codeC = int(2)

    codeSum = codeA + codeB + codeC
    codeProduct = codeA * codeB * codeC

    while (difficulty <= maxLevel):
        levelComplete = playGame(codeSum, codeProduct, difficulty, maxLevel)

    if (levelComplete == True):
        difficulty += 1


def main():
    difficulty = int(1)
    maxLevel = int(5)

    generateRandomCode(difficulty, maxLevel)

    print("end")
    return 0


main()
