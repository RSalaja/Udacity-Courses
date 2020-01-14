# Integers and Floats
# There are two Python data types that could be used for numeric values:

# int - for integer values
# float - for decimal or floating point values

# You can create a value that follows the data type by using the following syntax:
x = int(4.7)   # x is now an integer 4
y = float(4)   # y is now a float of 4.0
# You can check the type by using the type function:#
print(type(x))
# >>> int
print(type(y))
# >>> float

# Because the float, or approximation, for 0.1 is actually slightly more than 0.1,
# when we add several of them together we can see the difference between the mathematically
# correct answer and the one that Python creates.

print(.1 + .1 + .1 == .3)

print(5/0)