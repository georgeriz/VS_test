import unittest
from extract import foo, bar

class TestFoo(unittest.TestCase):
    def test_one_link(self):
        self.assertEqual(foo("this is bug-123"), ["bug-123"])
    
    def test_two_links(self):
        self.assertEqual(foo("bug-34 and bug-423 need fixing"), ["bug-34", "bug-423"])

    def test_punctuation_after_link(self):
        self.assertEqual(foo("fix bug-3243."), ["bug-3243"])

    def test_no_link(self):
        self.assertEqual(foo("hello world"), [])

    def test_almost_link_but_no(self):
        self.assertEqual(foo("this bug-verification"), [])

class TestBar(unittest.TestCase):
    def test_one_link(self):
        self.assertEqual(bar("this is bug-123"), "Did you mean http://jira.com/bug-123 ?")

    def test_multiple_links(self):
        self.assertEqual(bar("bug-34, bug-1200 and bug-423 need fixing"), 
                            "Did you mean http://jira.com/bug-34 and http://jira.com/bug-1200 and http://jira.com/bug-423 ?")

if __name__ == "__main__":
    unittest.main()