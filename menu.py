def create_file():
    print("give me a name for the file.")
    name = input("> ")
    with open(f"{name}.txt", "c") as file:
        try:
            file.create()
            print("file created.")
        except FileExistsError:
            print("a file with that name already exists.")

def read_file():
    print("which file? don't bother putting \".txt\" at the end.")
    name = input("> ")
    with open(f"{name}")

def menu():
    flag = "y"
    while flag == "y":
        menu_scheise = """
    1 - read file
    2 - create file
    3 - write file
    4 - append file
    5 - grunkle stunkle wins the funkle bunkle
    6 - skibni gtoiely
    """
        print(menu_scheise)
        print("enter one of the above numbers.")
        choice = input("> ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                while True:
                    print("grunkle", sep = " ")
            elif choice == 2:
                while True:
                    print("stunkle", end = " ")
            elif choice == 3:
                while True:
                    print("wins", end = " ")
            elif choice == 4:
                while True:
                    print("the", end = " ")
            elif choice == 5:
                while True:
                    print("grunkle stunkle wins the funkle bunkle", end = " ")
            elif choice == 6:
                while True:
                    print("skibni gtoiely", end = " ")
            else:
                print("invalid input.")
        else:
            print("invalid input.")

menu()