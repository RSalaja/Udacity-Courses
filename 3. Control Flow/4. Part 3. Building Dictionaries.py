# Iterating Through Dictionaries with For Loops
# When you iterate through a dictionary using a for loop,
# doing it the normal way (for n in some_dict) will only give you access
# to the keys in the dictionary - which is what you'd want in some situations.
# In other cases, you'd want to iterate through both the keys and values in the dictionary.
# Let's see how this is done in an example.

# Consider this dictionary that uses names of
# actors as keys and their characters as values.

cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }

# Iterating through it in the usual way with a for loop
# would give you just the keys, as shown below:

for key in cast:
     print(key)

# If you wish to iterate through both keys and values,
# you can use the built-in method items like this:

for key, value in cast.items():
    print("Actor: {}    Role: {}".format(key, value))

# items is an awesome method that returns tuples of key, value pairs,
# which you can use to iterate over dictionaries in for loops.
