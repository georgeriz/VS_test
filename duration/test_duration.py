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

	def test_zero(self):
		self.assertEquals(duration(0), "now")

	def test_years(self):
		self.assertEquals(duration(101956166), "3 years, 85 days, 1 hour, 9 minutes and 26 seconds")

	def test_start_with_one(self):
		self.assertEquals(duration(600), "10 minutes")
		
		
if __name__ == "__main__":
	unittest.main(failfast=True)