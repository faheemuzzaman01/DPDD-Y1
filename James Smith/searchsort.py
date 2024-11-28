#  - - - - - - - - - - S E A R C H  A L G O R I T H M S - - - - - - - - - -

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

def bubble_sort(arr):
    for n in range(len(arr) - 1, 0, -1):
        swap = False  
        for i in range(n):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swap = True
        if swap == False:
            break

#  - - - - - - - - - - - S O R T  A L G O R I T H M S - - - - - - - - - - -

def insertion_sort(arr):
    n = len(arr)
    if n <= 1:
        return
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
    i = 0    
    j = 0     
    k = l 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
# ----------l = 0, r = len(arr) - 1-----------
def merge_sort(arr, l, r):
    if l < r:
        m = l+(r-l)//2
        merge_sort(arr, l, m)
        merge_sort(arr, m+1, r)
        merge(arr, l, m, r)

# ---------------size = len(arr)--------------
def selection_sort(arr, size):
    for i in range(size):
        min_index = i
        for j in range(i + 1, size):
            if arr[j] < arr[min_index]:
                min_index = j
        (arr[i], arr[min_index]) = arr[min_index], arr[i]