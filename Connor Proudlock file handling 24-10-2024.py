# try:
#     number = int(input("Enter a number:\n"))
# except ValueError:
#     print("that's not a valid number!")

# output if inputted "david" == that's not a valid number!
#|
#|
#|
# try:
#     number = int(input("Enter a number:\n"))
# finally:
#     print("... and finally")

# output with "david":  ... and finally
#|
#|
#|
#|
# def rerun():
#     try:
#         rerun_ = int(input("would you like to run again? yes(1) no(2)"))
#     except ValueError:
#         print("error\nplease enter an integer (1 or 2)")
#     match rerun_:
#         case 1:
#             main()
#         case 2:
#             print("Exiting...")
# def main():
#     file = "dav.txt"
#     with open(file, "r") as file_1:
#         y = len(file_1.readlines())
#     try:
#         choice = int(input("would you like to read(1) or write to the file(2)?"))
#     except ValueError:
#         print("error\nplease enter an integer (1 or 2)\nrestarting...")
#         main()
#     match choice:
#         case 1:
#             with open(file, "r") as file_1:
#                 read_ = ''.join(file_1.readlines())
#             print(f"here is your file:\n{read_}")
#             print(f"\nthere are {y} lines")
#         case 2:
#             lines=int(input("how many lines are you writing?\n"))
#             with open(file, "a") as file_1:
#                 for x in range(lines):
#                     line=input(f"enter line {y}:")
#                     file_1.write(f"\n{line}")
#                     y+=1
#     file_1.close()
#     rerun()
# main()
# |
# |
# |
# |
# def p(x):
#     print(x)
#     return 0
# try:
#     num1 = int(input("enter the first number: "))
#     num2 = int(input("enter the second number: "))
#     num3 = num1 / num2
# except ValueError:
#     p("you need to enter numbers")
# except TypeError:
#     p("you need to enter integers!")
# except ZeroDivisionError:
#     p("you cant divide by zero!")
# finally:
#     p(f"your answer is {num3}")


# num = int(input("enter your number"))
# if num < 0:
#     raise ValueError


def menu():
    while runtime == True:
        opt=int(input("whatwould you like to do?\n(1) create a file\n(2) write to a file\n(3) append a file\n(4) exit"))
        match opt:
            case 1:
                print("you have selected to create a file")
                file_name = input("what will the file be called")
                open(file_name, "x")
            case 2:
                print("you have selected to write to a file")
                file_name = input("what is the file name?")
                with open(file_name, "w"):
                    lines = int(input("how many lines are you writing?"))
                    for x in range(lines):
                        line = input("enter your lines: ")
                        file_name.write(line)
                    
            case 3:
                print("you have selected to append a file")
                file_name = input("what is the file name?")
                with open(file_name, "a"):
                    lines = int(input("how many lines are you writing?"))
                    for x in range(lines):
                        line = input("enter your lines: ")
                        file_name.write(f"\n{line}")
            case 4:
                print("you have selected to exit")
                print("exiting now")
                runtime = False
        