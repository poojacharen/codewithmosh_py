# Exceptions : An exception is a kind of error that terminates the execution of a program.
# When writing programs, many things can go wrong. Our programs may encounter an error and terminate. Usually these errors happen because of programmers mistake, or bad data that 
# we get from the user.
# or resources not being available. For eg, we might need to open a file and if that file doesn't exist our program is going to crash.
# It's our job as a programmer to prevent our application from crashing in this kind of situations. Instead we want to display a proper error message to the user. Like, this file 
# doesn't exists
# some eg's are:
# Eg : 1
# numbers = [1, 2]
# print(numbers[3])  # output : we get an index error that happened   File "/Users/poojaraju/PycharmProjects/PythonProject1/app.py", line 8, in <module>
# In programming we accept this kind of error as an Exception.

# Eg : 2
age = int(input("Age: "))
print(age)  # output : when user types a instead of a number we get an error saying type value error

# So it's our job as a programmer to handle this exception and prevent our app from crashing 

