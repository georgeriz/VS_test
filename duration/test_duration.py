import unittest
from duration import duration

class TestDuration(unittest.TestCase):
	def test_seconds(self):
		self.assertEquals(duration(2), "2 seconds")

	def test_one_second(self):
		self.assertEquals(duration(1), "1 second")

	def test_minutes(self):
		self.assertEquals(duration(120),"2 minutes")

	def test_one_hour(self):
		self.assertEquals(duration(3600), "1 hour")

	def test_hour_minute_seconds(self):
		self.assertEquals(duration(3662), "1 hour, 1 minute and 2 seconds")
		
		
if __name__ == "__main__":
	unittest.main(failfast=True)