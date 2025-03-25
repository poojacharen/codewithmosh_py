# Type Conversions
# input() - get the input from the user

x = input("x: ")
y = int(x) + 1
print(f"x: {x}, y: {y}")

# int(x)
# float(x)
# bool(x)
# str(x)

# bool(x) are tricky because in python there is a concept called truthy and falsy values.
# these values are not exactly boolean true or false but they can be interpreted as boolean true or false
# Falsy Values in Py
# "" - empty string
# 0
# None - represents the absence of a value
# whenever we use the above falsy values, in boolean context, we will get false and anything else will be true
# eg:
# bool(0) - false
# bool(1) - true
# bool(-1) - true
# bool(6) - true
# bool("") - false
# bool("false") - true (because this is not an empty string)
