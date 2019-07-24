# Structured Data (Introduction)

# The main new topic for Unit 3 is structured data. By the end of this unit, you will have finished
# building a simple web crawler.
# The closest thing you have seen to structured data so far is the string type introduced in Unit 1, and
# used in many of the procedures in Unit 2. A string is considered a kind of structured data because
# you can break it down into its characters and you can operate on sub-sequences of a string. This
# unit introduces lists, a more powerful and general type of structured data. Compared to a string
# where all of the elements must be characters, in a list the elements can be anything you want such
# as characters, strings, numbers or even other lists!

# The table below summarizes the similarities and differences between strings and lists.

# String                                             List
# elements are characters                            elements may be any Python value
#
# surrounded by singled or double quotes             surrounded by square brackets
# s = 'yabba!'                                       p = ['y','a','b','b','a','!']
#
# select elements using <string>[<number>]           select elements using <list>[<number>]
# s[0] → 'y'                                         p[0] → 'y'
#
#
# select sub-sequence using                          using select sub-sequence using
# <string>[<number> : <number>]                      <list>[<number> : <number>]
# s[2:4] → 'bb'                                      p[2:4] → ['b','b']
#
#
# immutable                                          mutable
# s[0] = 'b' → Error                                 p[0] = 'b'
# cannot change the value of a string                changes the value of the first element of p

#       Q-1: Quiz (Stooges)
# Define a variable, stooges,
# whose value is a list
# of the names of the Three Stooges:
# “Moe”, “Larry” and “Curly.”
stooges = ['Moe', 'Larry', 'Curly']

#       Q-2: Quiz (Days in a Month)
# Given the variable:

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# define a procedure, how_many_days,
# that takes as input a number
# representing a month, and outputs
# the number of days in that month.

def how_many_days(a):
    print(days_in_month[a - 1])


how_many_days(1)
how_many_days(9)
