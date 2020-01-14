# Lambda Expressions
# You can use lambda expressions to create anonymous functions.
# That is, functions that don’t have a name.
# They are helpful for creating quick functions that aren’t needed later in your code.
# This can be especially useful for higher order functions, or functions that take in other functions as arguments.
#
# With a lambda expression, this function:

def multiply_1(x, y):
    return x * y
# can be reduced to:

multiply_2 = lambda x, y: x * y

# Both of these functions are used in the same way.
# In either case, we can call multiply like this:

multiply_1(4, 7)
multiply_2(6, 9)

def mean(num_list):
    return sum(num_list) / len(num_list)

averages = list(map(mean, numbers))
print(averages)

mean = lambda num_list: sum(num_list)/len(num_list)