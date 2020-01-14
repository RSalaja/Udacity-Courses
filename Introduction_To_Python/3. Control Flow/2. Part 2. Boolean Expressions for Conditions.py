# Good and Bad Examples
# Here are some things to keep in mind while writing boolean expressions for your if statements.

# 1. Don't use True or False as conditions
# # Bad example
# if True:
#     print("This indented code will always get run.")

# While "True" is a valid boolean expression, it's not useful as a condition since it always evaluates to True,
# so the indented code will always get run. Similarly, if False is not a condition you should use
# either - the statement following this if statement would never be executed.

# # Another bad example
# if is_cold or not is_cold:
#     print("This indented code will always get run.")

# Similarly, it's useless to use any condition that you know will always evaluate to True,
# like this example above. A boolean variable can only be True or False, so either
# is_cold or not is_cold is always True, and the indented code will always be run.

# 2. Be careful writing expressions that use logical operators
# Logical operators and, or and not have specific meanings that aren't quite the
# same as their meanings in plain English. Make sure your boolean expressions are
# being evaluated the way you expect them to.

# # Bad example
# if weather == "snow" or "rain":
#     print("Wear boots!")
# This code is valid in Python, but it is not a boolean expression, although it reads l
# ike one. The reason is that the expression to the right of the or operator, "rain",
# is not a boolean expression - it's a string! Later we'll discuss what happens when you
# use non-boolean-type objects in place of booleans.

# 3. Don't compare a boolean variable with == True or == False
# This comparison isn’t necessary, since the boolean variable itself is a boolean expression.

# # Bad example
# if is_cold == True:
#     print("The weather is cold!")
# This is a valid condition, but we can make the code more readable
# by using the variable itself as the condition instead, as below.

# # Good example
# if is_cold:
#     print("The weather is cold!")
# If you want to check whether a boolean is False, you can use the not operator.
