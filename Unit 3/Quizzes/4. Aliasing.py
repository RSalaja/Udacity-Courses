# Aliasing

# Q-6: Quiz
# What is the value of agent[2] after running the following code:

spy = [0, 0, 7]
agent = spy
spy[2] = agent[2] + 1

# Q-7: Quiz (Replace Spy)
# Define a procedure, replace_spy, that takes as its input a list of three
# numbers and increases the value of the third element of the list to be one more than its previous value.
# Here is an example of the behavior that you want:
    # spy = [0, 0, 7]
    # replace_spy(spy)
    # print(spy)
    # [0, 0, 8]

spy = [0, 0, 7]

def replace_spy(p):
    p[2] = p[2] + 1

replace_spy(spy)
print(spy)

