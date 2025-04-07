# Sets : It is very useful data structure which is basically a collection with no duplicates

numbers = [1, 1, 2, 3, 4] # if we want to remove the duplicates then -
# we can convert this list to a set
uniques = set(numbers)
print(uniques)  # output : {1, 2, 3, 4} we have only unique items, so 1 is not repeated.
                # also note that we use curly braces to define sets
# We can also define a second set using curly braces
numbers = [1, 1, 2, 3, 4]
uniques = set(numbers)
second = {1, 4}  # Now similar to lists, we can add new items to a set or remove an existing one
second.add(5) # we can add a new number
second.remove(2)  # we can also remove
len(second)  # we can use the len() function to get the number of items in a set
print(uniques)

# But where sets shine are in the powerful mathematical operations that are supported by them.
numbers = [1, 1, 2, 3, 4]
first = set(numbers)  # we will rename uniques to first
second = {1, 5}

print(first | second) # we can get a union of two sets using a vertical bar |, so this expression will return a new set that includes all the items that are either in the first or in the second set
                      # output : {1, 2, 3, 4, 5} - we can see the union of these two sets is another set that includes all the items that are either in the first set or the second set
print(first & second)              # we can also get the intersection of two sets
                     # output : {1} this will return a new set that includes all the items that are in both first and second sets.
                     #    so only number that exists in both these sets is 1
print(first - second)   # we can also get the difference between two sets
                    # output : {2, 3, 4} - so the first set has these additional numbers that we don't have in the second set
print(first ^ second)   # semantic difference - this will return items thar are either first or second sets but not both
                        # output : {2, 3, 4, 5}

# Note: One thing we need to know about sets is that unlike lists there are unordered collection. Which means the items that we have
#       in a set are not in sequence, so we cannot access them using an index.
# In other words, if we try to
print(first[0])  # we get an run-time error, because set object does not support indexing
# if we need to access items by index, we need to use a list

# So with set we use one of the above operators or we can check for the existence of an item in a set
if 1 in first:
    print("yes")  # Output : yes

# Summary:
# Set is an unordered collection of unique items, we cannot have a duplicate.
# And this objects are unordered they're not in sequence. So we cannot access them using an index.
