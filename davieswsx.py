def sub(num1, num2):
    ans = num1 - num2
    return ans

def multi(num1, num2):
    ans = num1 * num2
    return ans

def get_name(name):
    print("give me your name.")
    name = input("> ")
    return name

name = ""
get_name(name)

print(f"so, {name}, what will you do now?")
print("<=1: Subtract Numbers")
print("==2: Multiply Numbers")
print(">=3: Exit")
choice = input("> ")
while not choice.isdigit():
    print("invalid selection. try again.")
    choice = input("> ")
choice = int(choice)

if choice <= 1:
    print("give me a number.")
    num1 = int(input("> "))
    print("give me another number.")
    num2 = int(input("> "))
    ans = sub(num1, num2)
    print(ans)

elif choice == 2:
    print("give me a number.")
    num1 = int(input("> "))
    print("give me another number.")
    num2 = int(input("> "))
    ans = multi(num1, num2)
    print(ans)

elif choice >= 3:
    print("bye.")
    exit()

else:
    print("if you're reading this, what the hell is going on???")
