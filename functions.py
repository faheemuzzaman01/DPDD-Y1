def perimeter():
    type = input("What type of shape is your shape? (square / circle / rectangle / triangle) ")
    if type == 'square':
        sqaure()
    elif type == 'circle':
        circle()
    elif type == 'rectangle':
        rectangle()
    elif type == 'triangle':
        triangle()
    else:
        print("Please pick one of the selections.")
        perimeter()

def sqaure():
    side = int(input("Please enter one length of the square in cm: "))
    print()
    print(f"The perimeter of the square is {side*4}cm!")
    print()
    again = input("Would you like to restart? (y/n)")
    print()
    if again == 'y':
        perimeter()
    elif again == 'n':
        exit()
    else:
        print("Please pick one of the selections.")
        exit()

def circle():
    side = int(input("Please enter the radius of the circle in cm: "))
    print()
    print(f"The perimeter of the circle is {round(side*side*3.14159265,2)}cm!")
    print()
    again = input("Would you like to restart? (y/n)")
    print()
    if again == 'y':
        perimeter()
    elif again == 'n':
        exit()
    else:
        print("Please pick one of the selections.")
        exit()

def rectangle():
    side = int(input("Please enter one length of the rectangle in cm: "))
    side2 = int(input("Please enter the other length of the rectangle in cm: "))
    print()
    print(f"The perimeter of the rectangle is {side+side+side2+side2}cm!")
    print()
    again = input("Would you like to restart? (y/n)")
    print()
    if again == 'y':
        perimeter()
    elif again == 'n':
        exit()
    else:
        print("Please pick one of the selections.")
        exit()

def triangle():
    side = int(input("Please enter the first length of the triangle in cm: "))
    side2 = int(input("Please enter the second length of the triangle in cm: "))
    side3 = int(input("Please enter the last length of the triangle in cm: "))
    print()
    print(f"The perimeter of the triangle is {side+side2+side3}cm!")
    print()
    again = input("Would you like to restart? (y/n)")
    print()
    if again == 'y':
        perimeter()
    elif again == 'n':
        exit()
    else:
        print("Please pick one of the selections.")
        exit()
perimeter()