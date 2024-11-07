list = []
x=0
def factorial(x):
    while x != 0:
        list.append(x)
        x -= 1
    if not list:  
        return 0
    total = list[0]  
    for num in list[1:]: 
        total *= num
    print(total)
def main():
    try:
        q1 = int(input("enter a number to factorial | "))
    except ValueError:
        print("error, enter an integer!")
        main()
    if q1 <= 0:
        print("error please enter a number above 0")
        main()
    factorial(q1)
main()