import unittest
from get_links import get_links

class TestGetLinks(unittest.TestCase):
    def test_one_bug_link(self):
        self.assertEqual(get_links("this is bug-12"), ["http://jira.com/bug-12"])

    def test_one_cr_link(self):
        self.assertEqual(get_links("check cr-abc1-d3rt"), ["goto.com/cr-abc1-d3rt"])

    def test_two_different_links(self):
        self.assertEqual(get_links("add bug-1234 to cr-1234-fghj"), ["http://jira.com/bug-1234", "goto.com/cr-1234-fghj"])

if __name__ == "__main__":
    unittest.main()