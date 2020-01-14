# Q-5: Quiz (Finishing the Web Crawler)
# Fill in the missing line using the variable content.

# def crawl_web(seed):
    # tocrawl = [seed]
    # crawled = []
    # index = []
    # while tocrawl:
        # page = tocrawl.pop()
        # if page not in crawled:
            # content = get_page(page)
            # FILL IN THE MISSING LINE BELOW HERE
            # union(tocrawl,get_all_links(content))
            # crawled.append(page)
        # return index

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            union(tocrawl,get_all_links(content))
            crawled.append(page)
        return index
