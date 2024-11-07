# # # task 1: print all even numbers from 1 to 20 # # #
#for x in range(21):
#    if (x) % 2 != 0:
#        continue
#    print(x)

# # # task 2: print the factorial of a user-inputted number # # #
print("give me a number")
num = int(input("> "))
if num <= 0:
    print("no.")
else:
    fact = 1
    for y in range(1, num + 1):
        fact = fact * y
    print(f"{num} factorial is {fact}.")
