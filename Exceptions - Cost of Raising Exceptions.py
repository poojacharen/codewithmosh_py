# Cost of Raising Exceptions

from timeit import timeit  # with this function we can calculate the execution time and some python code

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


calculate_xfactor(-1)  # output - we get an error because we didn't have a try block
# to fix the above issue

try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)   # output - Age cannot be 0 or less.
"""

print("first code=", timeit(code1, number=10000))  # we have a keyword argument (number=), we set this to the number of times we want to execute this piece of code
                          # now this function returns the execution time of this piece of code after 10,000 repetition
        # output : after running this code we got 10,000 messages saying Age cannot be 0 or less.

# refer course again if any doubt cause mosh has duplicated the above code with code2 = ""
