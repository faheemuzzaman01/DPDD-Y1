# def subtract(n1,n2):
#         return f"{n1} - {n2} is {n1 - n2}"
    
# def multiply(n1,n2):
#        return f"{n1} * {n2} is {n1 * n2}"

# def name():
#        username = str(input("Enter name: "))
#        return f"Your name is {username}"
# try:
#       n1 = float(input("Enter 1st number: "))
#       n2 = float(input("Enter 2nd number"))
#       print(subtract(n1,n2))
#       print(multiply(n1,n2))
# except TypeError:
#        print("Please only enter numbers!")
# finally:
#         print(name())

# def Perimeter(Length, Width):
#     return f"The permiter of the shape is {Length*2 + Width*2}"

# def Area(Length, Width):
#     print(f"The area of the shape is {Length * Width}")

# try:
#     Length = float(input("Enter Length: "))
#     Width = float(input("ENter Width: "))
#     print(Perimeter(Length,Width))
#     Area(Length,Width)
# except TypeError:
#     print("Please enter numbers!")

def fn_rec(num):
    if num == 10:
        return num
    else:
        print("Hello")
        return fn_rec(num+1)

print(fn_rec(0))
