import sort

list = [64, 34, 25, 12, 22, 11, 90]

while True:
    option = input(("""Choose a sorting method:
1 - Bubble Sort
2 - Insertion Sort
3 - Merge Sort
4 - Exit
> """))
    if option in "1234":
        break
    else:
        print("ERROR: That is not an option. Please choose one of the options available.\n")

if option == "1":
    print(f"Unsorted List: {list}")
    print(f"Sorted List: {sort.bubble(list)}")
elif option == "2":
    print(f"Unsorted List: {list}")
    print(f"Sorted List: {sort.insertion(list)}")
elif option == "3":
    print(f"Unsorted List: {list}")
    print(f"Sorted List: {sort.merge(list)}")