# This is gonna be my attempt at rewriting my locksport game using ruby. I feel like this will be a great learning experience and will be a chance to see if I can improve upon the original design at the same time.
# Remember to make a specific method for pretty much everything you want to do multiple times.

def start_game()
    # Print introduction
    puts("Welcome to locksport.")
    puts()
    # Establish difficulty
    difficulty = 3
    @level = 1
    chances = (difficulty * 0.6.to_f).ceil
    game_loop(difficulty, level, chances)
end

def game_loop(difficulty, level, chances) # add arguemnt, previous code = nil
    # While loop to control difficulty
    # if preveious code = nil, generate code; else use previous
    while level <= difficulty
        puts("level: #{level}")
        puts("chances: #{chances}")
        # How many chances left?
        if chances == 0
            return game_over(chances)
        end
        # Generate Code
        return generate_code(difficulty, level, chances)
    end
    game_over(chances)
end

def generate_code(difficulty, level, chances)
    # Randomize code
    # Evaluate sum and product of code
    puts()
    # Execute player input method
    player_input(sum_of_code(level), product_of_code(level), difficulty, level, chances)
end

def player_input(sum_of_code, product_of_code, difficulty, level, chances)
    # Get player input
    puts()
    print("Please guess the first digit of the code: ")
    guess_a = gets.chomp.to_i
    print("Please guess the second digit of the code: ")
    guess_b = gets.chomp.to_i
    print("Please guess the third digit of the code: ")
    guess_c = gets.chomp.to_i
    # Find sum and product of guesses
    guess_sum = guess_a + guess_b + guess_c
    guess_product = guess_a * guess_b * guess_c
    # Evaluate against random code
    if guess_sum == sum_of_code && guess_product == product_of_code # can be it's own method; correct_guess?
        puts()
        puts("SUCCESS")
        win_state(difficulty, level, chances)
    else
        puts()
        puts("FAIL")
        fail_state(difficulty, level, chances)
    end
    # Execute win/loss
end

private

def challenge_modifier(level)
    level + 1
end

def code_a(level)
    rand(1..challenge_modifier(level))
end

def code_b(level)
    rand(1..challenge_modifier(level))
end

def code_c(level)
    rand(1..challenge_modifier(level))
end

def sum_of_code(level)
    puts("The sum of the three digit code is: #{sum_of_code}")
    return code_a(level) + code_b(level) + code_c(level)
end

def product_of_code(level)
    puts("The product of the three digit code is: #{product_of_code}")
    return code_a(level) * code_b(level) * code_c(level)
end

def guess_a
    gets.chomp.to_i
end

def guess_b
    gets.chomp.to_i
end

def guess_c
    gets.chomp.to_i
end

def guess_sum
    guess_a + guess_b + guess_c
end

def guess_product
    guess_a * guess_b * guess_c
end

def correct_guess?(level)
    guess_sum == sum_of_code(level) && guess_product == product_of_code(level)
end

def win_state(difficulty, level, chances)
    # You got the tumbler into place
    level += 1
    game_loop(difficulty, level, chances)
end

def fail_state(difficulty, level, chances)
    # YOU BREAK A LOCKPICK NERD
    chances -= 1
    game_loop(difficulty, level, chances)
end

def game_over(chances)
    # If win, congrats! Play again?
    if chances > 0
        puts("YOU WIN!")
    # Else, BOO! YOU SUCK! Play again?
    else 
        puts("YOU LOSE!")
    end
    exit()
end

start_game()