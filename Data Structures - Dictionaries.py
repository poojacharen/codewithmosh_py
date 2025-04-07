# Dictionaries : It is basically a collection of key value pairs. We use it to map a key to a value
# A real world eg of this is a phone book
# In a phone book we map a person's name to their contact details. So we use a person's name as the key and the contact info as the value
# So phone book is a dictionary, its a collection of key value pairs
#
# output : KeyError: 'a' - error

# there are 2 work arounds here
# one solution is to check the existence of a key
point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
print(point["x"])
point["x"] = 10
print(point)
point["z"] = 15
print(point)
if "a" in point:
    print(point["a"])  # now when we run we don't get any error

# second solution is to use the get method
point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
print(point["x"])
point["x"] = 10
print(point)
point["z"] = 15
print(point)
if "a" in point:
    print(point["a"])
#point["a"] # instead of using brackets and the name of the key, we call the get method
point.get("a")
print(point.get("a"))  # output : none
                      # If the key doesn't exists by default it returns none or we can pass a default value as a second argument
print(point.get("a", 0))  # if we dont have an item with a key a, return 0 by default
                         # output : 0
del point["x"]   #to delete an item we use del or delete statement
print(point)  # output : {'y': 2, 'z': 15} - x is gone we only have y and z

# these are the basic operations in dictionaries, we can easily add new items, remove existing items and look up items by their key
# We'll see how to loop over dictionaries
for x in point:
    print(x)  # output : y
              #          z
          # So in each iteration, our loop variable will hold the key of an item. So it's better to rename this to key as well as the value associated with the key
for key in point:
    print(key, point[key])  # output : y 2
                            #          z 15
# There is another way to iterate over a dictionary
for x in point.items():
    print(x)  # output : ('y', 2)
              #          ('z', 15)
       # so in each iteration we het a tuple, in this tuple we have the key and the value
# So we can unpack it
for key, value in point.items():
    print(key, value)  # Output: y 2
                       #         z 15
