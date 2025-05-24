import unittest
from funk import q2

class Q2Tests(unittest.TestCase):
    def test1(self):
        actual = q2(1,2,3)
        expected = 'No roots'
        self.assertEqual(actual, expected)

    def test2(self):
        actual = q2(4,2,3)
        expected = 'No roots'
        self.assertEqual(actual, expected)
    def test3(self):
        actual = q2(4,8,3)
        expected = (-1.5, -0.5)
        self.assertEqual(actual, expected)
        

if __name__ == "__main__":
    unittest.main()


