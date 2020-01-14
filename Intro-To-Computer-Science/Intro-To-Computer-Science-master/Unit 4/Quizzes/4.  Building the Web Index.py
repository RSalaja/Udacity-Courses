# Building the Web Index (Building the Web Index)

# Q-4: Quiz (Add Page to Index)

# Define a procedure, add_page_to_index, that takes three inputs:

# - index
# - url (string)
# - content (string)

# It should update the index to include all of the word occurrences found in the page content by
# adding the url to the word's associated url list.

index = []


def add_to_index(index, keyword, url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword, [url]])

def lookup(index, word):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return []

def add_page_to_index(index,url,content):
    words=content.split()
    for word in words:
        add_to_index(index, word,url)

add_page_to_index(index,'fake.text',"This is a test")
print (index)

# >>> [['This', ['fake.text']], ['is', ['fake.text']], ['a', ['fake.text']],
# >>> ['test',['fake.text']]]

