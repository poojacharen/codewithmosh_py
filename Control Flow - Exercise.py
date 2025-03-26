# Exercise : Write a program to display the even numbers between 1 to 10

count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)

print(f"We have {count} even numbers")
