# Index

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
