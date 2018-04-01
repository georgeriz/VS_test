import unittest

from afile import foo

class TestA(unittest.TestCase):
    def test_foo_avg(self):
        self.assertEquals(10, foo(5))

    def test_foo_zero(self):
        self.assertEquals(0, foo(0))

if __name__ == "__main__":
    unittest.main()