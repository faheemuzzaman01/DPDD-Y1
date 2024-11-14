import unittest as ut
import logging as l

# l.basicConfig(filename = 'error.log', level = l.ERROR)

# def add(x, y):
#     return x + y
# def sub(x, y):
#     return x - y 
# def div(x, y):
#     return x/y
# def mul(x, y):
#     return x*y

# def test_addition():
#     try:
#         assert add(2, 3) == 8
#         print('no error found')
#     except:
#         print('an error has been logged')
#         l.error("Error Log")
# test_addition()

# class TestCode(ut.TestCase):
#     def test_add(self):
#         self.assertEqual(add(2,3), 5)
#     def test_sub(self):
#         self.assertEqual(sub(3,2), 1)
#     def test_div(self):
#         self.assertEqual(div(4,2), 2)
#     def test_mul(self):
#         self.assertEqual(mul(2,3), 6)
# if __name__ == '__main__':
#     ut.main()

# def process(x):
#     print(x)

# with open('large_text.txt', 'r') as f:
#     while  chunk := f.read(1024):
#         process(chunk)

# with open('image.jpg', 'rb') as f:
#     binary_data = f.read()
# print(binary_data)

try:
    f = open('does_not_exist.txt', 'r')
except FileNotFoundError:
    print('file not found')