# List Comprehensions

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

prices = list(map(lambda item: item[1], items))  # map function

prices = [item[1] for item in items]  # this is the list comprehension and it produces the exact same result as what we have in line 9

filtered = list(filter(lambda item: item[1] >= 10, items))  # filter function

filtered = [item for item in items if item[1] >= 10]
