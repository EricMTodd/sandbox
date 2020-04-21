# My iterative solution
def factorials(n)
    product = 1
    for i in 1..n
        product *= i
        # puts(i)
    end
    puts(product)
end

factorials(5)

# Recursion will break the stack if the number is too big.
# def factorial_r(n)
#     return 1 if n <= 1
#     n * factorial_r(n-1)
# end

# puts(factorial_r(100000))

def fac(n)
    (1..n).inject(:*)
end

puts(fac(5))