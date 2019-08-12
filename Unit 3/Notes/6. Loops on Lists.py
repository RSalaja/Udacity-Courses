# Loops on Lists

# Since lists are collections of things,it is very useful
# to be able to go through a list and do something with every element.

# In Unit 2, we introduced the while loop:
# while <TestExpression>:
# <Block>

# If the test expression is True, the <Block> is executed.
# At the end of the block, execution continues by re-evaluating
# the test expression, and continuing to execute the block as
# long as the test expression evaluates to true.

# QUIZ

# Define a procedure called print_all_elements that takes as
# input a list p and prints out every
# element of that list. Here is a start:
def print_all_elements(p):
    i = 0
    while i < len(p):
        print
    p[i]
    i = i + 1
