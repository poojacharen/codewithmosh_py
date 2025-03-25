# Escape Sequences
# There is a string "Python Programming", let's say we want to put a double quote in the middle of the string
# "Python " Programming" : there is a prob, bcause the python itself takes this string as an interpretation as the end of the string ie,... the word programming
# the rest of the code is meaningless and invalid
# To solve this,
course = 'Python \"Programming' # \ is an escape character and \" is an escape sequence
print(course)

# other escape sequences
# \"
# \'
# \\
# \n - new line
