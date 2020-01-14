# Add To Index

# Q-2: Quiz (Add to Index)
# Define a procedure, add_to_index, that takes three inputs:

# - an index [[<keyword>, [<url>, …]], …]
# - a keyword string
# - a url string

# If the keyword is already in the index, add the url to the list of urls associated with that keyword.
# If the keyword is not in the index, add an entry to to the index: [keyword, [url]]

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
