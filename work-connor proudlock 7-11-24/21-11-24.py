

#def main():
#    current=0; items=[15,9,27,34,6,12]; c = 27; passes = 0; ran=[]
#    complete = False
#    while complete == False:
#        if items[current] != c:
#            ran_2 = "number: ", str(items[current]), "| index:", str(current)
#            result = " ".join(ran_2)
#            ran.append(result); current = current + 1; passes += 1
#        if items[current] == c:
#            ran_2 = "number: ", str(items[current]), "| index:", str(current)
#            result = " ".join(ran_2)
#            ran.append(result); current = current + 1; passes += 1
#            print(f"{c} was found at index {current} in {passes+1} passes\nthese were the items ran through: {ran}")
#            complete = True
#main()




# def binary_search(items, search_item):
#     index=-1
#     first=0
#     last=len(items)-1
#     found = False
#     while first <= last and found == False:
#         midpoint=(first+last)//2
#         if items[midpoint] == search_item:
#             index = midpoint
#             found = True
#         elif items[midpoint] < search_item:
#             first = midpoint+1
#         else:
#             last = midpoint-1
#     return index

# a = [15,9,27,34,6,12]
# print(binary_search(a, 27))

# def bin(listNum, searchValue):

#     left=0; right=len(listNum)-1
#     if len(set(listNum)) > len(listNum):
#         print(f"there are {len(set(listNum)) - len(listNum)} duplicate numbers.")
#     while left<=right:
#         mid=(left+right)//2
#         if listNum[mid]==searchValue:
#             return mid
#         elif listNum[mid]<searchValue:
#             left=mid+1
#         else:
#             right=mid-1
#     return 0
# print(bin(sorted([24,12,45,78,98,6,5,95,2,46,73,63,3456,143,65,65]),12))

def bin(listNum, searchValue):

    left=0; right=len(listNum)-1
    if len(set(listNum)) < len(listNum):
        print(f"there are -{len(set(listNum)) - len(listNum)}-- duplicate numbers.")
    while left<=right:
        mid=(left+right)//2
        if listNum[mid]==searchValue:
            return mid
        elif listNum[mid]<searchValue:
            left=mid+1
        else:
            right=mid-1
    return 0
print(d.bin(sorted([2,4,6,8,10,12,14]),10))
