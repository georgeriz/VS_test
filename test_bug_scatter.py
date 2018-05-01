import bug_scatter
import unittest

class TestBugScatter(unittest.TestCase):
    def test_basic(self):
        room=["+----------------0---------------+",
        	  "|                                |",
        	  "|                                |",
        	  "|          U        D            |",
        	  "|     L                          |",
        	  "|              R                 |",
        	  "|           L                    |",
        	  "|  U                             1",
        	  "3        U    D                  |",
        	  "|         L              R       |",
        	  "|                                |",
        	  "+----------------2---------------+"]
        self.assertEquals(bug_scatter.cockroaches(room), [1, 2, 2, 5, 0, 0, 0, 0, 0, 0])

    def test_corners(self):
        room = ["2-----------4",
                "|           |",
                "|    UD     |",
                "|    RL     |",
                "|           |",
                "6-----------8"]
        self.assertEquals(bug_scatter.cockroaches(room), [0, 0, 1, 0, 1, 0, 1, 0, 1, 0])

    def test_random(self):
        room = ["6--------9--------3--------------+",
        "|            L   R            D  |",
        "|                                7",
        "|                     LL         |",
        "|                  D             |",
        "|                      D   R     |",
        "2 UL     U                  RD   4",
        "|        D                       |",
        "|     L        D                 |",
        "|                   R       L    |",
        "|                                |",
        "5----------------10-----------8--+"]
        self.assertEquals(bug_scatter.cockroaches(room), [0, 2, 4, 1, 2, 2, 1, 1, 4, 1])


if __name__ == "__main__":
    unittest.main()

