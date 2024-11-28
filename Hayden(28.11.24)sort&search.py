# import random

# number = random.randint(1,100)
# guesses = 6
# guess = 999
# name = input("Hello user, what is your name? ")

# while guess != number and guesses > 0:
#     guess = int(input("Guess a number "))
#     while guesses > 0:
#         if guess == number:
#             print(f"Congradulations {name} you guessed correctly!")
#             guesses = 0
#         elif guess < number:
#             print("Too Low")
#             print(f"{guesses} guesses remain")
#             guess = int(input("Guess a number "))
#             guesses -= 1
#         else:
#             print("Too High")
#             print(f"{guesses} guesses remain")
#             guess = int(input("Guess a number "))
#             guesses -= 1

# def fn_binary_game():
#     print("Think of a number between 1-100: ")

#     low = 0
#     high = 100
#     attempts = 0

#     while low <= high:
#         attempts = 1
#         guess = (low+high) //2
#         print(f"My guess is {guess} ")

#         feedback = input("""
#     it is correct(c)
#     higher (h)                         
#     lower (l)                     
# """)
#         if feedback == "c":
#             print(f"I have guessed the number in {attempts} attempts")
#             break
#         elif feedback == "h":
#             print("")
#         elif feedback == "l":
#             print("")

# def insertion_sort(listnumber):
#     try:
#         for i in range(1,len(listnumber)):
#             key = listnumber[i]
#             j = i - 1
#             while j >= 0 and listnumber[j] > key:
#                 listnumber[j+1] = listnumber[j]
#                 j = j - 1
#             listnumber[j+1] = key
#         return listnumber
#     except TypeError:                                           # Won't cause an error if the list contains a value that isn't an integer or float
#         return "List contains none numerical value"
# listnumber = [3,4,8,5,3.4]                                      # List data
# print(insertion_sort(listnumber))

def fn_merge_sort(list_data):
    if len(list_data) > 1:
        mid = len(list_data) // 2
        left = list_data[:mid]
        right = list_data[mid:]

        fn_merge_sort(left)
        fn_merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list_data[k] = left[i]
                i += 1
            else:
                list_data[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            list_data[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            list_data[k] = right[j]
            j += 1
            k += 1


list_data = [3,1,5,8,7,6]
fn_merge_sort(list_data)
print(list_data)

