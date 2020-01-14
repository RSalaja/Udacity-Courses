# Q-3: Quiz (Lookup)

# Define a procedure, lookup, that takes two inputs:
# - An index:
                # A list where each element of the list is a list containing a
                # keyword and a list as its second element.
                # The second list element is a list of urls where that keyword appears.
# -The keyword to lookup
                # The output should be a list of the urls associated with the keyword.
                # If the keyword is not in the
                # index, the output should be an empty list.
# For example:
# lookup('udacity') → ['http://udacity.com', 'http://npr.org']

def lookup(index, word):
    for entry in index:
        if entry [0] == keyword:
            return entry [1]
    return []

def add_to_index(index, keyword, url):
    for entry in index:
        if entry [0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword, [url]])

index = []
add_to_index(index, 'udacity', 'http://udacity.com')
add_to_index(index, 'computing', 'http://acm.org')
add_to_index(index, 'udacity', 'http://npr.org')

print(lookup(index, 'udacity'))

