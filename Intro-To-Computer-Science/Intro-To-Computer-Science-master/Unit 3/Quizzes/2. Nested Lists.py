# Nested Lists

# Q-3: Quiz (Countries)
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

# Q-4: Quiz (Relative Size)
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
