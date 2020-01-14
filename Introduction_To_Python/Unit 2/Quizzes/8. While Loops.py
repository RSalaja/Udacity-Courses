# While Loops (While Loops)

# Q-16: Quiz (While Loops)
# What does this program do?
i = 0
while i != 10:
    i = i + 2
    print (i)

# a. Produce an error
# b. Print out the numbers from 0 to 9.
# c. Print out the numbers from 1 to 9.
# d. Print out the numbers from 1 to 10.
# e. Run
# Ans: D

# Q-17: Quiz (While Loops-2)
# What does the following code do?
i = 1
while i != 10:
    i = i + 2
    print (i)

# a. Produce an error.
# b. Print out 2, 4, 6, 8.
# c. Print out 1, 3, 5, 7, 9.
# d. Print out 3, 5, 7, 9.
# e. Run forever.
# Ans: E

# Q-18: Quiz (Print Numbers)
# Define a procedure, print_numbers, that takes as input a positive whole number, and prints out all
# the whole numbers from 1 up to and including the input number.
# print_numbers(3)
# 1
# 2
# 3

def print_numbers(a):
    i = 1
    while i <= a:
        print(i)
        i = i + 1
