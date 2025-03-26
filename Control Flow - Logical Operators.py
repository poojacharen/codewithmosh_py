# Logical Operators
# Three logical operators : and, or, not
# Eg : Imagine we are building an app for processing loans

high_income = True
good_credit = False

if high_income and good_credit:
    print("Eligible")
else:
    print("Not Eligible")
# and operator: With and operator, if both conditions are True, it is True

if high_income or good_credit:
    print("Eligible")
else:
    print("Not Eligible")
# or operator: if one of the condition is true, if both the conditions are false its false
high_income = True
good_credit = False
student = False

if not student:
    print("Eligible")
else:
    print("Not Eligible")
# not operator: not true - false, not false - true

# Using operators with complex conditions
# Eg: A person can be eligible if they have either high income or good credit and it should not be a student

high_income = True
good_credit = False
student = False

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligible")
