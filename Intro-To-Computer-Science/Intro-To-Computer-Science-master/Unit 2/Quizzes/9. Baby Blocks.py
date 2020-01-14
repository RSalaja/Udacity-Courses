# Baby Blocks

# Q-19: Quiz (Factorial)
# Define a procedure, factorial, that takes one number as its input and outputs the factorial of that
# number.

def factorial(n):
    i = 1
    while n >= 1:
        i = i * n
        n = (n - 1)
    return i
