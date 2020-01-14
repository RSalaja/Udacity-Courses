# Another important string method: split()
# A helpful string method when working with strings is the .split method.
# This function or method returns a data container called a list that contains the words from the input string.
# We will be introducing you to the concept of lists in the next video.

# The split method has two additional arguments (sep and maxsplit).
# #The sep argument stands for "separator".
# It can be used to identify how the string should be split up
# (e.g., whitespace characters like space, tab, return, newline; specific punctuation (e.g., comma, dashes)).
# If the sep argument is not provided, the default separator is whitespace.

# True to its name, the maxsplit argument provides the maximum number of splits.
# The argument gives maxsplit + 1 number of elements in the new list,
# with the remaining string being returned as the last element in the list.
# You can read more about these methods in the Python documentation too.

# Here are some examples for the .split() method.
# 1. A basic split method:
new_str = "The cow jumped over the moon."
new_str.split()
# Output is:
    # ['The', 'cow', 'jumped', 'over', 'the', 'moon.']

# 2. Here the separator is space, and the maxsplit argument is set to 3.
new_str.split(' ', 3)
# Output is:
    # ['The', 'cow', 'jumped', 'over the moon.']

# 3. Using '.' or period as a separator.
new_str.split('.')
# Output is:
    # ['The cow jumped over the moon', '']

# 4. Using no separators but having a maxsplit argument of 3.
new_str.split(None, 3)
# Output is:
# ['The', 'cow', 'jumped', 'over the moon.']

# Quiz: String Methods Coding Practice
# Below, we have a string variable that contains the first verse of the poem,
# 'If' by Rudyard Kipling.
# Remember, \n is a special sequence of characters that causes a line break (a new line).

# What is the length of the string variable verse?
# What is the index of the first occurrence of the word 'and' in verse?
# What is the index of the last occurrence of the word 'you' in verse?
# What is the count of occurrences of the word 'you' in the verse?
# You will need to refer to Python's string methods documentation
verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse, "\n")

print("Verse has a length of {} characters.".format(len(verse)))
print("The first occurence of the word 'and' occurs at the {}th index.".format(verse.find('and')))
print("The last occurence of the word 'you' occurs at the {}th index.".format(verse.rfind('you')))
print("The word 'you' occurs {} times in the verse.".format(verse.count('you')))