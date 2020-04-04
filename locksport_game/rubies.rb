# This is gonna be my attempt at rewriting my locksport game using ruby. I feel like this will be a great learning experience and will be a chance to see if I can improve upon the original design at the same time.
# Remember to make a specific method for pretty much everything you want to do multiple times.

def game_over()
    # If win, congrats! Play again?
    # Else, BOO! YOU SUCK! Play again?
end

def fail_state()
    # YOU BREAK A LOCKPICK NERD
end

def win_condition()
    # You got the tumbler into place
end

def player_input()
    # Get player input
    # Evaluate against random code
    # Execute win/loss
end

def generate_code()
    # Randomize code
    # Evaluate sum and product of code
    # Return code
end

def main()
    # Print introduction
    puts("Welcome to locksport.")
    puts nil
    # Establish difficulty
    difficulty = 3
    level = 1
    chances = difficulty * 0.35
    # While loop to control difficulty
    while level <= difficulty
        puts(level)
        level += 1
    # Generate Code
    # Tell player sum and product of code
    # Get player guess
    # Evaluate guess against actual code
    # Win/Lose
    # If lose, subtract chances
    end
end

main()