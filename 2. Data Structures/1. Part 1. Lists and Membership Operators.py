# List and Membership Operators

# There are three videos as a part of this page.
# Be sure to check them out along with the additional helpful reminders!

# Lists!
# Data structures are containers that organize and group data types together in different ways.
# A list is one of the most common and basic data structures in Python.

# You saw here that you can create a list with square brackets.
# Lists can contain any mix and match of the data types you have seen so far.

list_of_random_things = [1, 3.4, 'a string', True]

# This is a list of 4 elements.
# All ordered containers (like lists) are indexed in python using a starting index of 0.
# Therefore, to pull the first value from the above list, we can write:
list_of_random_things[0]
#
# It might seem like you can pull the last element with the following code, but this actually won't work:

# list_of_random_things[len(list_of_random_things)]
# ---------------------------------------------------------------------------
# IndexError                                Traceback (most recent call last)
# <ipython-input-34-f88b03e5c60e> in <module>()
# ----> 1 lst[len(lst)]
# IndexError: list index out of range

# However, you can retrieve the last element by reducing the index by 1.
# Therefore, you can do the following:

list_of_random_things[len(list_of_random_things) - 1]
# True

# Alternatively, you can index from the end of a list by using negative values,
# where -1 is the last element, -2 is the second to last element and so on.

list_of_random_things[-1]
# True
list_of_random_things[-2]
# a string

