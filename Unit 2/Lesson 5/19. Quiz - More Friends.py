# Define a procedure, is_friend, that takes
# a string as its input, and returns a
# Boolean indicating if the input string
# is the name of a friend. Assume
# I am friends with everyone whose name
# starts with either 'D' or 'N', but no one
# else. You do not need to check for
# lower case 'd' or 'n'

def is_friend(a):
    if a[0] == "D":
        c = True
    else:
        if a[0] == "N":
            c = True
        else:
            c = False

    return c


print(is_friend('Diane'))
# >>> True

print(is_friend('Ned'))
# >>> True

print(is_friend('Moe'))
# >>> False
