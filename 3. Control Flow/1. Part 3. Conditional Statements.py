# Indentation
# Some other languages use braces to show where blocks
# of code begin and end. In Python we use indentation to
# enclose blocks of code. For example, if statements use
# indentation to tell Python what code is inside and outside of different clauses.

# In Python, indents conventionally come in multiples of four spaces.
# Be strict about following this convention, because changing the
# indentation can completely change the meaning of the code.
# If you are working on a team of Python programmers, it's
# important that everyone follows the same indentation convention!

# Spaces or Tabs?
# The Python Style Guide recommends using 4 spaces to indent,
# rather than using a tab. Whichever you use, be aware that
# "Python 3 disallows mixing the use of tabs and spaces for indentation."

# First Example - try changing the value of phone_balance
phone_balance = 10
bank_balance = 50

if phone_balance < 10:
    phone_balance += 10
    bank_balance -= 10

print(phone_balance)
print(bank_balance)

# Second Example - try changing the value of number

number = 145
if number % 2 == 0:
    print("Number " + str(number) + " is even.")
else:
    print("Number " + str(number) + " is odd.")

# Third Example - try to change the value of age
age = 35

# Here are the age limits for bus fares
free_up_to_age = 4
child_up_to_age = 18
senior_from_age = 65

# These lines determine the bus fare prices
concession_ticket = 1.25
adult_ticket = 2.50

# Here is the logic for bus fare prices
if age <= free_up_to_age:
    ticket_price = 0
elif age <= child_up_to_age:
    ticket_price = concession_ticket
elif age >= senior_from_age:
    ticket_price = concession_ticket
else:
    ticket_price = adult_ticket

message = "Somebody who is {} years old will pay ${} to ride the bus.".format(age, ticket_price)
print(message)
