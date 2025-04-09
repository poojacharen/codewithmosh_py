# Unpacking Operator

numbers = [1, 2, 3, 4, 5]
print(numbers)  # output : [1, 2, 3, 4, 5]

# but what if we want to print the individual numbers
print(1, 2, 3, 4, 5)  # output : 1 2 3 4 5  so here we don't have square brackets and we don't have comma
                      # we are printing out individual numbers/individual items in our list
# To achieve this, we can use the Unpacking Operator
numbers = [1, 2, 3, 4, 5]
print(*numbers)  # all we have to do is prefix this variable with the unpacking operator *, in javascript we have an operator called spread operator which is 3 dots ... this is exactly the same
# So here we unpack the container, take out its individual elements and pass them as arbitrary arguments to print function
# output : 1 2 3 4 5 we get the exact same output as before

# Another useful application of this is when creating lists
# so let's say we want to have a list of numbers from 0-5
range(5)  # the range() returns a range object.
# so we need to convert it to a list and then store the result in the variable
values = list(range(5))
print(values)  # output : [0, 1, 2, 3, 4]
# so here in the above instead of using the list function we can use the unpacking operator
values = list(range(5))
values = [*range(5)]   # we know this returns an iterable range(5), the good thing about this unpacking operator is that we can unpack any iterable, it doesn't have to be a list, 
                       #so we unpack this iterable which basically means we take individual values and put them in  alist and finally store the result
print(values)  # output : [0, 1, 2, 3, 4]

# by the same token we can unpack a string
values = list(range(5))
values = [*range(5), *"Hello"]
print(values) # output : [0, 1, 2, 3, 4, 'H', 'e', 'l', 'l', 'o']

# Another eg, so using this operator we can combine multiple lists.
first = [1, 2, 3]
second = [4, 5, 6]
values = [*first, "Hi", *second, *"Pooja"] # to combine this lists we can unpack the first one and then the second one[*first, *second]. We can also put something in the middle
                                           # [*first, "a", *second] or unpack a string at the end [*first, "a", *second, *"Pooja]. So it's very powerful
print(values)  # output : [1, 2, 3, 'Hi', 4, 5, 6, 'P', 'o', 'o', 'j', 'a']

# We can also unpack dictionaries but we need to use two asterisks **
first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1}
print(combined) # output : {'x': 10, 'y': 2, 'z': 1}, here if we notice x: 10 it's because if we have multiple items with the same key ie., we have used x in for first and second, 
                #so the last value will be used ie., x : 10

# Summary:
# We can use the unpacking operator to take out individual values in any iterable


