# Iterables

# print(type(5)) # op: class 'int'
# print(type(range(5))) # op: class 'range'

# range is a complex type
# range object is iterable which means you can iterate over it and use it in a for loop
# ie,.. we write a code like this
# for x in range(5):
# Strings are also iterable
for x in "Python":  # so in each iteration x will hold 1 character in this string
   print(x)

# Another complex type called List, which we used to store a list of objects []
for x in [1, 2, 3]:
    print(x)
