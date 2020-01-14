# Mutability and Order

# Mutability is about whether or not we can change an object once it has been created.
# If an object (like a list or string) can be changed (like a list can),
# then it is called mutable. However, if an object cannot be changed with creating
# a completely new object (like strings), then the object is considered immutable.

my_lst = [1, 2, 3, 4, 5]
my_lst[0] = 'one'
print(my_lst)
# ['one', 2, 3, 4, 5]

# As shown above, you are able to replace 1 with 'one' in the above list. This is because lists are mutable.

# However, the following does not work:

# >>> greeting = "Hello there"
# >>> greeting[0] = 'M'
# This is because strings are immutable. This means to change this string,
# you will need to create a completely new string.

# There are two things to keep in mind for each of the data types you are using:#
# Are they mutable?
# Are they ordered?

# Order is about whether the position of an element in the object can be used to access the element. Both strings and
# lists are ordered. We can use the order to access parts of a list and string.

# However, you will see some data types in the next sections that will be unordered. For each of the upcoming data
# structures you see, it is useful to understand how you index, are they mutable, and are they ordered.
# Knowing this about the data structure is really useful!

# Additionally, you will see how these each have different methods, so why you would use one
# data structure vs. another is largely dependent on these properties, and what you can easily do with it!

# Quiz: List Indexing
# Use list indexing to determine how many days are in a particular month based on the integer
# variable month, and store that value in the integer variable num_days.
# For example, if month is 8, num_days should be set to 31, since the eighth month, August, has 31 days.

# Remember to account for zero-based indexing!

month = 8
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# use list indexing to determine the number of days in month

num_days = days_in_month[month - 1]
print(num_days)

# Quiz: Slicing Lists
# Select the three most recent dates from this list using list slicing notation.
# Hint: negative indexes work in slices!

eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']

# TODO: Modify this line so it prints the last three elements of the list
print(eclipse_dates[-3:])