import unittest
from script import add

class TestScript(unittest.TestCase):
    def test_add(self):
        # Test addition function
        self.assertEqual(add(2, 3), 5)  # Example test case

if __name__ == '__main__':
    unittest.main()
