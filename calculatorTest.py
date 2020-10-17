import unittest
from calculator import Calculator

class CalculatorTest(unittest.TestCase):

    calc = Calculator()

    def test_sum_0_dot_5(self):
        self.assertEqual(self.calc.sum(0.3, 0.2), 0.5)

    def test_sum_6(self):
        self.assertEqual(self.calc.sum(3.5, 2.5), 6)
    
    def test_sum_0_dot24(self):
        self.assertEqual(self.calc.sum(0.2, 0.04, precision=10), 0.24)

    def test_sum_0_dot4(self):
        self.assertEqual(self.calc.sum(0.36, 0.04), 0.4)

    def test_sum_0_dot72(self):
        self.assertEqual(self.calc.sum(0.68, 0.04), 0.72)
    
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4.5, 3), 1.5)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3.5, 2), 7.0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(2, 4), 0.5)

if __name__ == '__main__':
    unittest.main()