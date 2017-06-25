import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + os.sep + "..")

import numpy as np

from sense.soil import Soil


class TestSoil(unittest.TestCase):
    def setUp(self):
        self.eps = 4.+0.j
        self.s = 1.
        self.f = 5.
        self.theta = 0.5

    def tearDown(self):
        pass
    
    def test_init(self):
        S = Soil(s=self.s,f=self.f, eps=self.eps)
        self.assertEqual(S.ks, S.k*S.s)




if __name__ == '__main__':
    unittest.main()
