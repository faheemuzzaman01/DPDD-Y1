 
# for Outer_loop in range(5):
#     for Inner_loop in range(Outer_loop + 1):
#             print("*",end="")
#     print("")

#|
#|
#|

# for Outer_loop in range(5):
#     for Inner_loop in range(Outer_loop + 1):
#             print(f"inner = {Outer_loop} | outer = {Inner_loop}")
#     print("")

#|
#|
#|

# usr = int(input("enter the amount of stars you want: "))
# for Outer_loop in range(usr):
#     for Inner_loop in range(Outer_loop + 1):
#             print("*",end="")
#     print("")


#|
#|
#|

# fruits=["apple","banana","orange"]
# for i in range(len(fruits)):
#         print(fruits[i])

#|
#|
#|

# liststudent=["lee", "jack", "zee", "zhu"]
# for student in liststudent:
#         print(student)
        
# print(len(student))

#|
#|
#|

# s = ["*"]; userinput = int(input("enter the amount of stars you would like to make")); userinput = userinput + 1
# while len(s) != userinput:
#     print(''.join(s))
#     s.append("*")
#|
#|
#|
#|
#|

#-- Task One ---

for i in range(1, 21):
    if (i % 2) == 0:
        print(i)


#|
#|
#|
#|
#|
#|
#|
#|

#-- Task Two ---
number = int(input("enter a number you would like"))
x = 0
while x != 1:
    fact = 1
    for num in range(2, number + 1):
        fact *= num
    print(fact)
    x = 1
