# Building the Web Index (Building the Web Index)

# To build your web index you want to find a way to separate all the words on a web page. It is
# possible to use the concepts you've already seen to build a procedure to do this, however, Python
# has a built-in operation that will make this much simpler.

# Split. When you invoke the split operation on a string the output is a list of the words in the string.
    # <string>.split()
    # [<word>, <word>, … ]

# For example,
quote = "In Washington, it's dog eat dog. In academia, it's exactly the opposite. --- Robert Reich"
print(quote.split())
# ['In', 'Washington,', "it's", 'dog', 'eat', 'dog.', 'In', 'academia,',
# "it's", 'exactly', 'the', 'opposite.', '---', 'Robert', 'Reich']

# This operation does a pretty good job of separating out the words in the list so that they will be
# useful. However, in the case of 'Washington,'which was followed by a comma in the quote, for
# the keyword you would not want to include the comma. While this isn't perfect, it is going to good
# enough for now.

# Here is another example of how split works, using triple quotes ("""). Using the triple quotes you
# can define one string over several lines:
quote = """
        There's no buisiness like show business,
        but there are several businesses like accounting.
        (David Leterman)
        """
print(quote.split())
# ["There's", 'no', 'buisiness', 'like', 'show', 'business,', 'but',
# 'there', 'are', 'several', 'businesses', 'like', 'accounting.'
# '(David', 'Leterman)']
# This still has similar problems to the first example, where the parentheses are included in the word
# '(David'.


# Q-4: Quiz (Add Page to Index)

# Define a procedure, add_page_to_index, that takes three inputs:

# - index
# - url (string)
# - content (string)

# It should update the index to include all of the word occurrences found in the page content by
# adding the url to the word's associated url list.

# For example:

# index = []
# add_page_to_index(index, 'fake.test', "This is a test")
# print index
# [['This', ['fake.test']], ['is', ['fake.test']], ['a', ['fake.test']],
# ['test', ['fake.test']]]

# Printing at index[0] :

# index = []
# add_page_to_index(index, 'fake.test', "This is a test")
# print index[0]
# ['This', ['fake.test']]

# Printing at index[1] :

# index = []
# add_page_to_index(index, 'fake.test', "This is a test")
# print index[1]
# ['is', ['fake.test']]

# Now, add a page called real.test:

# index = []
# add_page_to_index(index, 'fake.test', "This is a test")
# add_page_to_index(index, 'real.test', "This is not a test")

# print index
# [['This', ['fake.test', 'real.test']], ['is', ['fake.test',
# 'real.test']], ['a', ['fake.test']], ['test', ['fake.test',
# 'real.test']], ['not', ['real.test']]]

# Have a look at the entries when you index[1]:

# index = []

# add_page_to_index(index, 'fake.test', "This is a test")
# add_page_to_index(index, 'real.test', "This is not a test")

# print index
# print index[1]
# [['This', ['fake.test', 'real.test']], ['is', ['fake.test',
# 'real.test']], ['a', ['fake.test']], ['test', ['fake.test',
# 'real.test']], ['not', ['real.test']]]
# ['is', ['fake.test', 'real.test']]

def add_to_index(index, keyword, url):
    for entry in index:
        if entry [0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword, [url]])

index = []
add_to_index(index, 'udacity', 'http://udacity.com')
print(index)