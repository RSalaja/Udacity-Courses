# If Statements (If Statements)

# An if statement provides a way to control what code executes based on the result of a test
# expression. Here is the grammar of the if statement:
    # if <TestExpression>:
    # <block>

# In this statement, the code in the <block> runs only if the value of the test expression is True.
# Similar to procedures, the end of the if statement block is determined by the indentation.

# Here is an example where we use an if statement to define a procedure that returns the absolute
# value of its input:
# def absolute(x):
    # if x < 0:
    # x = -x
    # return x

# Q-12: Quiz (If Statements)
# Define a procedure, bigger, that takes in two numbers as inputs, and outputs the greater of the two
# inputs.
# bigger(2, 7) → 7
# bigger(3, 2) → 3
# bigger(3, 3) → 3

def bigger(a, b):
    if a > b:
        return a
    return b
