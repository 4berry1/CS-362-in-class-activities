import unittest
import Sentleng

class testCaseAdd(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Sentleng.calc("is this a palandrome"), 4)
    def test_2(self):
        self.assertEqual(Sentleng.calc(" i o u c p q"), 6)
    def test_3(self):
        self.assertEqual(Sentleng.calc("False"), 1)
    def test_4(self):
        self.assertEqual(Sentleng.calc(""), 0)


if __name__ == '__main__':
    unittest.main()