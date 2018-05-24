import unittest
from duration import duration

class TestDuration(unittest.TestCase):
	def test_seconds(self):
		self.assertEquals(duration(2), "2 seconds")
		
	def test_minutes(self):
		self.assertEquals(duration(122),"2 minutes and 2 seconds")
		
		
if __name__ == "__main__":
	unittest.main()