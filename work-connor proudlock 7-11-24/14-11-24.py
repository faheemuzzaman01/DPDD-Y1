import logging
import unittest

logging.basicConfig(filename="Programming\week 8\error.log",
level=logging.ERROR)

# def add(a, b):
#     return a + b
# def test():
#     try:
#         assert add(1, 3) == 5, "should be 5"
#     except AssertionError as error:
#         logging.error(f"assertion error | {error}")
# test()

def sub(x,y):
    return x-y
def mult(x,y):
    return x*y
def div(x,y):
    return x/y

class functions(unittest.TestCase):
    def test_addition(self):
        try:
            self.assertEqual(sum([2,3,5]), 10, "it should be 10")
        except AssertionError as error:
            logging.error(f"assertion error | {error}")
    def test_subtraction(self):
        try:
            self.assertEqual(sub(5,4), 1, "it should be 1")
        except AssertionError as error:
            logging.error(f"assertion error | {error}")
    def test_multiplication(self):
        try:
            self.assertEqual(mult(5,4), 20, "it should be 20")
        except AssertionError as error:
            logging.error(f"assertion error | {error}")
    def test_division(self):
        try:
            self.assertEqual(div(20,4), 5, "it should be 5")
        except AssertionError as error:
            logging.error(f"assertion error | {error}")

with open("Programming\\week 8\\large_text.txt", "r") as file:
    while chunk := file.read(1024):
        print(chunk)

if __name__ == "__main__":
    unittest.main()