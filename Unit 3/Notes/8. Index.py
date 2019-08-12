# Index

# There are many other ways to define find_element.
# A built-in list operation that we have not yet introduced
# that makes it easier to write find_element is the index method:

# <list>.index(<value>) → <position> or error

# The index method is invoked on a list by passing in a value, and the output is the first position
# where that value sits in the list. If the list that does not contain any occurrences of the value you
# pass in, index produces an error (this is different from the find method for strings which we used
# in Unit 1, that returns a -1 when the target string is not found).

# Examples:

# p = [0, 1, 2]
# print p.index(2)
# 2
# p = [0, 1, 2, 2, 2]
# print p.index(2)
# 2
# Even though there are many 2s in the list, the output is the first position where 2 occurs.

# p = [0, 1, 2]
# print p.index(3)
# ValueError: list.index(x): x not in list

# Since the requested behavior of find_element is to output -1
# when the input element is not found, we cannot use index
# directly to implement find_element since index produces an error
# when the element is not found. Instead, we can use another list operation,
# in, to first test if the element is anywhere in the list. We have already
# seen in used in the for loop, however outside of a
# for loop header it means something different:

# <value> in <list> → <Boolean>

# The output is True if the list contains an element matching value, and False if it does not.

# Examples:

# p = [0, 1, 2]
# print 3 in p
# False
# print 1 in p
# True

# Similarly, you can use not in, which has the opposite meaning of in:

# <value> not in <list>

# If the value is not in the list the result of <value> not in <list> is True, and if the <value> is in
# the <list> than the result is False.

# These two expressions are equivalent:

# <value> not in <list> not <value> in <list>

# Q-16: Quiz
# Define find_element, this time using index.

def find_element(p, t):
    if t in p:
        return p.index(t)
    else:
        return -1


def find_element(p, t):
    if t not in p:
        return -1
    return p.index(t)


# Q-17: Quiz (Union)
# Define a procedure, union, that takes as inputs two lists. It should modify the first input list to be
# the set union of the two lists.
# Examples:
# a = [1, 2, 3]
# b = [2, 4, 6]
# union(a, b)
# print a
# [1, 2, 3, 4, 6]
# print b
# [2, 4, 6]
# Answer to Q-17

def union(p, q):
    for e in q:
        if e not in p:
            p.append(e)
