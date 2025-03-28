# Exercise
# FizzBuzz when divisible by both 3 and 5
# Fizz when divisible by 3
# Buzz when divisible by 5

# any_number = int(input("Enter a number: "))
#
# for i in range(1, any_number):
#
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)


# OR

def fizz_buzz(input):
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
print(fizz_buzz(3))

