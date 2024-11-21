def linearSearch(list, target):
    current = 0
    count = 0
    while current < len(list):
        if list[current] == target:
            count += 1
        current += 1
    return count

listSize = int(input("How long is the list? > "))
list = []

for i in range(listSize):
    value = input(f"Write a value for {i}: ")
    list.append(value)

target = input("What would you like to search for? > ")

if linearSearch(list, target) == 0:
    print(f"{target} Not Found")
else:
    print(f"{target} found {linearSearch(list, target)} times.")