def linear_search(list, target):
    found_count = 0
    for index in range(len(list)):
        if list[index] == target:
            found_count += 1
            print(f"found at position {index}")
    print(f"found {found_count} times.")

def binary_search(target, list, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if list[mid] == target:
        return mid
    el

print("how long is the list?")
length = input("> ")
while not length.isdigit():
    print("preferably that would be an integer.")
    length = input("> ")
length = int(length)
list = []
for x in range(length):
    print(f"give me the item to put in position {x}.")
    item = input("> ")
    list.append(item)
print("what would you like to search the list for?")
target = input("> ")
print("press 1 for linear search, don't press 1 for binary search, which doesn't work.")
search_type = input("> ")
if search_type == "1":
    linear_search(list, target)
else:
    binary_search(list, target)