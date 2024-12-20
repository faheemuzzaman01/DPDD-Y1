
# linear search template-------------------------------------------------------------------------------------------
# def linear_search(items, search_item):
#     index = -1
#     current = 0
#     found = False
#     while current < len(items) and found == False:
#         if items[current] == search_item:
#             index = current
#             found = True
#         current = current = 1
#     return index





#binary search template-------------------------------------------------------------------------------------------
# def binary_search(items, search_item):
#     index = -1
#     first = 0
#     last = len(items) - 1
#     found = False
#     while first <= last and found == False
#         midpoint = (first + last) // 2
#         if items[midpoint] == search_item:
#             index = midpoint 
#             found = True
#         elif items[midpoint] < search_item:
#             first = midpoint + 1
#         else:
#             last = midpoint - 1
#     return index




#binary search template--------------------------------------------------------------------------------------------
# def BinarySearch(item, items):
#     index = -1
#     first = 0
#     last = len(items) - 1
#     found = False
#     while first <= last and found == False:
#         midpoint = (first + last) // 2
#         if items[midpoint] == item:
#             index = midpoint
#             found = True
#         elif items[midpoint] < item:
#             first = midpoint + 1
#         else:
#             last = midpoint - 1
#     if index == -1:
#         return f"{item} is not in list!"
#     else:
#         return f"{item} is in position {index}"
 
# try:
#     item = int(input("Enter whole number to find: "))
#     items = []
#     x = 0
#     while True:
#         try:
#             toadd = int(input("Enter whole number to put in list: "))
#             items = items + [toadd]
#         except ValueError:
#             print(BinarySearch(item, items))
#             exit()
# except ValueError:
#         print("Only enter whole numbers!")

# #how to linear search a list-----------------------------------------------------------
# def fn_linear_search(listNumber,searchValue):
#     count = 0
#     index = 0
#     listindex = []
#     for number in listNumber:
#         if number == searchValue:
#             count = 1
#             listindex.append(index)
#         index = 1
    
#     if listindex == []:
#         return -1
#     else:
#         return listindex
#     print(fn_linear_search([15,9,27,34,6,12,27],28))




# pseudocode binary search--------------------------------------------------------------------

#left = 0
#right = 5
#mid = (0 + 5) // 2
#mid = 2



# def fn_binary_search(listNumber,searchValue):
#     left = 0
#     right = len(listNumber) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if listNumber[mid] == searchValue:
#             return mid
#         elif listNumber[mid] < searchValue:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1

# print(fn_binary_search(sorted([24,12,45,78,98,6]),12))

# #binary search in recursive---------------------------------------------------------------------------
# def recursive_binary_search(arr, target, left, right):
# # base case: if the range is invalid
#     if left > right:
#         return -1
#     #calculate hte middle index
#     mid = (left + right) // 2
#     #check if the middle element is the target
#     if arr[mid] == target:
#         return mid
#     elif arr[mid] > target:
#         #recursivly search the left half
#         return recursive_binary_search(arr, target, left, mid - 1)
#     else:
#         #recursivly search the right half
#         return recursive_binary_search(arr, target, mid + 1, right)




# # this is a binary search program
# def fn_recursive_binary_search(listNumber,searchValue,left,right):

#     if left > right:
#         return -1
#     mid = (left + right) // 2
#     if listNumber[mid] == searchValue:
#         return mid
#     elif listNumber[mid] > searchValue:
#         return fn_recursive_binary_search(listNumber,searchValue,left,mid - 1)
#     else:
#         return fn_recursive_binary_search(listNumber,searchValue,mid + 1,right)

# list_numbers = [12,13,2,5,8,6,4,10]
# list_numbers = sorted(list_numbers)
# print(list_numbers)

# print(fn_recursive_binary_search(list_numbers,12,0,len(list_numbers) -1 ))



# #my attempt at binary search
# def fn_recursive_binary_search(listNumber,searchValue,left,right):

#     if left > right:
#         return -1
#     mid = (left + right) // 2
#     if listNumber[mid] == searchValue:
#         return mid
#     elif listNumber[mid] > searchValue:
#         return fn_recursive_binary_search(listNumber,searchValue,left,mid - 1)
#     else:
#         return fn_recursive_binary_search(listNumber,searchValue,mid + 1,right)

# list_numbers = [2,4,6,8,10,12,14]
# list_numbers = sorted(list_numbers)
# print(list_numbers)

# print(fn_recursive_binary_search(list_numbers,12,0,len(list_numbers) -1 ))











