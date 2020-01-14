# For Loops

# Q-13: Quiz (Sum List)

# Define a procedure, sum_list, that takes as its
# input a list of numbers, and produces as its output
# the sum of all the elements in the input list.
# For example,
# sum_list[1, 7, 4]

def sum_list(p):
    result = 0
    for e in p:
        result = result + e
    return result


print(sum_list([1, 4, 7]))

# Q-14: Quiz (Measure Udacity)

# Define a procedure, measure_udacity,
# that takes as its input a list of strings, and outputs a
# number that is a count of the number of elements in the input
# list that start with an uppercase letter 'U'.
# For example:
# measure_udacity(['Dave', 'Sebastian', 'Katy'])
# 0

# measure_udacity(['Umika', 'Umberto'])
# 2
def measure_udacity(p):
    f = 0
    for e in p:
        if e[0] == 'U':
            f = f + 1
    return f


print(measure_udacity(['Umika', 'Umberto']))
print(measure_udacity(['Dave', 'Sebastian', 'Katy']))


# Q-15: Quiz (Find Element)

# Define a procedure, find_element, that takes as its
# input a list and a value of any type, and outputs
# the index of the first element in the input list
# that matches the value. If there is no matching
# element, output -1.

def find_element(p, t):
    i = 0
    for e in p:
        if e == t:
            return i
        i = i + 1
    return -1


# Examples:
find_element([1, 2, 3], 3)
find_element(['alpha', 'beta'], 'gamma')
