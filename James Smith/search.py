def linear_search(items, search_item):
    count = 0
    index = 0 
    list_index = []
    while count < len(items):
        if items[index] == search_item:
            count += 1
            list_index.append(index)
            break
        index += 1
    if list_index == []:
        return -1
    else:
        return list_index

def binary_search(items, search_item):
    left = 0
    right = len(items) -1
    while left <= right:
        mid = (left + right) // 2
        if items[mid] == search_item:
            return mid
        elif items[mid] < search_item:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def recursive_binary_search(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return recursive_binary_search(arr, target, left, mid - 1)
    else:
        return recursive_binary_search(arr, target, mid + 1, right)

def for_loop_binary_search(items, search_item):
    left = 0
    right = len(items) -1
    for _ in range(len(items)):
        mid = (left + right) // 2
        if items[mid] == search_item:
            return mid
        elif items[mid] < search_item:
            left = mid + 1
        else:
            right = mid - 1