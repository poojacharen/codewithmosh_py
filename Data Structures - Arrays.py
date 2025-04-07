# Arrays - When we are dealing with a large sequence of numbers. These arrays take less memory and perform a little bit faster
# Note : 90% of the cases we use lists but we use arrays when we are really dealing with large numbers 10,000 or more numbers

# To use array we need to import it from the array module

from array import array

numbers = array("i", [1, 2, 3])  # a typecode - which is a string that determines the type of objects in your array. It is a string of one char that determines the type of objects in our list
# In array we have that is similar to lists
numbers.append(4)  # adding new objects
numbers.insert(4)  # to add a number and a specific index
numbers.pop(4)    # removes and return a specified element from list or dictionary
numbers.remove(4)  # used to remove items from the list
numbers[0]  # we can also access items by their index. We can get the first item in the array. Unlike lists, objects in this array are typed.
            # so here every object should get integer
numbers[0] = 1.0 # when we change the first item to a floating point number we'll get an error
                # so every obj in this array should be of the same type, which is determined at the time of creating the array using the typecode

# Summary:
# Use arrays only when we are dealing with a large sequence of numbers and you encounter performance problems
# For other cases use lists and tuples by default
