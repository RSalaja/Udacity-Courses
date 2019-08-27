# Or Expressions

# Q-15: Quiz (Biggest)
# Define a procedure, biggest, that takes three numbers as inputs, and outputs the greatest of the
# three numbers.
# biggest (6, 2, 3) → 6
# biggest (6, 2, 7) → 7
# biggest (6, 9, 3) → 9

def bigger (a, b):
    if a > b:
        return a
    else:
        return b

def biggest(a, b, c):
    return bigger(bigger(a, b), c)

def biggest(a, b, c):
    return max(a, b, c)

print(biggest (6, 2, 3))
print(biggest (6, 2, 7))
print(biggest (6, 9, 3))

