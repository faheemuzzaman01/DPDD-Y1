import os
def CreatingFile():
    FileName = str(input("Enter new file name: "))
    try:
        file = open(f"{FileName}.txt", "w")
        file.close()
        print(f"{FileName} Created!")
    except FileExistsError:
        print("That file already exists!")
    finally:
        mainmenu()

def WritingFile():
    FileName = str(input("Enter name of file you would like to write to: "))
    try:
        file = open(f"{FileName}.txt", "a")
        file.close()
    except FileNotFoundError:
        print(f"{file} does not exist!")
        mainmenu()
    file = open(f"{FileName}.txt", "w")
    FileLines = int(input("Enter how many lines you want in file: "))
    LineNumber = 1
    Lines = []
    try:
        for i in range(FileLines):
            Line = str(input(f"Input text you want on line {LineNumber}: ") + "\n")
            LineNumber += 1
            Lines = Lines + [Line]
        file.writelines(Lines)#
        file.close()
        print("File Written Correctly!")
    except TypeError:
        print("That is not a number!")
    finally:
        mainmenu()

def AppendingFile():
    FileName = str(input("Enter name of file you would like to write to: "))
    try:
        file = open(f"{FileName}.txt", "a")
    except FileNotFoundError:
        print(f"{file} does not exist!")
        mainmenu()
    FileLines = int(input("Enter how many lines you want in file: "))
    LineNumber = 1
    Lines = []
    try:
        for i in range(FileLines):
            Line = str(input(f"Input text you want on line {LineNumber}: ") + "\n")
            LineNumber += 1
            Lines = Lines + [Line]
        file.writelines(Lines)#
        file.close()
        print("File Written Correctly!")
    except TypeError:
        print("That is not a number!")
    finally:
        mainmenu()

def ErasingFile():
    FileName = str(input("Enter name of file you want to delete: "))
    try:
        os.remove(f"{FileName}.txt")
        print(f"{FileName} Deleted!")
    except FileNotFoundError:
        print(f"{FileName} does not exist!")
    finally:
        mainmenu()

def ReadingFile():
    FileName = str(input("Enter file name you want to read: "))
    try:
        file = open(f"{FileName}.txt", "r")
        print(file)
        file.close()
    except FileNotFoundError:
        print("File not found!")
    finally:
        mainmenu()

def mainmenu():
    selection = int(input("""
1: Creating File
2: Writing to file (will erase contents)
3: Appending to file
4: Erasing file
5: Reading file
6: Exit program
"""))
    try:
        if selection == 1:
            CreatingFile()
        elif selection == 2:
            WritingFile()
        elif selection == 3:
            AppendingFile()
        elif selection == 4:
            ErasingFile()
        elif selection == 5:
            ReadingFile()
        elif selection == 6:
            print("Goodbye!")
            exit()
        else:
            print("You must enter a number between 1-5!")
    except ValueError:
        print("That is not a number!")    

mainmenu()
