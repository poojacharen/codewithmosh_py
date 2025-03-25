# String Methods

course = "Python Programming"
# len() - it is used for general purpose and it is not limited to strings

# There are few functions that are specific to strings
# everything in Python is an object. And objects have function called methods
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip()) # used to trim any space at the beginning and end of a string. Also have lstrip and rstrip
print(course.find("Pro")) # get an index of the character
print(course.replace("i", "m")) # replaces the character
print("Pro" in course) # if we want to check the existence of a char or seq of char in your string. This expression returns a boolean
                       # output : True
print("swift" not in course) # not operator : use that to see if our string is not contain a char or seq of char
                             # output : true
