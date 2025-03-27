# xargs
# There are times that I want to create a function that takes a variable number of arguments
# eg :

def multiple(x, y):
    return x * y

multiple(2, 3,) # it's good. what if we wanna pass (2, 3, 4, 5) one or 2 more arguments here?
                      # That doesn't work because multiply func only takes two parameters
# To solve the above prob. We need to

def multiply(*numbers):
    print(numbers)

multiply(2, 3, 4, 5)  # we [] to create lists, and () to create tuples.
                                # Tuples is similar to a list in that it's a collection of objects
                                # The difference is that we cannot modify this collection. We cannot
                                #  add a new object to this tuple
# Tuples just like lists are iterable, so we can iterate over them which means we can use them in loops.
# eg :
def multiply(*numbers):
    for number in numbers:
        print(number)

multiply(2, 3, 4, 5)

# eg:
def multiply(*numbers):
    total = 1
    for number in numbers:
        total += number
    return total


print(multiply(2, 3, 4, 5))
