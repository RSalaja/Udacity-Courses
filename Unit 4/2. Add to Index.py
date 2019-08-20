# Q-2: Quiz (Add to Index)
# Define a procedure, add_to_index, that takes three inputs:

# - an index [[<keyword>, [<url>, …]], …]
# - a keyword string
# - a url string

# If the keyword is already in the index, add the url to the list of urls associated with that keyword.
# If the keyword is not in the index, add an entry to to the index: [keyword, [url]]

# For example:

    # index = []
    # add_to_index(index, 'udacity', 'http://udacity.com')
    # add_to_index(index, 'computing', 'http://acm.org')

# This code starts with the empty list index. After the two lines of code the empty list will contain
# two lists beginning with the keywords, udacity and computing.

    # index = []
    # add_to_index(index, 'udacity', 'http://udacity.com')
    # add_to_index(index, 'computing', 'http://acm.org')
    # add_to_index(index, 'udacity', 'http://npr.org')

# In this code, udacity is already in the index and you don't want to add a new entry to the index
# itself. Since udacity is already in the index, what you want to do is add the new url to the list
# already associated with that keyword

def add_to_index(index, keyword, url):
    for entry in index:
        if entry [0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword, [url]])

index = []
add_to_index(index, 'udacity', 'http://udacity.com')
print(index)


# add_to_index(index, 'computing', 'http://acm.org')
# add_to_index(index, 'udacity', 'http://npr.org')
