# This is gonna be my attempt at rewriting my locksport game using ruby. I feel like this will be a great learning experience and will be a chance to see if I can improve upon the original design at the same time.
# Remember to make a specific method for pretty much everything you want to do multiple times.

def start_game()
    # Print introduction
    puts("Welcome to locksport.")
    puts()
    # Establish difficulty
    difficulty = 3
    level = 1
    chances = (difficulty * 0.6.to_f).ceil
    game_loop(difficulty, level, chances)
end

def game_loop(difficulty, level, chances)
    # While loop to control difficulty
    while level <= difficulty
        puts("level: #{level}")
        puts("chances: #{chances}")
        # How many chances left?
        if chances == 0
            game_over(chances)
        end
        # Generate Code
        generate_code(difficulty, level, chances)
    end
    game_over(chances)
end

def generate_code(difficulty, level, chances)
    challenge_modifier = 1 + level
    # Randomize code
    code_a = rand(1..challenge_modifier)
    code_b = rand(1..challenge_modifier)
    code_c = rand(1..challenge_modifier)
    # puts("code: #{code_a} #{code_b} #{code_c}")
    # Evaluate sum and product of code
    puts()
    sum_of_code = code_a + code_b + code_c
    puts("The sum of the three digit code is: #{sum_of_code}")
    product_of_code = (code_a * code_b * code_c)
    puts("The product of the three digit code is: #{product_of_code}")
    # Execute player input method
    player_input(sum_of_code, product_of_code, difficulty, level, chances)
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
    if guess_sum == sum_of_code && guess_product == product_of_code
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