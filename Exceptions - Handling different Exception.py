# Handling Different Exceptions
from argparse import ZERO_OR_MORE

try:
    age = int(input("Age: "))
    xfactor = 10 / age
except ValueError:
    print("You didn't enter a valid age.")  # output : Age: 0 - we get an error because we cannot divide a number by 0
except ZeroDivisionError:
    print("Age cannot be 0.")  # output : Age: 0
                               #          Age cannot be 0.
else:
    print("No exceptions were thrown.")

# Let's imagine if the user enters 0 for the age , you want to print the exact same error message.
try:
    age = int(input("Age: "))
    xfactor = 10 / age
except ValueError:
    print("You didn't enter a valid age.")
except ZeroDivisionError:
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")

# the above code looks like a repetitive, we have repeated the same message so that means if we want to change this message in future, we have to change in two places
# There is a better way to handle this situation
try:
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):   # in front of this except clause, we can specify multiple types of exceptions. So if the exception that is strong matches any of those exceptions then the code that we have in the except block will be executed. We need to add () to specify multiple types of exceptions separated by comma
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")

# Note:
# When python executes the code that we have in the try block, if any of these statements throws an exception that matches one of the
# except clauses, that except clause is executed and the other except clauses are ignored.
