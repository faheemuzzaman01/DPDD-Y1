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

list = ["Raven", "Raven", "Raven", "Raven", "Raven", "Raven"]
target = input("What would you like to find? > ")

if linearSearch(list, target) == -1:
    print("Value Not Found")
else:
    print(f"Value found at {linearSearch(list, target)}")