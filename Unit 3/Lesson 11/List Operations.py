# List Operations

# Append:
    # The append method adds a new element to the end of a list.
    # The append method mutates the list that it is invoked on,
    # it does not create a new list.
    # The syntax for the append method is:

        # <list>.append(<element>)

    # For example, assume you want to end up with four stooges
    # in your list, instead of just three:

        # stooges = ['Moe', 'Larry', 'Curly']
        # stooges.append('Shemp')
        # ['Moe', 'Larry', 'Curly', 'Shemp']

# Concatenation:
    # The + operator can be used with lists and is very
    # similar to how it is used to concatenate strings.
    # It produces a new list, it does not mutate either of the input lists.

        # <list> + <list> → <list>

    # For example,

        # [0, 1] + [2, 3] → [0, 1, 2, 3]

# Length:
    # The len operator can be used to find out the length of an object.
    # The len operator works for many things other than lists,
    # it works for any object that is a collection of things including strings.
    # The output from len is the number of elements in its input.

        # len(<list>) → <number>

    # For example, len([0,1]) → 2. Note that len only counts the outer elements:

        # len(['a', ['b', ['c', 'd']]]) → 2

    # since the input list contains two elements: 'a' and ['b', ['c', 'd']].
    # When you invoke len on a string, the output is the number of elements in the string.

        # len("Udacity") → 7

# QUIZ: LEN

# What is the value of len(p) after running the following code:
p = [1, 2]
p.append(3)
p = p + [4, 5]
len(p)
# Ans: 5
print(len(p))

# Q-9: Quiz

# What is the value of len(p) after running:
p = [1, 2]
q = [3, 4]
p.append(q)
# len(p) → ?
print(len(p))
