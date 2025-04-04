# Stacks - This resembles a stack of items in the real world.
# Imagine you have a stack of books and imagine the last book you put on top of this stack is the first book that you can remove
# We refer to this behavior as LIFO - Last In First Out. This is a stack data structure and it's very common in real world apps.

browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)  # output - [1, 2, 3]

# When the user presses the back button we should remove the last item in this list. We use the pop() method
last = browsing_session.pop()  # this removes the last item from the stack and return it
print(last)  # output - 3 - number 3 is removed
print(browsing_session)  # output - [1, 2]

# So we need to take the user to the previous website, which is the item on top of the stack. And we get that using a -1 index
print(browsing_session[-1])  # This returns the last items   # output - 2
print("Redirect", browsing_session) # So when the user presses the back button we redirect them to a previous website which is website number 2 # output - Redirect [1, 2]

# Now here we need to check if the stack is empty or not. If it becomes empty we need to disable the back button
if not browsing_session:
    print("disable")

# The summary :
browsing_session = []
browsing_session.append(1) # used append() method to add an item on top of the stack
browsing_session.pop()    #  used pop() method to remove the item on top of the stack
# Before using the index -1, we need to check to see if our stack is empty or not, because when it's empty if we run the index -1 code we get an error
if not browsing_session: # then we will get the item that is top of the stack
browsing_session[-1]  # used index -1 to get the item on top of the stack

