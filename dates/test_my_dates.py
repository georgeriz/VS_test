import unittest
from my_dates import foo

class TestMyDates(unittest.TestCase):
	def test_foo(self):
		self.assertEquals(foo(2017, 9), ("2017-9-01", "2017-9-30"))
		
if __name__ == "__main__":
	unittest.main()
