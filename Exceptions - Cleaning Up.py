# Cleaning Up
# There are times that we need to work with external resources like files, network connections, databases and so on.
# Whenever we use these resources after we are done we need to release them
# For eg: When we open a file, we should always close it after we are done otherwise another process or another program may not be able to open that file

try:
    file = open("app.py")          # in the try: block we are opening a file
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
finally:
    file.close()  # when we open a file it is obvious that we want to close a file
