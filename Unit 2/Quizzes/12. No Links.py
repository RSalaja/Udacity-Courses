# No Links (No Links)

# Q-22: Quiz (No Links)
# Think about making get_next_target more useful in the case where the input does not contain
# any link. This is something you can do! Here is a hint:
# def get_next_target(page):
# start_link = page.find('<a href=') # HINT: put something into the code here

# start_quote = page.find('"', start_link)
# end_quote = page.find('"', start_quote + 1)
# url = page[start_quote + 1:end_quote]
# return url, end_quote

# url, endpos = get_next_target('Not "good" at all!')
# print url
# Modify the get_next_target procedure so that if there is a link it behaves as before, but if
# there is no link tag in the input string, it outputs None, 0.

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote
    url, endpos = get_next_target('Not "good" at all!' > link! < / a >)
    if url:
        print("Here!")
    else:
        print("Not here!")
    print(url)
