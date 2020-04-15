import unittest
import triangle

class TestTriangle(unittest.TestCase):

    def test_hypo_one(self):
        self.assertEqual(triangle.getTriangle(3, 4), 5)

    def test_hypo_two(self):
        self.assertEqual(triangle.getTriangle(4, 4), 6)

if __name__ == "__main__":
    unittest.main()
