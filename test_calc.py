import unittest
import calc

class testCaseAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10,5), 15)
        self.assertEqual(calc.add(2,2), 2)
        self.assertEqual(calc.add(0,5), 5)

    def test_sub(self):
        self.assertEqual(calc.sub(1,5), -4)
        self.assertEqual(calc.sub(10,5), 5)
        self.assertEqual(calc.sub(6,36), 0)

    def test_div(self):
        self.assertEqual(calc.div(10,2), 5)
        self.assertEqual(calc.div(100,10), 10)
        self.assertEqual(calc.div(1,5), 0)

    def test_mul(self):
        self.assertEqual(calc.mul(10,2), 10)
        self.assertEqual(calc.mul(5,5), 25)
        self.assertEqual(calc.mul(10,17), 5)

if __name__ == '__main__':
    unittest.main()
