# Pop

# The pop operation mutates a list by removing its last element.
# It returns the value of the element that was removed.

    # <list>.pop() → element

# Example:
    # a = [1, 2, 3]
    # b = a             # both a and b refer to the same list
    # x = a.pop()       # value of x is 3, and a and b now refer to the list [1, 2]

# Q-18: Quiz (Pop Quiz)

# Assume p refers to a list with at least two elements.
# Which of these code fragments does not change the final value p.

# 1.    p.append(3)
#       p.pop()

# 2.    x = p.pop()
#       y = p.pop()
#       p.append(x)
#       p.append(y)

# 3.    x = p.pop()
#       p.append(x)

# 4.    x = p.pop()
#       y = p.pop()
#       p.append(y)
#       p.append(x)