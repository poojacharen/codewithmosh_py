# Map Function

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]
# Let's say we want to transform the above list into a different shape. So currently each item in this list is a tuple of two items
# Let's say we are only interested in the price of these items so we want to transform this list into a list of numbers ie., the list pf prices
# Here is the basic way to do it

prices = []    # define an empty lists
for item in items:  # we are iterating over our list of items
    prices.append(item[1])

print(prices)  # output : [10, 9, 12] With this code we hae transformed or mapped our original list into a different list

# Now there is a better and more elegant way to achieve the same result. Instead of this for() lop we can use the map function
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

x = map(lambda item: item[1], items)     # map() function takes two parameters, a func and a one or more iterables
for item in x:
    print(item)  # output : 10
                 #           9
                 #           12
# Alternatively we can convert this map object into a list object
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

prices = list(map(lambda item: item[1], items))  # we can use the list function as earlier we learned that we can pass any iterables to this list function to create a new list and also rename x to prices
print(prices)  # output : [10, 9, 12] we get a list of three numbers.
# This is how the map function works, it takes a lambda function and applies it to every item of this iterable
