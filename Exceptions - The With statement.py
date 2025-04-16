# The With Statement 


try:
   with open("app.py") as file:    # this is the file object that the open function returns
    print("File opened.")       # whenever we open a file using a with statement, python will automatically call file.close() whether we have a finally clause or not
                               # In other words, the with statement is used to automatically release external resources
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
