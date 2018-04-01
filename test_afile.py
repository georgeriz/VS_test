import unittest

from afile import foo

class TestA(unittest.TestCase):
    def test_foo(self):
        self.assertEquals(5, foo())

if __name__ == "__main__":
    unittest.main()