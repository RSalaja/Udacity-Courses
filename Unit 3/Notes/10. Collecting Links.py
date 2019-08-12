# Collecting Links
# Now we are ready to finish our web crawler!
# Let’s recap how the web crawler should work to find all the links that can be found from a seed
# page. We need to start by finding all the links on the seed page, but instead of just printing them
# like we did in Unit 2, we need to store them in a list so we can use them to keep going. We will go
# through all the links in that list to continue our crawl, and keep going as long as there are more
# pages to crawl.
# The first step to define a procedure get_all_links that takes as input a string that represents the
# text on a web page and produces as output a list containing all the URLs that are targets of link tags
# on that page.
# Get All Links
# Let’s recap the code we had from Unit 2:
# def print_all_links(page):
# while True:
# url, endpos = get_next_target(page)
# if url:
# print url
# page = page[endpos:]
# else:
# break
# We defined a procedure, get_next_target, that would take a page, search for the first link on that
# page, return that as the value of url and also return the position at the end of the quote is so we
# know where to continue.
# Then, we defined the procedure, print_all_links, that keeps going as long as there are more
# links on the page. It will repeatedly find the next target, print it out, and advance the page past the
# end position.
# What we want to do to change this is instead of printing out the URL each time we find one, we
# want to collect the URLs so we may use them to keep crawling and find new pages. To do this,
# we will create a list of all of the links we find. We change the print_all_links procedure into
# get_all_links so that we can use the output, which will be a list of links, which will correspond
# to the links we were originally printing out.