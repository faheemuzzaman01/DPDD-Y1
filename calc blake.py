import logging
import unittest

logging.basicConfig(filename='error.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class Calculator:
    def add(self, a, b):
        try:
            return a + b
        except Exception as e:
            logging.error(f"Error in add({a}, {b}): {str(e)}")
            raise

    def subtract(self, a, b):
        try:
            return a - b
        except Exception as e:
            logging.error(f"Error in subtract({a}, {b}): {str(e)}")
            raise

    def multiply(self, a, b):
        try:
            return a * b
        except Exception as e:
            logging.error(f"Error in multiply({a}, {b}): {str(e)}")
            raise

    def divide(self, a, b):
        try:
            if b == 0:
                raise ValueError("Cannot divide by zero")
            return a / b
        except Exception as e:
            logging.error(f"Error in divide({a}, {b}): {str(e)}")
            raise

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(3, 2), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-5, -5), -10)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(-5, -3), -2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 2), 6)
        self.assertEqual(self.calc.multiply(-1, 5), -5)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(-4, -4), 16)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)

    def test_divide_with_negative_divisor(self):
        self.assertEqual(self.calc.divide(5, -2), -2.5)

if __name__ == '__main__':
    unittest.main()
