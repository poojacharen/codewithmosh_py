# Types of Functions
# there are 2 types:
# 1 - A function that performs a task
# 2 - A function that calculate and return a value

# The below code is type 1
def greet(name):
    print(f"Hi {name}")

# type 2
round(1.9)  # this is an eg of a fun that calculates and returns the value

# eg of type 2

def get_greeting(name):
    return f"Hi {name}"

message = get_greeting("Pooja")  # we have this message variable and we can do whatever we want
file = open("content.txt", "w")  #   with it. We can print it on the terminal, write it to a file
file.write(message)              #  send it in an email etc...

# Another eg:

def greet(name):
    print(f"Hi {name}")

print(greet("Pooja"))  # after we run this we get an output as None
                       # None is the return value of the greet function

# So, in python all functions by default return a none value. NOne is an obj that represents the
# absence of a value
