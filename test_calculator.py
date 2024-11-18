import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:

    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1,-8), -9)


    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5,2), 3)
    def test_subtract_negative(self):
        self.assertEqual(self.calc.subtract(-159,-357), 198)
    

    def test_multiply_(self):
        result = 0
        for i in range(3):
            result = self.calc.add(result, 7)
        self.assertEqual(result, 21)
    def test_multiply_negative(self):
        result = 0
        for i in range(abs(-9)):
            result = self.calc.add(result, abs(-7))       
        self.assertEqual(result, 63)


    def test_divide(self):
        while 5 >= 2:
            x = self.calc.subtract(5, 2)
            result += 1
        self.assertEqual(result, 2)
    def test_divide_negative(self):
        while -90 <= -7:
            x = self.calc.subtract(-90, -7)
            result += 1
        self.assertEqual(result, 12)


    def test_modulo(self):
        result = 5
        while result >= 2:
            result = self.calc.subtract(result, 2)
        self.assertEqual(result, 1)
    def test_modulo_negative(self):
        result = -17
        while result <= -5:
            result = self.calc.subtract(result, -5)
        self.assertEqual(result, -2)

if __name__ == '__main__':
    unittest.main()