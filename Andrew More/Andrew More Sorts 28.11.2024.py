def BubbleSort(items):
   if len(items) <= 1:
        return "There is nothing in the list!"
   else:
        for i in range(len(items) -1, 0, -1):
            swap = False
            for n in range(i):
                if items[n] > items[n + 1]:
                    items[n], items[n + 1] = items[n + 1], items[n]
                    swap = True
            if swap == False:
                return f"The sorted list is: {items}"
            else:
                pass

def InsertionSort(items):
    n = len(items) 
    if n <= 1:
         print("There is only one item in list!")
    else:
        for i in range(1, n):
            key = items[i]
            j = i-1
            while j >= 0 and key < items[j]:
                items[j+1] = items[j]
                j -= 1
            items[j+1] = key
    print(f"Sorted lits is {items}") 


def MergeSort(listNumber):
    if len(listNumber) > 1:
        mid = len(listNumber) // 2
        left_half = listNumber[:mid]
        right_half = listNumber[:mid]

        MergeSort(left_half)
        MergeSort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                listNumber[k] = left_half[i]
                i += 1 
            else:
                listNumber[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            listNumber[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            listNumber[k] = right_half[j]
            j += 1
            k += 1

def SelectionSort(array, size):
    for ind in range(size):
        min_index = ind
        for j in range(ind + 1, size):
            if array[j] < array[min_index]:
                min_index = j
        (array[ind], array[min_index]) = (array[min_index], array[ind])

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)

items = []
print("Enter anything but a number to begin the sort!")
while True:
    try:
        toadd = float(input("Enter number to put in list: "))
        items = items + [toadd]
    except ValueError:
        # print(BubbleSort(items))
        # InsertionSort(items)
        # print(f"The sorted list is: {items}")
        MergeSort(items)
        # print("Sorted array is")
        # for i in range(n):
        #     print("%d" % items[i],end=" ")
        # size = len(items)
        # SelectionSort(items,size)
        # print(f"Sorted array is {items}")
        # sortarr = quicksort(items)
        # print(f"Sorted list is: {sortarr}")
        exit()