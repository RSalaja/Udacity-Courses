# Strings

# A string is a sequence of characters surrounded by quotes; either single or double.
    # 'I am a string!'

# The only requirement is that the string must start and end with the same kind of quote.
    # "I prefer double quotes!"

# This allows you to include quotes inside of quotes as a character in the string.
    # "I'm happy I started with a double quote!"

# Using the interpreter, notice how the color of the input changes before and after
# you put quotes on both sides of the string.

# What happens when you do not include any quotes:
# print(Hello)

# Without the quotes, Python reads Hello as a variable that is undefined:
    # NameError: name 'Hello' is not defined

# As we saw above, Python will not print an undefined variable,
# which is why we get the name error.

# QUIZ: HELLO!!
# Define a variable, name, and assign to it a string that is your name.

name = 'Rafa'
print('Hello ' + name + ('!' * 9))

# Indexing Strings

# When you want to select sub-sequences from a string, it is called indexing.
# Use the square brackets [] to specify which part of the string you want to select

# QUIZ: CAPITAL UDACITY

# Write Python code that prints out Udacity (with a capital U),
# given the definition of s below.

s = 'audacity'
print('U' + (s[2:]))
