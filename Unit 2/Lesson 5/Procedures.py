# Procedures and Control (Introduction to Web Browsers)

# 1. Procedures - a way to package code so it can be reused with different inputs.
# 2. Control - a way to have the computer execute different instructions depending on the data
# (instead of just executing instructions one after the other).

# Recall this code from then end of Unit 1:
    # page = ...contents from some web page
    # start_link = page.find('<a href=')
    # start_quote = page.find('"', start_link)
    # end_quote = page.find('"', start_quote + 1)
    # url = page[start_quote + 1:end_quote]
    # print url

# This finds and prints the first link on the page. To keep going, we could update the value of page to
# be the characters from the end_quote, and repeat the same code again:
    # page = page[end_quote:]
    # start_link = page.find('<a href=')
    # start_quote = page.find('"', start_link)
    # end_quote = page.find('"', start_quote + 1)
    # url = page[start_quote + 1:end_quote]
    # print url

    # page = page[end_quote:]
    # start_link = page.find('<a href=')
    # start_quote = page.find('"', start_link)
    # end_quote = page.find('"', start_quote + 1)
    # url = page[start_quote + 1:end_quote]
    # print url

# Clearly, this is tedious work. In addition to being tedious,
# repeating the same code over and over again like this won’t work well because some pages
# only have a few links while other pages will have more links than the number of repetitions.

# Procedures: abstract code from its inputs
# If statements: write code that executes differently depending on the data
# While loops: repeat the same operations many times

# Procedural Abstraction (Motivating Procedures)

# Procedural abstraction is a way to write code once that works on any number of different data
# values. By turning our code into a procedure, we can use that code over and over again with
# different inputs to get different behaviors.

# Procedures (Introducing Procedures)

# A procedure takes in inputs, does some processing, and produces outputs.

# For example, the + operator is a procedure where the inputs are two numbers and the output is
# the sum of those two numbers. The + operator looks a little different from the procedures we will
# define since it is built-in to Python with a special operator syntax. In this unit you will learn how to
# write and use your own procedures.

# Here is the Python grammar for writing a procedure:
    # def <name>(<parameters>):
    # <block>

# The keyword def is short for “define”.

# <name> is the name of a procedure. Just like the name of a variable, it can be any string that starts
# with a letter and followed by letters, number and underscores.

# <parameters> are the inputs to the procedure. A parameter is a list of zero or more
# names separated by commas: <name>, <name>,... Remember that when you name your
# parameters, it is more beneficial to use descriptive names that remind you of what they mean.
# Procedures can have any number of inputs. If there are no inputs, the parameter list is an empty set
# of closed parentheses: ().

# After the parameter list, there is a : (colon) to end the definition header.

# The body of the procedure is a <block>, which is the code that implements the procedure. The
# block is indented inside the definition. Proper indentation tells the interpreter when it has reached
# the end of the procedure definition.

# Let’s consider how to turn the code for finding the first link into a get_next_target procedure
# that finds the next link target in the page contents. Here is the original code:
    # start_link = page.find('<a href=')
    # start_quote = page.find('"', start_link)
    # end_quote = page.find('"', start_quote + 1)
    # url = page[start_quote + 1:end_quote]

# Next, to make this a procedure, we need to determine what the inputs and outputs are.
