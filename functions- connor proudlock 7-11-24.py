def subtract(x,y):
    z = x-y
    print(z)

def multiply(x,y):
    print(x*y)

def name_():
    global name
    name = input("enter your name | ")
    return name

# subtract(6,5)
# multiply(5,5)
# name_()
# print(name)

def fn_rec(num):
    if num==10:
        return num
    else:
        print("Hello")
        return fn_rec(num+1)

print(fn_rec(0))