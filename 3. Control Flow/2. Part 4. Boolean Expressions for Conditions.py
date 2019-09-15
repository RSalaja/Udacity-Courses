# Quiz: Using Truth Values of Objects
# The code below is the solution to the Which Prize quiz you've seen previously.
# You're going to rewrite this based on what you've learned about truth values.

# You will use a new variable prize to store a prize name if one was won,
# and then use the truth value of this variable to compose the result message.
# This will involve two if statements.

# 1st conditional statement: update prize to the correct prize name based on points.
# 2nd conditional statement: set result to the correct phrase based on whether prize is evaluated as True or False.

# If prize is None, result should be set to "Oh dear, no prize this time."
# If prize contains a prize name, result should be set to
# "Congratulations! You won a {}!".format(prize).
# This will avoid having the multiple result assignments for different prizes.

points = 174  # use this input when submitting your answer

# set prize to default value of None
prize = None

# use the value of points to assign prize to the correct prize name
if points <= 50:
    prize = "wooden rabbit"
elif 151 <= points <= 180:
    prize = "wafer-thin mint"
elif points >= 181:
    prize = "penguin"

# use the truth value of prize to assign result to the correct message
if prize:
    result = "Congratulations! You won a {}!".format(prize)
else:
    result = "Oh dear, no prize this time."

print(result)