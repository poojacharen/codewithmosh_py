# Accessing Items

letters = ["a", "b", "c", "d"]
print(letters[0])  # we get a
print(letters[-1]) # we get d, this returns the first item from the end of the list
# Using [] we can also modify items in the list so
letters[0] = "A"
print(letters) # output - ['A', 'b', 'c', 'd'], this is the basis of accessing individual elements in a list
print(letters[0:3]) # this will return a new list with the first 3 items in our original list
                    # output - ['A', 'b', 'c']
                    # :3, we get the same result
                    # 0:, we get the list of all items
print(letters[:]) # with this syntax we get a copy of our original list
print(letters[::2]) # when we slice a string, we can also pass a step and this is useful where situations where you want to return every sec or every third element in the original list
                    # we get the output as ['A', 'c'], b will be skipped

# eg:
numbers = list(range(20))
print(numbers[::2])  # output - [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print(numbers[::-2])  # output - [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1] we get all numbers in reverse order

