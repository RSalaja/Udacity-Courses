# Nested Lists
# So far, all of the elements in our lists have been of the same type: strings, numbers, etc. However,
# there are no restrictions on the types of elements in a list. Elements of a list can be any type you
# want, you can also mix and match different types of elements in a list.
# For example:

mixed_up = ['apple', 3, 'oranges', 27, [1, 2, ['alpha', 'beta']]]

# or a more useful example:

beatles = [['John', 1940], ['Paul', 1942], ['George', 1943], ['Ringo', 1940]]

# This list provides information about the names of the Beatles band members, as well as when
# they were born. Try putting this into your interpreter. When you are typing your code into the
# interpreter and you want to separate data onto two lines, do so after a comma to make it clear to
# the interpreter that this is still one list.

beatles = [['John', 1940], ['Paul', 1942], ['George', 1943], ['Ringo', 1940]]
print
beatles
print
beatles[3]

# You can also use indexing again on the list that results to obtain an inner element:

print
beatles[3][0]

#       Q-3: Quiz (Countries)
# Given the variable countries defined as:

countries = [['China', 'Beijing', 1350],
             ['India', 'Delhi', 1220],
             ['Romania', 'Bucharest', 21],
             ['United States', 'Washington', 307]]


# Each list contains the name of a country,
# its capital, and its approximate population in millions.
# Write code to print out the capital of India.

def country_capital(a):
    return (countries[a][1])


print(country_capital(1))

#       Q-4: Quiz (Relative Size)
# Given the variable countries defined as:
#              Name              Capital        Populations (millions)
countries = [['China', 'Beijing', 1350],
             ['India', 'Delhi', 1210],
             ['Romania', 'Bucharest', 21],
             ['United States', 'Washington', 307]]


# What multiple of Romania's population is the population
# of China? Calculate this by accessing the list and
# dividing the population of China (1350)
# by the population of Romania (21).
# Please print your result.

def pop_mup(a, b):
    mult = countries[a][2] / countries[b][2]
    print(mult)


pop_mup(0, 2)
