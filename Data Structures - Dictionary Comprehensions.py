# Dictionary Comprehensions

values = []  # we are defining an empty list
for x in range(5):  # we are iterating over the range object
    values.append(x * 2)  # in each iteration we get x multiply by 2 and add it to our list
# Whenever we have this pattern in our code we can use either the map function or list comprehension
# syntax for the list comprehension
# we have [] to define a list
# And here is the comprehension expression
# [expression for item in items] - so we iterate over an iterable, so in each iteration we get this item and then do something with the expression
values = [x * 2 for x in range(5)]  # so this line of code is exactly identical to the above code

# so the comprehensions are not only limited to lists. We can also use them with sets and dictionaries
values = {x * 2 for x in range(5)}  # so if we replace the [] to {} we get a set
print(values)  # output : {0, 2, 4, 6, 8} we get a set of even numbers

# what is the syntactical difference between a set and a dictionary?
# Well, for both these data structures we use {} in sets we just have values {1, 2, 3, 4}. But in dictionary we have key value pairs that are separated using a colon. So here we can map {1: "a", 2: "b"} and so on
# So we can easily use comprehension expressions to create dictionary objects.

# so now we can change this expression such that we have a key value pair, we can use x as a key
# values = {x * 2 for x in range(5)}
values = {x: x * 2 for x in range(5)}
print(values)  # output : {0: 0, 1: 2, 2: 4, 3: 6, 4: 8} - we have the dictionary with these key value pairs


# Summary:
# We can use comprehensions with lists, sets and dictionaries
# But what about tuples? values = (x * 2 for x in range(5))
#                        print(values)  Output : we get an error. we don't get a tuple 
