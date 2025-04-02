# Finding Items
# There are times that you want to find the index of a given object in a list

letters = ["a", "b", "c", "d"]
print(letters.index("a"))

# In case if you want to find an index which is not present in the list eg: lets say if you want to find the index of letter "d"
letters = ["a", "b", "c", "d"]
if "d" in letters:
    print(letters.index("d"))

# or
letters = ["a", "b", "c", "d"]
letters.count("d")  # count() it gives the number of occurrences of the given item in the list
if "d" in letters:
    print(letters.index("a"))
