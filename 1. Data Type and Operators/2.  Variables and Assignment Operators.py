# Variables and Assignment Operators
# From this page, you will get your first look at variables in Python.
# There are three videos in this concept to show you some different cases you might run into!

# Variables I
# Variables are used all the time in Python!
# Below is the example you saw in the video where we performed the following:
mv_population = 74728

# Here mv_population is a variable, which holds the value of 74728.
# This assigns the item on the right to the name on the left,
# which is actually a little different than mathematical equality, as 74728 does not hold the value of mv_population.
# In any case, whatever term is on the left side, is now a name for whatever value is on the right side.
# Once a value has been assigned to a variable name, you can access the value from the variable name.

# Variables II
# In this video you saw that the following two are equivalent in terms of assignment:
x = 3
y = 4
z = 5
# and
x, y, z = 3, 4, 5

# However, the above isn't a great way to assign variables in most cases,
# because our variable names should be descriptive of the values they hold.
# Besides writing variable names that are descriptive,
# there are a few things to watch out for when naming variables in Python.

# 1.    Only use ordinary letters, numbers and underscores in your variable names.
#       They can’t have spaces, and need to start with a letter or underscore.

# 2.    You can’t use reserved words or built-in identifiers that have important purposes in Python,
#       which you’ll learn about throughout this course. A list of python reserved words is described here.
#       Creating names that are descriptive of the values often will help you avoid using any of these words.
#       A quick table of these words is also available below.

# 3.    The pythonic way to name variables is to use all lowercase letters and underscores to separate words.

# YES
my_height = 58
my_lat = 40
my_long = 105
# NO
my_height = 58
MYLONG = 40
MyLat = 105

# Though the last two of these would work in python, they are not pythonic ways to name variables.
# The way we name variables is called snake case, because we tend to connect the words with underscores.

# Now it's your turn to work with variables.
# The comments in this quiz (the lines that begin with #) have instructions for creating and modifying variables.
# After each comment write a line of code that implements the instruction.
# Note that this code uses scientific notation to define large numbers.
# 4.445e8 is equal to 4.445 * 10 ** 8 which is equal to 444500000.0.

# Quiz: Assign and Modify Variables

# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6
# decrease the rainfall variable by 10% to account for runoff
rainfall= rainfall * (9/10)
# add the rainfall variable to the reservoir_volume variable
rainfall + reservoir_volume
# increase reservoir_volume by 5% to account for stormwater that flows
# into the reservoir in the days following the storm
reservoir_volume = reservoir_volume*(105/100)
# decrease reservoir_volume by 5% to account for evaporation
reservoir_volume = reservoir_volume*(95/100)
# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.
reservoir_volume = reservoir_volume - 2.5e5
# print the new value of the reservoir_volume variable
print(reservoir_volume)