# Unpacking Lists
# When we want to get individual items in a list we assign them to a diff variable
# eg:
# numbers = [1, 2, 3, 4]
# first = numbers[0]
# second = numbers[1]
# third = numbers[2]
# fourth = numbers[4]
# we are going to use the above variables in a few complex expressions in our code.
# There is a cleaner and more elegant way to achieve the same above result
# and that is what we call list as Unpacking Lists
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # we can unpack this lists into multiple variables
# first, second, third, fourth = numbers # what we have in line 12 is exactly identical to what we have on lines 5, 6, 7
                               # This is what we call list unpacking
# Important : the number of variables we have on the left side of the assignment operator should be equal to the number of items we have in the list
# So if we exclude fourth here and run the program, we will get an error
# But what if we
first, second, third, *other = numbers # we get first, second and third in a list and other items will be stored in a separate list
print(first)
print(other)  # output : 1
              #          [4, 5, 6, 7, 8, 9, 10]
