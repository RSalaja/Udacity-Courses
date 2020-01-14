# While Loops
# For loops are an example of "definite iteration" meaning that the loop's
# body is run a predefined number of times. This differs from "indefinite iteration"
# which is when a loop repeats an unknown number of times and ends when some condition is met,
# which is what happens in a while loop. Here's an example of a while loop.

card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []

# adds the last element of the card_deck list to the hand list
# until the values in hand add up to 17 or more
while sum(hand) < 17:
    hand.append(card_deck.pop())

# This example features two new functions.
# sum returns the sum of the elements in a list, and pop is a
# list method that removes the last element from a list and returns it.

# Components of a While Loop
# 1. The first line starts with the while keyword, indicating this is a while loop.

# 2. Following that is a condition to be checked. In this example, that's sum(hand) <= 17.

# 3. The while loop heading always ends with a colon :.

# 4. Indented after this heading is the body of the while loop.
# If the condition for the while loop is true, the code lines in the loop's body will be executed.

# 5. We then go back to the while heading line, and the condition is evaluated again.
# This process of checking the condition and then executing the loop repeats until the condition becomes false.

# 6. When the condition becomes false, we move on to the line following the body of the loop, which will be unindented.

# The indented body of the loop should modify at least one variable in the test condition.
# If the value of the test condition never changes, the result is an infinite loop!

# Quiz: Count By
# Suppose you want to count from some number start_num by another
# number count_by until you hit a final number end_num. Use break_num
# as the variable that you'll change each time through the loop.
# For simplicity, assume that end_num is always larger than start_num and count_by is always positive.

# Before the loop, what do you want to set break_num equal to?
# How do you want to change break_num each time through the loop?
# What condition will you use to see when it's time to stop looping?

# After the loop is done, print out break_num,
# showing the value that indicated it was time to stop looping.
# It is the case that break_num should be a number that is the first number larger than end_num.

start_num = 0   # provide some start number
end_num = 10    # provide some end number that you stop when you hit
count_by = 1    # provide some number to count by
break_num = 0

# write a while loop that uses break_num as the ongoing number to
while start_num<=end_num:
    start_num = start_num + count_by
    break_num = break_num + 1

#   check against end_num


print("This is the break number {}\nThis is the end number {}".format(break_num, end_num))
