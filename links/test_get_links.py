import unittest
from get_links import get_links

class TestGetLinks(unittest.TestCase):
    def test_one_BUG_link(self):
        self.assertEqual(get_links("this is BUG-12"), ["http://jira.com/BUG-12"])

    def test_one_CR_link(self):
        self.assertEqual(get_links("check CR-ABC1-D3RT"), ["goto.com/CR-ABC1-D3RT"])

    def test_two_different_links(self):
        self.assertEqual(get_links("add BUG-1234 to CR-1234-FGHJ"), ["http://jira.com/BUG-1234", "goto.com/CR-1234-FGHJ"])

    def test_link_at_start(self):
        self.assertEqual(get_links("BUG-800 is important"), ["http://jira.com/BUG-800"])

    def test_no_link(self):
        self.assertEqual(get_links("hello world"), [])

    def test_already_link(self):
        self.assertEqual(get_links("click here goto.com/CR-RFUJ-V8F9"), [])

    def test_link_with_punctuation(self):
        self.assertEqual(get_links("let's close BUG-74!"), ["http://jira.com/BUG-74"])

    def test_lowercase_link(self):
        self.assertEqual(get_links("please open bug-32"), ["http://jira.com/BUG-32"])

    def test_mixed_case_link(self):
        self.assertEqual(get_links("what if Bug-8765 didn't exist"), ["http://jira.com/BUG-8765"])

    def test_similar_to_link_but_no(self):
        self.assertEqual(get_links("please send bug-report today"), [])

if __name__ == "__main__":
    unittest.main()