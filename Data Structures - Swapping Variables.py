# Swapping Variables

x = 10
y = 11

z = x
x = y
y = z

print("x", x)
print("y", y)  # Output : x 11
               #          y 10

# In python, we can swap the value of two variables using only one line of code and without a third variable with this line of code we can swap two variables very easily
x = 10
y = 11

x, y = y, x
# x, y = (11, 10) in a tuple , we have a tuple that we are unpacking. we're sending x to 11 and y to 10

print("x", x)
print("y", y) # Output : x 11
               #         y 10

# We can also define multiple variables on the same line
x = 10
y = 11

x, y = y, x
a, b = 1, 2  # we are defining a tuple and unpacking it on the left side(a, b). So a will be 1 and b will be 2

print("x", x)
print("y", y)
