import unittest 
import tests.calc as calc 

# https://docs.python.org/3/library/unittest.mock.html#the-patchers
# https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug
# python3 -m unittest test_calc.py

class TestCalc(unittest.TestCase):

    def test_add(self): 
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 2), 1)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertRaises(ValueError, calc.divide, 10, 0)

        with self.assertRaises(ValueError):
            calc.divide(10, 0)


if __name__ == '__main__':
    unittest.main()