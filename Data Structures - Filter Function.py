# Filter Function
# We have a list of items. Let's say we want to filter this list and only get the items with price >= 10$
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]
# Again, one basic way is to define an empty list, then we iterate over our list of items, for each item we get the price, if it matches our criteria will add it to this list, this is pretty basic
filtered = []
# The better approach is to use the built-in filter function
x = filter(lambda item: item[1] >= 10, items)  # the parameters of this function is same like the map function takes two parameters. If function and iterable. SO it will apply this function on each item of this iterable, if the item matches some criteria, it will return it
print(x) # output : <filter object at 0x10479e200>    so we get a filter object, the filter object just like a map object is iterable so we can loop over it and also we can convert it to a list right away
# So
filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)   # output : [('Product1', 10), ('Product3', 12)] we got the prices >= 10$
