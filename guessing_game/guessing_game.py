from random import randint

n = randint(1, 100)
l = list(range(1, 101))


def engine(number, choices):
    while True:
        print(choices)
        try:
            guess = int(
                input(f"Please enter a number from {min(choices)} to {max(choices)}: "))
            if not min(choices) <= guess <= max(choices):
                raise ValueError
            if guess == number:
                return "You guessed the correct number!"
            if guess < number:
                print(f"Please guess a higher number than {guess}.")
                choices = [x for x in choices if x > guess]
            else:
                print(f"Please guess a number lower than {guess}.")
                choices = [x for x in choices if x < guess]
        except ValueError:
            print(
                f"Invalid input! Your guess must be a number from {min(choices)} to {max(choices)}")


print(engine(n, l))
