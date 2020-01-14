# Variables (Video: Variables)

# A variable is a name refers to a value. In Python,
# we can use any sequence of letters and numbers
# and underscores (_) we want to make a variable name,
# so long as it does not start with a number.

# Here are some examples of valid variable names:
# processor_speed
# n
# Dorina
# item73

# To introduce a new variable, we use an assignment statement:
# Name = Expression

# After executing an assignment expression,
# the name refers to the value of the expression on the
# right side of the assignment:
speed_of_light = 299792458

# We can use the variable name anywhere we want and
# it means the same things as the value it refers to.
# Here is an expression using the name to print out the speed of light in centimeters:
print(speed_of_light * 100)

# You can create new variables to keep track of values in programs.
# Here is an expression to find the
# length of the nanostick in centimeters:
speed_of_light = 299792458
billionth = 1.0 / 1000000000
nanostick = speed_of_light * billionth * 100
print(nanostick)

# QUIZ: DISTANCE OF A CYCLE

# Given the variables defined here, write Python
# code that prints out the distance, in meters,
# that light travels in one processor cycle.

# speed_of_light in meters per second
# cycles_per_second is 2.7 GHz

cycles_per_second = 2700000000
cycle_distance = (speed_of_light / cycles_per_second)
print(cycle_distance * 100)
print(cycle_distance)

cycles_per_second = 2800000000
print(cycle_distance)

cycle_distance = speed_of_light / cycles_per_second
print(cycle_distance)

# Variables Can Vary

# The value a variable refers to can change.
# When a variable name is used, it always refers to the last
# value assigned to that variable.
# For example, we can change the value of cycles_per_second.
# Suppose we have a faster processor:

speed_of_light = 299792458  # meters per second
cycles_per_second = 27000000000.  # 2.7GHz
cycle_distance = speed_of_light / cycles_per_second
cycle_per_second = 2800000000.  # 2.8 GHz
print
cycle_distance

cycle_distance = speed_of_light / cycles_per_second
print
cycle_distance

# Since the value that a variable refers to can change,
# the same exact expression can have different
# values at the different times it is executed.

# QUIZ: SPIRIT AGE

# Write python code that defines the variable
# age to be your age in years, and then prints
# out the number of days you have been alive.

year = 365  # in days
leap_year = 366  # in days
spirit_age = 24
age = ((spirit_age / 4) * (leap_year) + (24 - (spirit_age / 4)) * (year))
print(age)
