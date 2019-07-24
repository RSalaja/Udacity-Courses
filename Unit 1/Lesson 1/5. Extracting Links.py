# Extracting Links

# A web page is really just a long string of characters.
# Your browser renders the web page in a way that looks
# more attractive than just the string of characters.
# You can view the string of characters.
# Select View Page Source from the menu.
# The raw string for the web page pops up in a new window:

# For our web crawler, the important thing is to find the links to other web pages in the page. We can
# find those links by looking for the anchor tags that match this structure:
    # <a href="<url>">

# For example, here is a link to the News/Blag page:
    # <a href=http://blag.xkcd.com/>

# To build our crawler, for each web page we want to find all the link target URLs on the page.
# We want to keep track of them and follow them to find more content on the web.

    # For this unit, we will do the first step which is to extract the first target URL from the page.
    # In Unit 2, we will see how to keep going to get all the link targets, and in Unit 3,
    # we will see how to keep track of them to be able to crawl the target pages.

        # For now, our goal is to take the text from a web request and find the first link target in that text.
        # We can do this by finding the anchor tag, <a href=", and then extract from that tag the URL that is
        # found between the double quotes.

# We will assume that with the page's contents in a variable, page.

# QUIZ: EXTRACTING LINKS

# Write Python code that initializes the variable
# start_link to be the value of the position
# where the first '<a href=' occurs in a page.

page = '''<div id="top_bin"> <div id="top_content" class="width960">
   <div class="udacity float-left"> <a href="/">'''

start_link = page.find('<a href=')
print(start_link)


# QUIZ: FINAL QUIZ

# Write Python code that assigns to the
# variable url a string that is the value
# of the first URL that appears in a link
# tag in the string page.
# Your code should print http://udacity.com
# Make sure that if page were changed to

# page = '<a href="http://udacity.com">Hello world</a>'

# that your code still assigns the same value to the variable 'url',
# and therefore still prints the same thing.

# page = contents of a web page
page = ('<div id="top_bin"><div id="top_content" class="width960">'
        '<div class="udacity float-left"><a href="http://udacity.com">')
start_link = page.find('<a href=')

start_quote = (page.find('"', start_link))
end_quote = (page.find('"', start_quote + 1))
url = (page[start_quote + 1:end_quote])
print(url)
