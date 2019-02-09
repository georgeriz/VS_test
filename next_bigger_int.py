def next_bigger(n):
    w = list(reversed(str(n)))
    for i, c in enumerate(w[:-1]):
        if int(c) > int(w[i+1]):
            j = next(w.index(n) for n in w[:i+1] if n > w[i+1])
            w[j], w[i+1] = w[i+1], w[j]
            w[:i+1] = w[:i+1][::-1]
            return int(''.join(reversed(w)))
    else:
        return -1

import unittest

class TestNextBigger(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(next_bigger(12), 21)

    def test_example_2(self):
        self.assertEqual(next_bigger(513), 531)

    def test_example_3(self):
        self.assertEqual(next_bigger(2017), 2071)

    def test_example_4(self):
        self.assertEqual(next_bigger(9), -1)

    def test_example_5(self):
        self.assertEqual(next_bigger(111), -1)

    def test_example_6(self):
        self.assertEqual(next_bigger(531), -1)

    def test_example_7(self):
        self.assertEqual(next_bigger(2500), 5002)

    def test_example_9(self):
        self.assertEqual(next_bigger(1234567890), 1234567908)

    def test_example_8(self):
        self.assertEqual(next_bigger(6985), 8569)

if __name__ == "__main__":
    unittest.main()
    next_bigger(6985)
