# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.

# def symmetric(p):
#     print(p[0])
#     print(p)
#     list = 0
#     row = 0
#     column = 0
#     if len(p) != len(p[0]):
#         return False
#     else:
#         for e in p:
#             row = row + 1
#             list = list + 1
#         if p[list][row] == p[list][column]:
#                 print(p[list][row])
#                 print(p[list][column])


def symmetric(matrix):
    n = len(matrix)
    # Check if it's really a square matrix:
    for row in matrix:
        if len(row) != n:
            return False
    # Now check if it's symmetric:
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True



print(symmetric([["cat", "dog", "fish"],
                 ["dog", "dog", "dog"],
                 ["fish", "fish", "cat"]]))

#print(symmetric([[1, 2, 3],
#                 [2, 3, 4],
#                 [3, 4, 1]]))
# >>> True

# print symmetric([["cat", "dog", "fish"],
#                ["dog", "dog", "fish"],
#                ["fish", "fish", "cat"]])
# >>> True


# >>> False

# print symmetric([[1, 2],
#                [2, 1]])
# >>> True

# print symmetric([[1, 2, 3, 4],
#                [2, 3, 4, 5],
#                [3, 4, 5, 6]])
# >>> False

# print symmetric([[1,2,3],
#                 [2,3,1]])
# >>> False
