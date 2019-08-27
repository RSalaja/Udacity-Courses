# Mutation

# Q-5: Quiz (Different Stooges)
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
