# For Loops
# There are times that we may want to repeat a task a num of times.
# Eg: Let's say we send a msg to a user. If that msg cannot be delivered, perhaps we want to retry three times.
# print("Sending a message")
# print("Sending a message")
# print("Sending a message")
# print("Sending a message")
# print("Sending a message")
# If we want to retry 3 times, we don't want to repeat all the above code.
# That's when we use a loop, we use loop to create repetition.

for number in range(1, 4):
    print("Attempt", number, number * "." )

for number in range(1, 10, 3):  # 1, 10 is the range and 3 is the step
    print("Attempt", number, number * "." )
