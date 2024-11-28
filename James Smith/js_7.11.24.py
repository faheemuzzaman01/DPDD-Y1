# def factorial(num):
#     fact = 1
#     for i in range(1, num + 1):
#         fact *= i
#     print(f'the factorial of {num} is {fact}')
# while True:
#     try:
#         x = int(input('enter an integer: '))
#         if x < 0:
#             print('invalid')
#             continue
#         break
#     except ValueError:
#         print('invalid')
# factorial(x)

# def input_data():
#     name = input('enter your name: ')
#     return name
# def process_data(name):
#     return name.upper()
# def output_data(name):
#     print(f'hello, {name}!')
# name = input_data()
# name = process_data(name)
# output_data(name)

# def subt(x,y):
#     print(f'{x} - {y} = {x - y}')
# def mult(x,y):
#     print(f'{x} * {y} = {x * y}')
# while True:
#     try:
#         n1 = int(input('enter an integer: '))
#         n2 = int(input('enter another integer: '))
#         subt(n1,n2)
#         mult(n1,n2)
#         break
#     except ValueError:
#         print('input must be an integer')

# def enter_name():
#     name = input('enter your name: ')
#     return name
# name = enter_name()
# print(name)

# length = 14
# width = 5
# def perim(x,y):
#     return 2 * (x + y)
# print(perim(length,width))
# def area(x,y):
#     print(x * y)
# area(length,width)

def fn_rec(num):
    if num == 10:
        return num
    else:
        print(f'2 * {num} = {2 * num}')
        return fn_rec(num + 1)
print(fn_rec(0))
