# Aliasing
# Now that you know how a mutation modifies an existing list object,
# you will really be able to see
# how this is differs from strings when you introduce a new variable.

p = ['H', 'e', 'l', 'l', 'o']
p[0] = 'Y'
q = p

# After this assignment, p and q refer to the same list: ['Y', 'e', 'l', 'l', 'o'].
# Suppose we use an assignment statement to modify one of the elements of q:

q[4] = '!'

# This also changes the value of p:

print(p)
['Y', 'e', 'l', 'l', 'o']

# After the q = p assignment, the names p and q refer to the same list, so anything we do that
# mutates that list changes that value both variables refer to.
# It is called aliasing when there are two names that refer to the same object. Aliasing is very
# useful, but also can be very confusing since one mutation can impact many variables. If something
# happens that changes the state of the object, it affects the state of the object for all names that refer
# to that object.
# Strings are Immutable. Note that we cannot mutate strings, since they are immutable objects. Try
# mutating a string in the interpreter:

s = 'Hello'
s[0] = 'Y'

# 'str' object does not support item assignment
# Mutable and Immutable Objects. The key difference between mutable and immutable objects,
# is that once an object is mutable, you have to worry about other variables that might refer to the
# same object. You can change the value of that object and it affects not just variable you think you
# changed, but other variables that refer to the same object as well.
# Here is another example:

p = ['J', 'a', 'm', 'e', 's']
q = p
p[2] = 'n'

# Both p and q now refer to the same list:

['J', 'a', 'n', 'e', 's']

# What happens if you assign p a new value, as in:

p = [0, 0, 7]

# In this case, the value of p will change, but the value of q will remain the same. The assignment
# changes the value the name p refers to, which is different from mutating the object that p refers to.

# Q-6: Quiz
# What is the value of agent[2] after running the following code:

spy = [0, 0, 7]
agent = spy
spy[2] = agent[2] + 1

# Q-7: Quiz (Replace Spy)
# Define a procedure, replace_spy, that takes as its input a list of three numbers and increases the
# value of the third element of the list to be one more than its previous value. Here is an example of
# the behavior that you want:

spy = [0, 0, 7]
replace_spy(spy)
print(spy)
[0, 0, 8]
