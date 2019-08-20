# Introduction (Introduction)
# In unit 4 you are going to learn how to finish the code for your search engine and how to respond
# to a query when someone wants the given web pages that correspond to a given keyword. You will
# also learn about how networks and the world wide web work to understand more about how you
# can build up your search index.
# The main new computer science idea you will learn is how to build complex data structures. You
# will learn how to design a structure that you can use so that you can respond to queries without
# needing to rescan all the web pages every time you want to respond to a query. The structure
# you will build for this is called an index. The goal of an index is to map a keyword and where that
# keyword is found. For example, in the index of a book you can see a page number which serves as a
# map to where a term or concept can be found. The key ideas in index will allow us to find references
# to what we want. With a search engine the index gives you a way for a keyword to map to a list of
# web pages, which are the urls where those particular web pages appear. Once you have done the
# work of building an index, then the look-ups are really fast

# Q-1: Quiz (Data Structures)
# Deciding on data structures is one of the most important parts of building software. As long as you
# pick the right data structure, the rest of the code will be a lot easier to write.
# Which of these data structures would be a good way to represent the index for your search engine?
# a. [<keyword1>, <url1, 1>, <url1, 2>, <keyword2>, …]
# b. [[<keyword1>, <url1, 1>, <url1, 2>], [<keyword2>, <url2, 1>, …]
# c. [[<url1, 1>, [<keyword1>, <keyword23>, … ]], [<url2, 1>, [<keyword2>, …]]
# d. [[<keyword1>, <url1, 1>, <url1, 2>]], [<keyword2>, [<url2, 1>]], …]