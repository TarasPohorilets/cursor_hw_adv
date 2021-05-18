import unittest
from functions_to_test import Calculator as Calc


class TestFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calc.add(10, 6), 16)
        self.assertEqual(Calc.add(0.14, 0), 0.14)
        self.assertEqual(Calc.add(-9, 3), -6)
        self.assertNotEqual(Calc.add(5, 4), 2)
        self.assertNotEqual(Calc.add(-6, 2), 6)
        self.assertRaises(TypeError, Calc.add, "qwerty", 5)
        self.assertRaises(TypeError, Calc.add, None, 2)
        self.assertRaises(TypeError, Calc.add, "2", 8)
        self.assertRaises(TypeError, Calc.add, [5, 3], 8)

    def test_subtract(self):
        self.assertEqual(Calc.subtract(5, 3), 2)
        self.assertEqual(Calc.subtract(3, 10), -7)
        self.assertEqual(Calc.subtract(-7, 3), -10)
        self.assertNotEqual(Calc.subtract(10, 20), 30)
        self.assertNotEqual(Calc.subtract(10, 20), 30)
        self.assertRaises(TypeError, Calc.subtract, 100, "qwerty")
        self.assertRaises(TypeError, Calc.subtract, "2", 7)
        self.assertRaises(TypeError, Calc.subtract, None, 4)
        self.assertRaises(TypeError, Calc.subtract, {2}, 5)
        self.assertRaises(TypeError, Calc.subtract, [7, 2], 10)

    def test_multiply(self):
        self.assertEqual(Calc.multiply(8, 4), 32)
        self.assertEqual(Calc.multiply(7, 8), 56)
        self.assertEqual(Calc.multiply(-2, 12), -24)
        self.assertNotEqual(Calc.multiply(2, 2), 5)
        self.assertNotEqual(Calc.multiply(33, 5), 150)
        self.assertRaises(TypeError, Calc.multiply, "x", "y")
        self.assertRaises(TypeError, Calc.multiply, None, 3)

    def test_divide(self):
        self.assertEqual(Calc.divide(9, 3), 3)
        self.assertEqual(Calc.divide(88, 11), 8)
        self.assertEqual(Calc.divide(-60, 5), -12)
        self.assertNotEqual(Calc.divide(3, 2), 1)
        self.assertNotEqual(Calc.divide(22, 5), 10)
        self.assertRaises(TypeError, Calc.divide, None, 3)
        self.assertRaises(TypeError, Calc.divide, 'qwerty', 5)
        self.assertRaises(ValueError, Calc.divide, 6, 0)


if __name__ == '__main__':
    unittest.main()