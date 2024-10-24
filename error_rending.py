# try:
#     userInput1 = int(input("enter the value 01: "))
#     userInput2 = int(input("enter the value 02: "))
#     a = userInput1/userInput2
#     print(a)
# except ValueError as ve:
#     print("error: " ,ve)
# except ZeroDivisionError as zde:
#     print("error: ",zde)
# finally:
#     print("file works perfectly")







# try:
#     userInput1 = int(input("enter the value 01: "))
#     userInput2 = int(input("enter the value 02: "))
#     a = userInput1/userInput2
#     print(a)
# except ValueError as ve:
#      raise ValueError("age must be an integer")
# except ZeroDivisionError as zde:
#     raise ZeroDivisionError("age must be an integer")
# finally:
#     print("file works perfectly")






# age = int(input("enter your age"))
# if age < 0:
#     print("age cannot be negative")



# try:
#     age = int(input("enter your age"))
#     if age < 0:
#         raise ValueError("age cannot be negative")
# except ValueError as e:
#     print(f"error: {e}")





# while True:
#     try:
#         UserInput01 = int(input("enter the value 01: "))
#         UserInput02 = int(input("enter the value 02: "))
#         a = UserInput01/UserInput02
#         print(a)
#     except ValueError as ve:
#         print("the input should be an integer")
#     except TypeError as te:
#         print("the number must be an integer")
#     except ZeroDivisionError as zde:
#         print("the second number should not be zero or negative")
#     finally:
#         exit()




# name = "fahim"

# def fn_print_value(name_pram):
#     global name
#     if name == "":
#         print(name_pram)
#     else:
#         name_pram = name
#         print(name_pram)
#     return 0
# fn_print_value("fahim")



def fn_menu():
    flag = "y"
    while flag == "y":
        menu_desc = """
        01 - first option
        02 - second option 
        03 - third option
        04 - forth option
        05 - fifth option
        """

        print(menu_desc)
        option_number = int(input("enter the option number"))

        if option_number.isdigit():
            option_number = int(option_number)

        if option_number == 1:
            print("you have selected option 01")
        elif option_number == 2:
            print("you have selected option 02")
        elif option_number == 3:
            print("you have selected option 03")
        elif option_number == 4:
            print("you have selected option 04")
        elif option_number == 5:
            print("you have selected option 05")
        flag = "n"
        else:
        print("select an option between 1 - 5")
        else:
print("please input an integer")

fn_menu()
