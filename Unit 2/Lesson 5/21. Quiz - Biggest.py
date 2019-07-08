# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.

def biggest(a, b, c):
    global d
    if a > b or c:
        d = a

    if b > a or c:
        d = b

    if c > a or b:
        d = c
    return d


print(biggest(3, 6, 9))
# >>> 9

print(biggest(6, 9, 3))
# >>> 9

print(biggest(9, 3, 6))
# >>> 9

print(biggest(3, 3, 9))
# >>> 9

print(biggest(9, 3, 9))
# >>> 9
