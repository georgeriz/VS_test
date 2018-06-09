import unittest
from find_appointment import get_start_time

schedules = [
  [['09:00', '11:30'], ['13:30', '16:00'], ['16:00', '17:30'], ['17:45', '19:00']],
  [['09:15', '12:00'], ['14:00', '16:30'], ['17:00', '17:30']],
  [['11:30', '12:15'], ['15:00', '16:30'], ['17:45', '19:00']]
]

class TestGetStartTime(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(get_start_time(schedules, 60), '12:15')

    def test_no_match(self):
        self.assertIsNone(get_start_time(schedules, 90))

if __name__ == "__main__":
    unittest.main()