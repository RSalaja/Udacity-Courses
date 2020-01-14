# Zip and Enumerate
# zip and enumerate are useful built-in functions that can come in handy when dealing with loops.

# Zip
# zip returns an iterator that combines multiple iterables into one sequence of tuples.
# Each tuple contains the elements in that position from all the iterables. For example, printing
print(list(zip(['a', 'b', 'c'], [1, 2, 3])))
# would output [('a', 1), ('b', 2), ('c', 3)].

# Like we did for range() we need to convert it to a list or iterate through it with a loop to see the elements.

# You could unpack each tuple in a for loop like this.

letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))

# In addition to zipping two lists together, you can also unzip a list into tuples using an asterisk.

some_list = [('a', 1), ('b', 2), ('c', 3)]
letters, nums = zip(*some_list)

# Enumerate
# enumerate is a built in function that returns an iterator of tuples containing indices and values of a list.
# You'll often use this when you want the index along with each element of an iterable in a loop.

letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)


# Quiz: Zip Coordinates
    # Use zip to write a for loop that creates a string specifying the label
    # and coordinates of each point and appends it to the list points. Each string should be formatted as
    # label: x, y, z. For example, the string for the first coordinate should be F: 23, 677, 4.

x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
# write your for loop here

for point in zip(labels, x_coord, y_coord, z_coord):
    points.append("{}: {}, {}, {}".format(*point ))

for point in points:
    print(point)
