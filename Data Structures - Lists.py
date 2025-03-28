# Lists
# [] - We can define a lists or a sequence of objects

letters = ["a", "b", "c", "d"]
matrix = [[0, 1], [2, 3]]  # We have a list, each item in this list will be a list. We have a parent list and inside we have two child lists
zeros = [0] * 5 # When we want 100 zeros, so using * we can repeat the items in a list and also we can use + to concatenate multiple lists
combined = zeros + letters
print(combined)  # So lists in python can be of different type, so they don't have to from the same type
                # We can combine a list of numbers with strings, boolean and even lists
numbers = list(range(20))
chars = list("Hello Pooja")
print(len(chars))
