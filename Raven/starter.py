def linearSearch(list, target):
    index = -1
    current = 0
    found = False
    while current < len(list) and found == False:
        if list[current] == target:
            index = current
            found = True
        current += 1
    return index

list = ["15", "9", "27", "34", "6", "12"]
target = input("What would you like to search for? > ")

if linearSearch(list, target) == -1:
    print("Value Not Found")
else:
    print(f"Value Found: {linearSearch(list, target)}")

def binarySearch(list, target):
    index = -1
    first = 0
    last = len(list) - 1
    found = False
    while first <= last and found == False:
        midpoint = (first + last) // 2
        if list[midpoint] == target:
            index = midpoint
            found = True
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return index

list = ["15", "9", "27", "34", "6", "12"]
target = input("What would you like to find? > ")

if binarySearch(list, target) == -1:
    print("Value Not Found")
else:
    print(f"Value found at {binarySearch(list, target)}")