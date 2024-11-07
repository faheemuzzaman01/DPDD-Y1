# def input_data():
#     name = input("enter your name: ")
#     return name
# def process_data(name):
#     return name.upper()
# def output_data(name):
#     print("hello," + name + "!")

# name=input_data() 
# name=process_data(name)

# output_data(name)              


# #task 1 --------------------------------
# def subtract(numberOne,numberTwo):
#     print(numberOne-numberTwo)
# #task 2 --------------------------------
# def fn_multiplication(numberOne,numberTwo):
#      print(numberOne*numberTwo)
# #task 3 --------------------------------
# def output_data():
#      userName = input("Enter the user name: ")
#      return userName


# subtract(10,8)
# fn_multiplication(10,3)

# print(output_data())



# def P(length,width):
#      return 2 * (length + width)

# def fn_area(length,width):
#      print(length*width)
     

# print(P(14,5))
# fn_area(14,5)




# count=0
# while True:
#      print("yooooo",count)
#      count +=1




def fn_rec(num):
    if num == 10:
        return num
    else:
        print("hello")
        return fn_rec(num + 1)
    
print(fn_rec(0))

for i in range(1,11):
    print(F"2 * {i} = {2*i}")