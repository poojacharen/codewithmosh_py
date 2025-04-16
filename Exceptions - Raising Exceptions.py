# Raising Exceptions

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
