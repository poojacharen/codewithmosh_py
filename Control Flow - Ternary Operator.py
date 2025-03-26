# Ternary Operator
# Let's imagine we are building an app for University and we want to check to see if the person whose applying is eligible or not

# Method 1
age = 23
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")

# Method 2
if age >=18:
    message = "Eligible"
else:
    message = "Not Eligible"
print(message)

# Method 3 : This method is a Ternary Operator
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)
