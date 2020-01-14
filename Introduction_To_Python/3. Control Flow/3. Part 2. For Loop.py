# Practice: Quick Brown Fox
# Use a for loop to take a list and print each element of the list in its own line.

# Example:

# sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]
# Output:
# the
# quick
# brown
# fox
# jumped
# over
# the
# lazy
# dog

sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

# Write a for loop to print out each word in the sentence list, one word per line

for word in sentence:
    print(word)

# Practice: Multiples of 5
# Write a for loop below that will print out every whole number that is a multiple of 5 and less than or equal to 30.
#
# This should output:

# Write a for loop using range() to print out multiples of 5 up to 30 inclusive

for i in range(5, 35, 5):
    print(i)

# Quiz: Create Usernames
# Write a for loop that iterates over the names
# list to create a usernames list. To create a username for each name,
# make everything lowercase and replace spaces with underscores. Running your for loop over the list:
#
# names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
#
# should create the list:
#
# usernames = ["joey_tribbiani", "monica_geller", "chandler_bing", "phoebe_buffay"]
#
# HINT: Use the .replace() method to replace the spaces with
# underscores. Check out how to use this method in this Stack Overflow answer.

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here

for name in names:
    usernames.append(name.lower().replace(" ", "_"))
print(usernames)

# for city in cities:
#     capitalized_cities.append(city.title())

# TODO: Finish Quizzes

