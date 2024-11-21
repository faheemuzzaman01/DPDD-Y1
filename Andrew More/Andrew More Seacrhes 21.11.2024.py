# def LinearSearch(items, item):
#     index = -1
#     current = 0
#     while current < len(items):
#         if items[current] == item:
#             print(f"{item} is in position {current}")
#         current = current + 1
#     if index == -1:
#         return f"{item} is not in list"
#     else:
#         pass

# item = str(input("Enter Item: "))
# x = 0
# items = []
# while x == 0:
#     toadd = str(input("Enter something to find in list. Leave blank if you want to proceed: "))
#     if toadd == "":
#         LinearSearch(items, item)
#         x = 1
#     else:
#         items = items + [toadd]

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
#     item = float(input("Enter whole number to find: "))
#     items = []
#     x = 0
#     while True:
#         try:
#             toadd = float(input("Enter whole number to put in list: "))
#             items = items + [toadd]
#         except ValueError:
#             print(BinarySearch(item, items))
#             exit()
# except ValueError:
#         print("Only enter whole numbers!")