# Sorting Lists
# We have a list with bunch of numbers that are not in any particular order.
# To sort this list we use sort()
numbers = [3, 51, 2, 8, 6]
numbers.sort()
print(numbers)  # output : [2, 3, 6, 8, 51] - it is sorted in ascending order

# What about in descending order
numbers = [3, 51, 2, 8, 6]
numbers.sort(reverse=True)
print(numbers) # output : [51, 8, 6, 3, 2]

# In addition to sort() method, we have a built-in function called sorted() this function takes iterable, so we can pass any iterables here and it will sort it for us
numbers = [3, 51, 2, 8, 6]
numbers.sort(reverse=True)
print(sorted(numbers) ) # this will return a new list that is sorted. So unlike sort it will not modify the original list. It will return a new sorted list
print(numbers)       # output : [51, 8, 6, 3, 2] original list that is not sorted


numbers = [3, 51, 2, 8, 6]
# numbers.sort(reverse=True)
print(sorted(numbers, reverse=True)) # Also, similar to the sort() method, if we want to change the sort order we can simply set the reverse argument to true
print(numbers)  # output : [3, 51, 2, 8, 6]

# Now, what if we're dealing with list of complex objects
# Example: what if we have list of tuples
# Let's imagine we are building an application for processing orders
items = [
    ("Product1", 10),
    ("Product2", 9),              # every item in this list is a tuple, with two items
    ("Product3", 12)
]
items.sort()
print(items) # output : [('Product1', 10), ('Product2', 9), ('Product3', 12)] Nothing in here is changed. Bcause python doesn't know how to sort this list.
# In situations like this, we need to define a function that python would use for sorting lists

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

def sort_item(item):
    return item[1]    # we want to return the items based on their price

items.sort(key=sort_item)
print(items)     # output : [('Product2', 9), ('Product1', 10), ('Product3', 12)]
