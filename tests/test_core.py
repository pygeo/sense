import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + os.sep + "..")

import numpy as np

from sense import core

class TestCore(unittest.TestCase):
    def test_fresnel0(self):
        e = 4.+0j 
        F = core.Fresnel0(e)
        self.assertAlmostEqual(F.x, 1./9.)

    def test_reflectivity(self):
        e  = 1.+0j
        theta = 0.
        R = core.Reflectivity(e, theta)
        F = core.Fresnel0(e)
        self.assertEqual(F.x, R.v)
        self.assertEqual(F.x, R.h)
        
        R = core.Reflectivity(e, np.deg2rad(60.))
        self.assertEqual(R.v, 0.)
        self.assertEqual(R.h, 0.)


if __name__ == '__main__':
    unittest.main()
