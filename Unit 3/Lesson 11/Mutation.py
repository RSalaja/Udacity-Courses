# Mutation

# Mutation means changing the value of an object. Lists support mutation. This is the second main
# difference between strings and lists.
# It might have seemed like we could change the value of strings:

s = 'Hello'
s = 'Yello'

# However, this expression changes the value the variable s refers to, but does not change the value
# of the string 'Hello'. As another example, consider string concatenation:
s = s + 'w'
# This operation may look like it is changing the value of the string, but that's not what happens. It is
# not modifying the value of any string, but instead is creating a new string, 'Yellow', and assigning
# the variable s to refer to that new string.
# Lists can be mutated, thus changing the value of an existing list. Here is a list:

p = ['H', 'e', 'l', 'l', 'o']

# Mutate a list by modifying the value of its elements:

p[0] = 'Y'
# This expression replaces the value in position 0 of p with the string 'Y'. After the assignment, the
# value of p has changed:

print(p)
['Y', 'e', 'l', 'l', 'o']
p[4] = '!'
print(p)
['Y', 'e', 'l', 'l', '!']

#       Q-5: Quiz (Different Stooges)
# Previously, we defined:

stooges = ['Moe', 'Larry', 'Curly']

# In some Stooges films, though, Curly was replaced by Shemp.
# Write one line of code that changes
# the value of stooges to be:

['Moe', 'Larry', 'Shemp']


# but does not create a new list object.

def stooge_change(a, b, c):
    stooges[2] = 'shemp'
    print(stooges)


stooge_change('Moe', 'Larry', 'Curly')
