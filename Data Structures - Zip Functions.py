# Zip Functions

list1 = [1, 2, 3]
list2 = [10, 20, 30]
# In the above we have 2 lists and let's say we want to combine these lists into a single list of tuples like this :

# we have a list, where each item is a tuple and in the first tuple we're gonna have the first element of each list, similarly the second and the third element
[(1, 10), (2, 20), (3, 30)]  # here we can't use map, filter or list comprehension because it works only with single lists but ere we are combining multiple lists
# So we use the built-in zip function
# zip()  # this function takes multiple iterables and it will combines them

print(zip(list1, list2))  # output : <zip object at 0x104860340> - it returns a zip object which returns an iterable, so we can iterate over it or simply pass it to the built-in list function to convert it to a list
print(list(zip(list1, list2)))  # As the zip functions takes one or more iterable, so we dont have to pass a list here
                              # I can also pass a string print(list(zip("abc", list1, list2)))
                              # Output - [('a', 1, 10), ('b', 2, 20), ('c', 3, 30)]
