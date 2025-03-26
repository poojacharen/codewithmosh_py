# For...Else
# eg: Let's imagine the scenario after the first attempt we can successfully send the msg

successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")
