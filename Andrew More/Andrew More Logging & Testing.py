import unittest, logging

logging.basicConfig(filename="CalcError.log",level=logging.ERROR)
def add(n1,n2):
    return f"{n1} + {n2} is {n1 + n2}"

def sub(n1,n2):
   return f"{n1} - {n2} is {n1 - n2}"

def div(n1,n2):
    try:
       return f"{n1} / {n2} is {n1 / n2}"
    except ZeroDivisionError:
        logging.error("n2 was set to 0 in divison")

def mult(n1,n2):
    return f"{n1} * {n2} is {n1 * n2}"

class TestingSum(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1,1), "1 + 1 is 2", "It should be 2")
    
    def test_sub(self):
        self.assertEqual(sub(1,1), "1 - 1 is 0", "It should be 0")
    
    def test_div(self):
       self.assertEqual(div(10,2), "10 / 2 is 5.0", "It should be 5")

    def test_mult(self):
        self.assertEqual(mult(2,3), "2.0 / 3.0 is 6.0", "It should be 6")

if __name__ == "__main__":
    try:
        unittest.main()
    except SystemExit:
        pass

try:
    n1 = float(input("Enter number: "))
    n2 = float(input("Enter number: "))
    print(add(n1,n2))
    print(sub(n1,n2))
    print(div(n1,n2))
    print(mult(n1,n2))
except ValueError:
    if n1.isalpha() == True:
        logging.error("n1 is not a number")
    else:
        logging.error("n2 is not a number")

