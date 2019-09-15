# Strings
# Strings in Python are shown as the variable type str.
# You can define a string with either double quotes " or single quotes '.
# If the string you are creating actually has one of these two values in it,
# then you need to be careful to assure your code doesn't give an error.

my_string = 'this is a string!'
my_string2 = "this is also a string!!!"
# You can also include a \ in your string to be able to include one of these quotes:
this_string = 'Simon\'s skateboard is in the garage.'
print(this_string)
# Simon's skateboard is in the garage.
# If we don't use this, notice we get the following error:
# >>> this_string = 'Simon's skateboard is in the garage.'
#   File "<ipython-input-20-e80562c2a290>", line 1
#     this_string = 'Simon's skateboard is in the garage.'                          ^
# SyntaxError: invalid syntax

# The color highlighting is also an indication of the error you have in your string in this second case.
# There are a number of other operations you can use with strings as well. In this video you saw a few:

first_word = 'Hello'
second_word = 'There'
print(first_word + second_word)
# HelloThere

print(first_word + ' ' + second_word)
# Hello There

print(first_word * 5)

# HelloHelloHelloHelloHello
print(len(first_word))
# 5

# Unlike the other data types you have seen so far, you can also index into strings,
# but you will see more on this soon! For now, here is a small example.
# Notice Python uses 0 indexing - we will discuss this later in this lesson in detail.

first_word[0]
# H
#
first_word[1]
# e

# The len() function

# len() is a built-in Python function that returns the length of an object, like a string.
# The length of a string is the number of characters in the string. This will always be an integer.
# There is an example above, but here's another one:

print(len("ababa") / len("ab"))
# 2.5

# Quiz: Fix the Quote
# The line of code in the following quiz will cause a SyntaxError,
# thanks to the misuse of quotation marks. First run it with Test Run to view the error message.
# Then resolve the problem so that the quote (from Henry Ford) is correctly assigned to the variable ford_quote.

# TODO: Fix this string!
ford_quote = 'Whether you think you can, or you think you can\'t--you\'re right.'

# Quiz: Write a Server Log Message
# In this programming quiz, you’re going to use what you’ve learned
# about strings to write a logging message for a server.

# You’ll be provided with example data for a user, the time of their visit and the site they accessed.
# You should use the variables provided and the techniques you’ve learned to print a log message
# like this one (with the username, url, and timestamp replaced with values from the appropriate variables):

# Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20.

# Use the Test Run button to see your results as you work on coding this piece by piece.

username = "Kinari"
timestamp = "04:50"
url = "http://petshop.com/pets/mammals/cats"
print(username+ " accessed the site " + url + " at " + timestamp + "." )
# TODO: print a log message using the variables above.
# The message should have the same format as this one:
# "Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20."

# Quiz: len()
# Use string concatenation and the len() function to find the length of a certain
# movie star's actual full name. Store that length in the name_length variable.
# Don't forget that there are spaces in between the different parts of a name!

given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"

name_length = len(given_name + middle_names + family_name) + 2 # todo: calculate how long this name is

# Now we check to make sure that the name fits within the driving license character limit
# Nothing you need to do here
driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)
