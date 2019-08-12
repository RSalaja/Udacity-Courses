# For Loops

# In Python there is a more convenient way to loop
# through the elements of a list: the for loop.
# The syntax looks like this:

# for <name> in <list>:
#     <block>

# The loop goes through each element of the list in turn,
# assigning that element to the <name> and
# evaluating the <block>. Using the for loop, we can use
# less code than we needed using the while
# loop to define the procedure print_all_elements:

# def print_all_elements(p):
#     for e in p:
#        print e

# Let's walk-through what happens when you apply this for loop to a list:
# mylist = [1, 2, 3]
# print_all_elements(mylist)

# When you pass in mylist to print_all_elements
# the variable p will refer to the list that contains
# the three elements, 1, 2 and 3.
# When the loop is executed, the variable e is assigned to the first
# element in the list, and the body of the loop will print the first element.
# So, for the first iteration the value of e will be 1.
# The block is executed, printing out 1. Since there are more elements in the list,
# execution continues, assigning 2 to the e. Again, the block is executed,
# but this time it prints out 2. Execution continues for the third iteration,
# which prints out 3. There are no more elements in the
# list, so the for loop is complete

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
