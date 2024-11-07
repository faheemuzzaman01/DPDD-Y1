import logging
from datetime import datetime as dt

time = dt.now()
dtString = time.strftime("%d-%m-%y-%H-%M-%S")

logging.basicConfig(filename=f"error-{dtString}.log", level=logging.ERROR)

# with open("example.txt") as file:
#     content = file.read()
#     print(content)

# with open("example.txt", "a") as file:
#     file.write("New entry added.")

# try:
#     open("rahh.txt")
# except FileNotFoundError:
#     open("rahh.txt", "w")

# with open("rahh.txt") as file:
#     content = file.read()
#     print(content)

# try:
#     userInput01 = int(input("Enter an integer: "))
#     userInput02 = int(input(f"Enter an integer to divide {userInput01} by: "))
#     a = userInput01 / userInput02
#     print(a)
# except:
#     print("ERROR.")

# try:
#     age = int(input("Enter your age: "))
#     if age < 0:
#         raise ValueError("Age cannot be negative.")
# except ValueError as ve:
#     print(f"ERROR: {ve}")

# while True:
#     try:
#         userInput01 = int(input("Enter an integer: "))
#         userInput02 = int(input(f"Enter another integer to divide {userInput01} by: "))
#         a = userInput01 / userInput02
#         print(a)
#         break
#     except ValueError as ve:
#         print("ERROR: Value must be an integer.")
#         continue
#     except ZeroDivisionError as ve:
#         print("ERROR: No number is divisible by 0.")
#         continue

flag = "y"
while flag == "y":
    menuDecr = """
    1 - welcome
    2 - to
    3 - the
    4 - underground
    5 - how
    6 - was
    7 - the
    8 - fall
"""
    print(menuDecr)
    optionMenu = int(input("enter an option. > "))
    
    if optionMenu == 1:
        print("welcome")
    elif optionMenu == 2:
        print("to")
    elif optionMenu == 3:
        print("the")
    elif optionMenu == 4:
        print("underground")
    elif optionMenu == 5:
        print("how")
    elif optionMenu == 6:
        print("was")
    elif optionMenu == 7:
        print("the")
    elif optionMenu == 8:
        print("fall")
    else:
        brokenHeart = """
 ____   ____
/    \ /    \\
\     \\\    /
 \    //   /
  \   \\\  /
   \  // /
    \ \\\/
     \//

"""
        print(brokenHeart)
