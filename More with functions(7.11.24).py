# def factorial(n):
#     if n > 0:
#         if n < 2:
#             return 1
#         else:
#             return n * factorial(n-1)
#     elif n == 0:
#         return 1
#     else:
#         raise ValueError("Factorial only applies to non negative numbers")

# print(factorial(-0))

# n = int(input("Input a positive integer "))
# i = 1
# while n > 1:
#     i = i * n
#     n -= 1
# print(i)

# def fact(number):
#     result = 1
#     for i in range(number, 0, -1):
#         result *= i
#     return result
# print(fact())

# def fact(number):
#     try:
#         if number > -1:
#             result = 1
#             for i in range(number, 0, -1):
#                 result *= i
#             return result
#         else:
#             raise ValueError("Factorial only works with positive integers")
#     except ValueError as ve:
#         print(f"Error {ve}")
# print(fact(-1))


# import requests
# r = requests.get("https://google.com")
# r.status_code

# def input_data():
#     name=input("Enter your name: ")
#     return name
# def process_data(name):
#     return name.upper()
# def output_data(name):
#     print("Hello," +name+ "!")
# name=input_data()
# name=process_data(name)
# output_data(name)

# def subtract(a,b):
#     c = a - b
#     return c
# print(subtract(int(input("Input the first number ")),int(input("Input the second number "))))

# def multiply(d,e):
#     f = d * e
#     return f
# print(multiply(int(input("Input the first number ")),int(input("Input the second number "))))




# def save_name():
#     global name
#     name =input("What's your name? ")

# save_name()

# print(name)

# def perimeter(l,w):
#     p = 2*l + 2*w
#     return p
# print("The perimeter is", perimeter(int(input("Input the length: ")),int(input("Input the width: "))),"units")

# def area(l,w):
#     global a
#     a = (l * w)

# area(int(input("Input the length: ")),int(input("Input the width: ")))
# print(f"The area is {a} units squared")

# def h():
#     print("hi")          # Infinite Loop, uses lots of memory
#     h()
# h()

# while True:
#     print("hi")     # Infinite Loop, uses less memory

# def fact(n):
#     if n == 1:
#         return n
#     else:
#         return n * fact(n-1)
# print(fact(5))

# def fn_rec(num):
#     if num == 10:
#         return num
#     else:
#         print("Hello")
#         return fn_rec(num+1)
    
# print(fn_rec(0))

# for i in range(1,11):
#     print(f"2 * {i} = {2*i}")

def multiplier(i):
    while i > 0:
        print(f"2 * {i} = {2*i}")
        i -= 1
multiplier(10)