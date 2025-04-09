# Handling Exceptions

# age = int(input("Age: "))
# To handle the value error exception here we need to put the statement in the try block.

try:
    age = int(input("Age: "))
except ValueError:  # when user types a character instead of number
    print("You didn't enter a valid age")  # output : 1 - Age: 29 (our program completed successfully)
                                           # output : 2 - Age: hi
                                           #              You didn't enter a valid age

# We also have optional else clause here
try:
    age = int(input("Age: "))
except ValueError:
    print("You didn't enter a valid age")
else:
    print("No exceptions were thrown")  # output : when we enter a valid age no exceptions were thrown
# So what we have in the else: clause will only be executed if we don't have any exceptions. This is similar for our for...else loops 
