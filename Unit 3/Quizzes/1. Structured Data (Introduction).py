# Structured Data (Introduction)

# Q-1: Quiz (Stooges)
# Define a variable, stooges,
# whose value is a list
# of the names of the Three Stooges:
# “Moe”, “Larry” and “Curly.”
stooges = ['Moe', 'Larry', 'Curly']

# Q-2: Quiz (Days in a Month)
# Given the variable:

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# define a procedure, how_many_days, that takes as input a number
# representing a month, and outputs the number of days in that month.

def how_many_days(a):
    print(days_in_month[a - 1])

how_many_days(1)
how_many_days(9)
