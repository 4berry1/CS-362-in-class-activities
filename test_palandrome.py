import unittest
import palandrome

class testCaseAdd(unittest.TestCase):
    def test_1(self):
        self.assertEqual(palandrome.calc("is this a palandrome"), 0)
    def test_2(self):
        self.assertEqual(palandrome.calc("racecar"), 1)
    def test_3(self):
        self.assertEqual(palandrome.calc("False"), 1)


if __name__ == '__main__':
    unittest.main()