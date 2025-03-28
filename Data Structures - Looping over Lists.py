# Looping over Lists
# 1. We can use for loop to iterate over lists
letters = ["a", "b", "c", "d"]
for letter in letters:
    print(letter)

# 2. When we want to get the index of each item, we got a built-in function called enumerate
# To call index we can use enumerate function, so this will return an enumerate object which is iterable and in each iteration it will return a tuple
letters = ["a", "b", "c", "d"]
for letter in enumerate(letters):   # In this enumerate obj will give us a tuple
    print(letter)  # output -  (0, 'a')
                   #           (1, 'b')
                   #           (2, 'c')
                   #           (3, 'd')
                  # So in each iteration we're getting a tuple. The first item is the index and the second item is the item in the index
# 3. We can unpack the tuple with the below code
letters = ["a", "b", "c", "d"]
items = (0, "a")
index, letter = items
for index, letter in enumerate(letters):
    print(index, letter) # output - 0 a
                         #          1 b
                         #          2 c
                         #          3 d
