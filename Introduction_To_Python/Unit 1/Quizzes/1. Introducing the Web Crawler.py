# What is a Web Crawler:

# A web crawler is a program that collects content from the web.
# A web crawler finds web pages by starting from a seed page
# and following links to find other pages, and following links from the other
# pages it finds, and continuing to follow links until it has found many web pages.



# Here is the process that a web crawler follows:
# Start from one preselected page. We call the starting page the "seed" page.
# Extract all the links on that page. (This is the part we will work on in this unit and Unit 2.)
# Follow each of those links to find new pages.
# Extract all the links from all of the new pages found.
# Follow each of those links to find new pages.
# Extract all the links from all of the new pages found.

# This keeps going as long as there are new pages to find, or until it is stopped.

# In this unit we will be writing a program to extract the first link from a given web page. In Unit 2,
# we will figure out how to extract all the links on a web page. In Unit 3, we will figure out how to
# keep the crawl going over many pages.
