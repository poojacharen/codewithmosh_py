# Strings

course = "Python Programming"
print(len(course))

# If we want to access the specific char in a string, we use [] to get a specific element or a specific char
print(course[0]) # 0 is an index, output is P
print(course[-1]) # now the output is g

# Using the same above syntax we can slice the string, [:] use this notation to slice a string
print(course[0:3]) # this returns 3 characters ie., Pyt, the character of this index is 0,1,2. the index 3 is not included
print(course[0:]) # this gives the entire string Python Programming
print(course[:3]) # this gives the output as Pyt
print(course[:]) # this returns the copy of the original string, output : Python Programming
