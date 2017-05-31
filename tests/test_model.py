import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + os.sep + "..")

from sense import model

class TestModel(unittest.TestCase):
    def test_init(self):
        M = model.Model()

class TestSingle(unittest.TestCase):
    def test_init(self):
        # some dummy variables
        g = 'abc'
        c = 'def'
        cg = 'ghj'
        gcg = 'klm'
        S = model.SingleScatRT(ground=g, canopy=c, canopy_ground=cg, ground_canopy_ground=gcg)

if __name__ == '__main__':
    unittest.main()
