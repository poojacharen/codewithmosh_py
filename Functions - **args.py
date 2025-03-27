# **args
# When we ** we can pass multiple key value pairs or multiple key word arguments to a function, and python will automatically package them into a dictionary

def save_user(**user):
    print(user)

save_user(id=1, name="Pooja", age=29)   # output : {'id':1, 'name':'Pooja', 'age':'29'}
                                        # This output is called a dictionary. It is another complex type or a data structure in python

