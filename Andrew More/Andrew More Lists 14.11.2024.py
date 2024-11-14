# prints everything in the list
fruits=["apple","banana","orange"]
for i in fruits:
    print(i)

x= 0
while x != 5:
    print(x)
    x += 1

#print all even numbers between 1-20 with for loop
for i in range(2, 21, 2):
    print(i)

#Factorial with while loop
x = int(input("Input number you want factorial of: "))
y = x
while y != 1:
    x = x * (y-1)
    y = y - 1
print(x)

# Factorial without loop
def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n - 1)

x = int(input("Enter number you want factorial of: "))
print(factorial(x))
