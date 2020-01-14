# Print All Links (Print All links)

# Q-23: Quiz (Print All Links)
# In the following code, fill in the test condition for the while loop and the rest of the else statement:
    # def print_all_links(page):
        # while ________:                           # what goes as the test condition for the while?
            # url, endpos = get_next_target(page)
            # if url:                               # test whether the url you got back is None
                # print url
                # page = page[endpos:]              # advance page to next position
            # else:                                 # if there was no valid url, then get_next_target did not

def print_all_links(page):
    while True:
        url, endpos = get_next_target(page)
        if url:
            print(url)
            page = page[endpos:]
        else:
            break
    print_all_links('this <a href="test1">link 1</a> is <a href="+Unit 2 Quizzes">link2 < / a > a < ahref = "test3" > link3 < / a > ')

