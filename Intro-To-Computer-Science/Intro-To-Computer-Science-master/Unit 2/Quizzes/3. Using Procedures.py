# Using Procedures (Using Procedures)

# Q-4: Quiz (Inc Procedure)
# What does the inc procedure defined below do?
# def inc(n):
# return n + 1
# a. Nothing
# b. Takes a number as input, and outputs that number plus one
# c. Takes a number as input, and outputs the same number
# d. Takes two numbers as inputs, and outputs their sum
# Ans: C

# Q-5: Quiz (Sum Procedure)
# What does the sum procedure defined below do?
# def sum(a, b):
# a = a + b
# a. Nothing
# b. Takes two numbers as its inputs, and outputs their sum
# c. Takes two strings as its inputs, and outputs the concatenation of the two strings
# d. Takes two numbers as its inputs, and changes the value of the first input to be the sum of
#    the two number
# Ans: D

# Q-6: Quiz (Sum Procedure with a Return Statement)
# What does the sum procedure defined below do?
# def sum(a,b):
# a = a + b
# return a
# a. Takes two numbers as its inputs, and outputs their sum.
# b. Takes two strings as its inputs, and outputs the concatenation of the two strings.
# c. Takes two numbers as its inputs, and changes the value of the first input to be the sum of
#    the two number.
# Ans: C

# Q-7: Quiz (Square)
# Define a procedure, square, that takes one number as its input, and outputs the square of that
# number (result of multiplying the number by itself).
# For example,
# print square(5)
# 25

def square(a):
    a = a ** 2
    print(a)


square(5)


# Q-8: Quiz (Sum of Three)
# Define a procedure, sum3, that takes three inputs, and outputs the sum of
# the three input numbers.
# print sum3(1, 2, 3) → 6
def sum3(a, b, c):
    c = a + b + c
    print(c)


sum3(1, 2, 3)


# Q-9: Quiz (Abbaize)
# Define a procedure, abbaize, that takes two strings as its input, and outputs
# a string that is the first input followed by two repetitions of the
# second input, followed by the first input.
# abbaize('a', 'b') → 'abba'
# abbaize('dog', 'cat') → 'dogcatcatdog'
def abbaize(a, b):
    c = a + b + b + a
    return c


print(abbaize('a', 'b'))


# Q-10: Quiz (Find Second)
# Define a procedure, find_second, that takes two strings as its inputs: a
# search string and a target string. It should output a number located at the
# second occurrence of the target string within the search string.
# Example:
# danton = "De l'audace, encore de l'audace, toujours de l'audace."
# print find_second(danton, 'audace')
# 25
def find_second(a, b):
    c = a.find(b)
    d = a.find(b, c + 1)
    return d


danton = "De l'audace, encore de l'audace, toujours de l'audace"
print(find_second(danton, 'audace'))
