# Infinite Loops - It is a loop that runs forever

command = ""
while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break
