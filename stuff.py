# fruits = ["apple", "banana", "orange"]

# print(fruits)
# for i in range(len(fruits)):
#     print(fruits[i])

# for fruit in fruits:
#     print(fruit)

# listStudent = ["Raven", "Sam", "Sal", "Phoenix", "Ezra", "Isaac"]
# for student in listStudent:
#     print(student)

# index = 5
# while index > 0:
#     print("Hello World!")
#     index = index - 1

for x in range(1,20):
    if x % 2 == 0:
        print(x)

givenNumber = int(input("\nGive me an integer number greater than 1: "))
factorial = givenNumber - 1
while factorial <= 0:
    print("That is not a valid number.")
    givenNumber = int(input("\nGive me an integer number greater than 1: "))
    factorial = givenNumber - 1

result = givenNumber * factorial
factorial -= 1

while factorial > 0:
    result *= factorial
    factorial -= 1
print(f"The factorial of {givenNumber} is {result}")
