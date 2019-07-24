#   Structured Data (Introduction)
# The main new topic for Unit 3 is structured data. By the end of this unit, you will have finished
# building a simple web crawler.
# The closest thing you have seen to structured data so far is the string type introduced in Unit 1, and
# used in many of the procedures in Unit 2. A string is considered a kind of structured data because
# you can break it down into its characters and you can operate on sub-sequences of a string. This
# unit introduces lists, a more powerful and general type of structured data. Compared to a string
# where all of the elements must be characters, in a list the elements can be anything you want such
# as characters, strings, numbers or even other lists!
# The table below summarizes the similarities and differences between strings and lists.

#           String                                           List
# elements are characters                       elements may be any Python value
#
# surrounded by singled or double quotes        surrounded by square brackets
# s = 'yabba!'                                  p =  elements using <list>[<number>]
# # s[0] → 'y'                                    p[0] → 'y'
#
# # select sub-sequence using                     s[2:4] → 'bb'
# # <string>[<number> : <number>]['y','a','b','b','a','!']
#
# select elements using <string>[<number>]      select
# s[2:4] → 'bb'
# select sub-sequence using
# <list>[<number> : <number>]
# p[2:4] → ['b','b']
# immutable
# s[0] = 'b' → Error
# cannot change the value of a string
# mutable
# p[0] = 'b'
# changes the value of the first element of p
# Q-1: Quiz (Stooges)
# Define a variable, stooges, whose value is a list of the names of the Three Stooges: “Moe”, “Larry”,
# and “Curly.”
# Answer to Q-1
2
Q - 2: Quiz(Days in a
Month)
Given
the
variable:
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
define
a
procedure, how_many_days, that
takes as input
a
number
representing
a
month, and
outputs
the
number
of
days in that
month.
how_many_days(1) → 31
how_many_days(9) → 30
Answer
to
Q - 2
Nested
Lists
So
far, all
of
the
elements in our
lists
have
been
of
the
same
type: strings, numbers, etc.However,
there
are
no
restrictions
on
the
types
of
elements in a
list.Elements
of
a
list
can
be
any
type
you
want, you
can
also
mix and match
different
types
of
elements in a
list.
For
example:
mixed_up = ['apple', 3, 'oranges', 27,
            [1, 2, ['alpha', 'beta']]]
or a
more
useful
example:
beatles = [['John', 1940],
           ['Paul', 1942],
           ['George', 1943],
           ['Ringo', 1940]]
This
list
provides
information
about
the
names
of
the
Beatles
band
members, as well as when
they
were
born.Try
putting
this
into
your
interpreter.When
you
are
typing
your
code
into
the
interpreter and you
want
to
separate
data
onto
two
lines, do
so
after
a
comma
to
make
it
clear
to
the
interpreter
that
this is still
one
list.
beatles = [['John', 1940], ['Paul', 1942],
           ['George', 1943], ['Ringo', 1940]]
print
beatles
[['John', 1940], ['Paul', 1942], ['George', 1943], ['Ringo', 1940]]
print
beatles[3]
['Ringo', 1940]
3
You
can
also
use
indexing
again
on
the
list
that
results
to
obtain
an
inner
element:
print
beatles[3][0]
Ringo
Q - 3: Quiz(Countries)
Given
the
variable
countries
defined as:
countries = [['China', 'Beijing', 1350],
             ['India', 'Delhi', 1220],
             ['Romania', 'Bucharest', 21]
             ['United States', 'Washington', 307]]
Each
list
contains
the
name
of
a
country, its
capital, and its
approximate
population in millions.
Write
code
to
print
out
the
capital
of
India.
Answer
to
Q - 3
Q - 4: Quiz(Relative
Size)
What
multiple
of
Romania
's population is the population of China? To solve this, you need to divide
the
population
of
China
by
the
population
of
Romania.
Answer
to
Q - 4
Mutation
Mutation
means
changing
the
value
of
an
object.Lists
support
mutation.This is the
second
main
difference
between
strings and lists.
It
might
have
seemed
like
we
could
change
the
value
of
strings:
s = 'Hello'
s = 'Yello'
However, this
expression
changes
the
value
the
variable
s
refers
to, but
does
not change
the
value
of
the
string
'Hello'.As
another
example, consider
string
concatenation:
s = s + 'w'
This
operation
may
look
like
it is changing
the
value
of
the
string, but
that
's not what happens. It is
not modifying
the
value
of
any
string, but
instead is creating
a
new
string, 'Yellow', and assigning
the
variable
s
to
refer
to
that
new
string.
Lists
can
be
mutated, thus
changing
the
value
of
an
existing
list.Here is a
list:
4
p = ['H', 'e', 'l', 'l', 'o']
Mutate
a
list
by
modifying
the
value
of
its
elements:
p[0] = 'Y'
This
expression
replaces
the
value in position
0
of
p
with the string 'Y'.After the assignment, the
value
of
p
has
changed:
print
p
['Y', 'e', 'l', 'l', 'o']
p[4] = '!'
print
p
['Y', 'e', 'l', 'l', '!']
