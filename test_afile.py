import unittest

from afile import foo

class TestFoo(unittest.TestCase):
    def test_avg(self):
        self.assertEquals(10, foo(5))

    def test_zero(self):
        self.assertEquals(0, foo(0))
        
    def test_negative(self):
        self.assertEquals(-10, foo(-5))

if __name__ == "__main__":
    unittest.main()
