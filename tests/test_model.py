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
        models = {'surface': 'abc', 'canopy':'efg'}
        S = model.SingleScatRT(surface='abc', canopy='def', models=models)

if __name__ == '__main__':
    unittest.main()
