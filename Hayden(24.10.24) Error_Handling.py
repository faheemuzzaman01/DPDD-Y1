# file = open("example.txt", "r")
# content = file.read()
# print(content)
# file.close()

# added_info = input("Write something to add to the text file:" )
# with open("example.txt", "a") as file:
#     file.write(f"\n{added_info}")
# with open("example.txt", "r") as file:
#     contents = file.read()
#     print(contents)

# try:
#     uInput1 = int(input("Enter first number: "))
#     uInput2 = int(input("Enter second number: "))
#     a = uInput1/uInput2
#     print(a)
#     # if uInput1 or uInput2 == 0:
#     #     raise ValueError("Input must be positive")
# except ValueError as ve:
#     print("The input should be an integer")
# except ZeroDivisionError as zde:
#     print("The denominator cannot be zero")
# finally:
#     print("The code runs well")

# try:
#     uInput1 = int(input("Enter first number: "))
#     uInput2 = int(input("Enter second number: "))
#     a = uInput1/uInput2
#     print(a)
#     if uInput1 or uInput2 < 0:
#         raise ValueError("Input cannot be negative")
# except ValueError as ve:
#     print(f"Error: {ve}")
# except ZeroDivisionError as zde:
#     print("The denominator cannot be zero")

# uInput1 = int(input("Enter first number: "))
# uInput2 = int(input("Enter second number: "))
# if uInput2 == 0:
#     print("Cannot divide by Zero")
# else:    
#     a = uInput1/uInput2
#     print(a)
# age = int(input("Input your age"))
# if not isinstance(age, int):
#     raise TypeError("Age must be an integer")

# age = int(input("Enter your age: "))
# if age < 0:
#     print("Age cannot be negative")

# try:
#     age = int(input("Enter your age: "))
#     # If age isnt positive, an error occurs
#     if age < 0:
#         raise ValueError("Age cannot be negative")
# # If age isnt a number or integer, an error occurs
# except ValueError as e:
#     print(f"Error: {e}")

# # Sorts a list in ascending order 
# l1 = [10,4,8,6,2,0]
# for i in range(0, len(l1)):
#     for j in range(i+1, len(l1)):
#         if l1[i] >= l1[j]:
#             l1[i], l1[j] = l1[j],l1[i]
# print(l1)

# # Creates a new text file if one under a specific name doesn't exist
# try:
#     file = open("notexisting.txt", "r")  
#     contents = file.read()
#     print(contents)
# except FileNotFoundError:
#     open("notexisting.txt","w")

# name = ""

# def value(name_pram):
#     global name
#     if name == "":
#         print(name_pram)
#     else:
#         name_pram = name
#         print(name_pram)
#     return 0 
# value("")

# # Defining a menu function
# def fn_menu():
#     flag = "y"
#     while flag == "y": 
#         menu_desc = """
#         01 - First Option
#         02 - Second Option
#         03 - Third Option
#         04 - Fourth Option
#         05 - Exit
#     """
#         print(menu_desc)
#         option_number = (input("Enter the option number: "))
#         if option_number.isdigit():
#             option_number = int(option_number)
#             if option_number == 1:
#                 print("You selected option 01")
#             elif option_number == 2:
#                 print("You selected option 02")
#             elif option_number == 3:
#                 print("You selected option 03")
#             elif option_number == 4:
#                 print("You selected option 04")
#             elif option_number == 5:
#                 print("You selected option 05")
#                 flag = "n"
#             else:
#                 print("Please select option between 1 - 5")
#         else:
#             print("Please input an integer")

# fn_menu()


def fn_menu():
    flag = "y"
    while flag == "y": 
        menu_desc = """
        01 - Read File
        02 - Write to file
        03 - Append File
        04 - Create File
        05 - Exit
    """
        print(menu_desc)
        option_number = (input("Enter the option number: "))
        if option_number.isdigit():
            option_number = int(option_number)
            if option_number == 1:
                print("You selected Read")
                with open("menu_file.txt", "r") as file:
                    contents = file.read()
                    print(contents)   
            elif option_number == 2:
                print("You selected Write")
                with open("menu_file.txt", "w") as file:
                    file.write(input("Write what you want to replace the text file with: "))
            elif option_number == 3:
                print("You selected Append")
                with open("menu_file.txt", "a") as file:
                    text_append = input("Write whatever you want to add to the end of the text file: ")
                    file.write(f"\n{text_append}")
            elif option_number == 4:
                print("You selected Create")
                try:
                    file = open("menu_file.txt", "r")  
                    contents = file.read()
                    print(contents)
                except FileNotFoundError:
                    open("menu_file.txt","w")
            elif option_number == 5:
                print("You selected Exit")
                flag = "n"
            else:
                print("Please select option between 1 - 5")
        else:
            print("Please input an integer")

fn_menu()

