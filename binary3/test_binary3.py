import unittest
from binary3 import is_binary3

class TestBinary3(unittest.TestCase):
    def test_true(self):
        self.assertTrue(is_binary3("110"))

    def test_false(self):
        self.assertFalse(is_binary3("111"))

    def test_zero(self):
        self.assertTrue(is_binary3("000"))

    def test_letters(self):
        self.assertFalse(is_binary3("abc"))

    def test_space(self):
        self.assertFalse(is_binary3(" 0"))

if __name__ == "__main__":
    unittest.main()