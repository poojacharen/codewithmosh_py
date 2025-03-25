# Formatted Strings

first = "Poojitha"
last = "Nagallapati"
full = first + " " + last  # + concatenation
print(full)
# OR
# We can use formatted strings : f"{}" it doesn't have a constant value, it is actually an expression that will be evaluated at one time. Also we can use built-in functions. 
# eg : f"{len(first)}"
# when using formatted strings we can put any valid expressions in between {}

first = "Poojitha"
last = "Nagallapati"
full = f"{first} {last}"
print(full)
