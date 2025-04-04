# Tuples - It is basically a read-only list. We can use it to contain a sequence of objects but we cannot modify this sequence.
# We cannot add a new object to it, we cannot remove an existing object and also we cannot modify an existing object

point = (1, 2)  # we can also remove the parenthesis()  still python takes it as a tuple
print(type(point))  # the type is tuple <class 'tuple'>

# if we want to define empty tuple, we need to define a empty parenthesis
point = ()
print(type(point))  # <class 'tuple'>

# Similar to lists, we can concatenate two tuples
point = (1, 2) + (3, 4)
print(point)  # output : (1, 2, 3, 4)

# We can also use a * operator to repeat a tuple
point = (1, 2) * 4
print(point)    # output : (1, 2, 1, 2, 1, 2, 1, 2)

# We can also convert a list to a tuple
# Let's say we have a list of two numbers, to convert this list to a tuple, we call a tuple function
# tuple() this function takes an iterable, so we can pass any iterable here and this function will return a tuple
point = tuple([1, 2])
print(point)  # output : (1, 2) - a tuple of two numbers

# Also, we can also pass a string because strings are iterable
point = tuple("Hello World!!")
print(point)  # output : ('H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!', '!')

# Similar to lists, we can access individual item using an index
point = (1, 2, 3)
print(point[0])  # output : 1

# Also we can get a range of items
point = (1, 2, 3, 4)
print(point[0:5]) # output : (1, 2, 3, 4)
print(point[0:4])  # Output : (1, 2, 3, 4)

# We can also unpack the tuples. So we can define three variables x, y and z, and set it to point
x, y, z = point
# similar to lists we can use the IN operator to check for the existence of an item
if 10 in point:
    print("exists")


# Where should we use tuple:
# Basic rule of thumb - Let's say you are dealing with a sequence of objects, and you want to make sure that you don't accidentally
# modify the sequence, you don't accidentally add a new object or remove an existing object, so instead of a list we can use a
# tuple to prevent these accidental errors
