import unittest as ut

# assert sum([2, 3, 5]) == 10, "Should be 10"

# def test_sum():
#     assert sum([2, 3, 5]) == 10, "Should be 10"

# if __name__ == "__main__":
#     test_sum()
#     print("Everything passed")

# def testSum():
#     assert sum([2, 3, 5]) == 10, "It should be 10"

# def testSumTuple():
#     assert sum([1, 3, 5]) == 10, "It should be 9"

# if __name__ == "__main__":
#     testSum()
#     testSumTuple()
#     print("Everything is correct")

class testingSum(ut.TestCase):
    def testSum(self):
        self.assertEqual(sum([2, 3, 5]), 10, "It should be 10")
    
    def testSumTuple(self):
        self.assertEqual(sum([1, 3, 5]), 10, "It should be 9")
    
    def testSub(self):
        self.assertEqual(sum([-2, -3, 5]), 0, "It should be 0")
    
    def testSubTuple(self):
        self.assertEqual(sum([-1, -3, 5]), 0, "It should be 1")
    
    def testMul(self):
        self.assertEqual(2 * 3 * 5, 30, "It should be 30")
    
    def testMulTuple(self):
        self.assertEqual(1 * 3 * 5, 30, "It should be 15")
    def testDiv(self):
        self.assertEqual(3 / 5 / 2, 0.3, "It should be 0.3")
    
    def testDivTuple(self):
        self.assertEqual(3 / 5 / 1, 0.3, "It should be 0.6")

if __name__ == "__main__":
    ut.main()
