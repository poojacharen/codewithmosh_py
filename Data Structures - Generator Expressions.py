# Generator Expressions
# Here we have created a list using a list comprehension expression then we iterate over all the numbers over this list and print them

values = [x * 2 for x in range(10)]
for x in values:
    print(x)  # output : we get all the even numbers from 0 - 18

# Above code is perfectly fine. But there are situations where we might be working on with a really large data set or perhaps an infinite stream of data
# In those situations we shouldn't store all of those values in the memory, because that's very memory inefficient
# For eg: What if instead of range(10) like the above code , we had a range(billion), you don't want to store a billion objects in memory, that takes too much memory.
# In situations like this it's more efficient to use a Generator Object.
# Generator Objects are iterable so just like lists we can iterate over them and in each iteration we generate or spit out a new value
# So unlike lists, they don't store all the values nad memory, they generate a new value in each iteration

values = (x * 2 for x in range(10))  # we changed [] to ()
for x in values:
    print(x)  # output : we get the same result as the above 0 - 18
# However a value is no longer a list, it's a generator object
values = (x * 2 for x in range(10))
print(values)  # output : <generator object <genexpr> at 0x102557510>

# what is interesting is the size of generator objects.
# Now let's see how we can get the size of an object

from sys import getsizeof

values = (x * 2 for x in range(1000))  # we changed range to 1000
print("gen:", getsizeof(values))  # output : gen: 200 - so the generator object takes 200 bytes of memory
