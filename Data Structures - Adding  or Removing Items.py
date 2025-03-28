# Adding / Removing Items
letters = ["a", "b", "c", "d"]
# To Add an item - append (to add something at the end of this lists)
letters.append("e")
print(letters)  # output - ['a', 'b', 'c', 'd', 'e']
# If we want to add an item at the specific position, then we should use
#  insert method
letters.append("e")
letters.insert(0, "-")
print(letters)  # output - ['-', 'a', 'b', 'c', 'd', 'e', 'e']
# To Remove the objects
# there are diff options
# if we want to remove the items at the end of the list, we should use the
#  pop method
letters = ["a", "b", "c", "d"]
letters.pop()
print(letters)  # output - ['a', 'b', 'c'] - the letter d is removed
# we can also pass an index to remove the item in the given index
letters.pop(0)
print(letters)
# if there is a situation when we want to remove an obj, but we don't know it's index
letters.pop(0)
letters.remove("b") # this will remove the first occurrence of the letter b. SO if we have multiple b's only the first one will be removed
print(letters)
# If we want to remove all b's in this list, we have to loop over this list and remove each b individually


# Difference between delete and pop
# we can delete an item by its index and also by its range
# the pop method will remove only one item by index
letters.pop(0)
letters.remove("b")
del letters[0:3]
print(letters)

# If we want to remove all the objects in the list
letters.pop(0)
letters.remove("b")
del letters[0:3]
letters.clear() # clear method is used
print(letters)
