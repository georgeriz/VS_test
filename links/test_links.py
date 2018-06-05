import unittest
from extract import foo

class TestFoo(unittest.TestCase):
    def test_one_link(self):
        self.assertItemsEqual(foo("this is bug-123"), ["bug-123"])
    
    def test_two_links(self):
        self.assertItemsEqual(foo("bug-34 and bug-423 need fixing"), ["bug-34", "bug-423"])

    def test_punctuation_after_link(self):
        self.assertItemsEqual(foo("fix bug-3243."), ["bug-3243"])

    def test_no_link(self):
        self.assertItemsEqual(foo("hello world"), [])

    def test_almost_link_but_no(self):
        self.assertItemsEqual(foo("this bug-verification"), [])

if __name__ == "__main__":
    unittest.main()