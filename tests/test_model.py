import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + os.sep + "..")

import numpy as np
from sense import model

class TestModel(unittest.TestCase):
    def test_init(self):
        M = model.Model(theta=np.arange(10))

class TestSingle(unittest.TestCase):
    def setUp(self):
        self.theta = np.arange(1.,80.)

    def test_init(self):
        # some dummy variables
        models = {'surface': 'abc', 'canopy':'efg'}
        S = model.SingleScatRT(surface='abc', canopy='def', models=models, theta=self.theta)

    def test_scat(self):
        # some dummy variables
        models = {'surface': 'Oh92', 'canopy':'dummy'}
        S = model.SingleScatRT(surface='abc', canopy='def', models=models, theta=self.theta)
        S.sigma0()

if __name__ == '__main__':
    unittest.main()
