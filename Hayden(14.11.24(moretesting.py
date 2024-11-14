# import logging
# logging.basicConfig(filename='error.log',
# level=logging.ERROR)

# def add(n1,n2):
#     sum = n1 + n2
#     return sum

# def test_addition():
#     try:
#         assert add(2,3) == 5, 'Should be 5'
#     except:
#         logging.error('Error')
# test_addition()

import unittest, logging

# logging.basicConfig(filename='error.log',
# level=logging.ERROR)

# def addition(a,b):
#     try:
#         return a + b
#     except ValueError:
#         if a.isalpha() == True or b.isalpha() == True:
#             logging.error('Variables must be integers')

# def subtraction(a,b):
#     try:
#         if a > b:
#             return a-b
#         else:
#             return b - a
#     except ValueError:
#         if a.isalpha() == True or b.isalpha() == True:
#             logging.error('Variables must be integers')

# def multiplication(a,b):
#     try:
#         return a * b
#     except ValueError:
#         if a.isalpha() == True or b.isalpha() == True:
#             logging.error('Variables must be integers')

# def division(a,b):
#     try:
#         return a / b
#     except ValueError:
#         if a.isalpha() == True or b.isalpha() == True:
#             logging.error('Variables must be integers')
#     if b == 0:
#         raise ZeroDivisionError("You can't divide by 0")
#         logging.error('Denominator must not be 0')


# class TestingBasicOpperations(unittest.TestCase):
    
#     def test_addition(self):
#         self.assertEqual(addition(1,2),3,'Should be 3')
        
#     def test_subtraction(self):
#         self.assertEqual(subtraction(3,1),2,'Should be 2')
        
#     def test_multiplication(self):
#         self.assertEqual(multiplication(3,1),3,'Should be 3')

#     def test_division(self):
#         self.assertEqual(division(3,1),3,'Should be 3')

# if __name__ == '__main__':
#     unittest.main()



# with open("large_file.txt", "r") as file:
#     while chunk := file.read(1024):
#         print(chunk)

# i = 0
# while True:
#     i += 1
#     with open("Dobby.png", "rb") as file:
#         binary_data = file.read()
#         print(binary_data)
#     a = str(i)
#     with open(f"{a}.png", "wb") as file:
#         file.write(binary_data)


# with open("Dobby.png", "rb") as file:
#     binary_data = file.read()
# print(binary_data)

# with open(".png", "wb") as file:
#     file.write(binary_data)

