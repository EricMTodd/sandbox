from random import randint
from math import ceil


def generateRandomCode(difficulty):
    codeA = int(randint(1, 2 + difficulty))
    codeB = int(randint(1, 2 + difficulty))
    codeC = int(randint(1, 2 + difficulty))

    codeSum = codeA + codeB + codeC
    codeProduct = codeA * codeB * codeC

    currentCode = f"{codeA} {codeB} {codeC}"
    print(f"currentCode: {currentCode}")


def main():
    difficulty = int(1)

    print("hello world")
    generateRandomCode(difficulty)


main()
