# Else Expressions (Is Friend)

# Q-13: Quiz (Is Friend)
# Define a procedure, is_friend, that takes a string as its input, and outputs
# a Boolean indicating if the input string is the name of a friend.
# Assume I am friends with everyone whose name starts with D and no one else.
# print is_friend('Diane') → True
# print is_friend('Fred') → False
def is_friend(name):
    if name [0] == 'D':
        return True
    else:
        return False

# Q-14: Quiz (More Friends)
# Define a procedure, is_friend, that takes a string as its input, and outputs
# a Boolean indicating if the input string is the name of a friend.
# Assume I am friends with everyone whose name starts with either D or N,
# but no one else.
# print is_friend('Diane') → True
# print is_friend('Ned') → True
def is_friend(name):
    if name[0] == 'D':
        return True
    if name [0] == 'N':
        return True
    return False
