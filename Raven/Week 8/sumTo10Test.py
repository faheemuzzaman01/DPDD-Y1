import unittest as ut

num1 = int(input("Welcome!\nI will ask you to input 3 numbers in total.\nAll numbers should add up to 10.\nPlease enter the first number: "))
num2 = int(input("Please enter the second number: "))
num3 = int(input("Please enter the third number: "))

class testingSum(ut.TestCase):
    def testSum(self):
        self.assertEqual(sum([num1, num2, num3]), 10, "The result should be 10.")

if __name__ == "__main__":
    ut.main()
