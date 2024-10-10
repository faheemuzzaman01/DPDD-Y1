# # Prints all names individually from a list
# studentlist = ["Zach", "Aiden", "Jude", "Kade"]
# for i in studentlist:
#     print(i)

# # Counts from 0 - 4
# index = 0
# while index < 5:
#     print(index)
#     index += 1

# # Counts from 5 - 1
# i = 5
# while i > 0:
#     print(i)
#     i -= 1

# # Prints an amount of rows of stars as inputted by the user
# x = int(input("How many rows of stars? "))
# y = 0
# while y <= x:
#     print("*" * y)
#     y += 1 

# # Prints "Hello World" 3 times
# for index in range(10):
#     if index == 3:
#         break
#     print("Hello World")

# # Prints "Hello World" 4 times
# for index in range(10):
#     print("Hello World")
#     if index == 3:
#         break

# # Prints "Hello World" 4 times
# for index in range(5):
#     if index == 3:
#         continue
#     print("Hello World")

# # Prints "Hello World" 5 times
# for index in range(5):
#     print("Hello World")
#     if index == 3:
#         continue

# # Print all even numbers from 1-20 using while loop
# i = 0
# while i < 21:
#     i += 1
#     if i % 2 != 0:
#         continue
#     else:
#         print(i)
# # Print all even numbers from 1-20 using for loop
# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i)

# # Prints the factorial of an inputted number
# number = int(input("Input an integer: "))
# factorial = 1
# while number != 1:
#     factorial = factorial * number
#     number -= 1
# print({factorial})

# # Prints the factorial of a number without using loops
# n = int(input("Input an integer number: "))
# def factorial(n):
#     if n < 2:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(n))

# Prints an intputted number to the power of itself apparently. (Tried to do factorial with for loop)
userinput = int(input("Enter integer number: "))
fact = 1
for x in range(userinput,0,-1):
    fact = fact * userinput
print (fact)
