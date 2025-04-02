# Lambda Functions
# It is basically a simple one line anonymous function that we can pass to other functions
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

# def sort_item(item):
#     return item[1]    # we want to return the items based on their price

items.sort(key=lambda item:item[1])
print(items)   # output : [('Product2', 9), ('Product1', 10), ('Product3', 12)] 
# We get the exact same result when we use lambda and its parameters and expressions. In this way we don't need to define def function(ie, def sort_item(item):    
#                                                                                                                                              return item[1] 
# that's why we commented out the def function
