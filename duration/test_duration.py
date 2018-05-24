import unittest
from duration import duration

class TestDuration(unittest.TestCase):
	def test_seconds(self):
		self.assertEquals(duration(2), "2 seconds")

	def test_one_second(self):
		self.assertEquals(duration(1), "1 second")

	def test_minutes(self):
		self.assertEquals(duration(122),"2 minutes and 2 seconds")

	def test_one_minute(self):
		self.assertEquals(duration(60), "1 minute")
		
		
if __name__ == "__main__":
	unittest.main()