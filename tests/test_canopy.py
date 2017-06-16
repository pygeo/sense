import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + os.sep + "..")

from sense.model import CanopyHomoRT
import numpy as np

class TestOh92(unittest.TestCase):
    def setUp(self):
        self.eps = 4.+0.j
        self.ks = 1.
        self.theta = 0.5

    def tearDown(self):
        pass

    def test_canopyhomo(self):

        stype='iso'

        ks_v = 1.
        ks_h = 0.

        ke_h = 2.
        ke_v = 3.
        theta = 0.5
        d = 0.
        C = CanopyHomoRT(ke_h=ke_h, ke_v=ke_h, ks_h=ks_h, ks_v=ks_h, d=d, theta=theta, stype=stype)
        self.assertEqual(C.t_v, 1.)
        self.assertEqual(C.t_h, 1.)

        d = 1.
        ke_h = 0.
        ke_v = 0.
        ks_v = 0.
        ks_h = 0.
        C = CanopyHomoRT(ke_h=ke_h, ke_v=ke_h, ks_v=ks_v, ks_h=ks_v, d=d, theta=theta, stype=stype)
        self.assertEqual(C.t_v, 1.)
        self.assertEqual(C.t_h, 1.)


        theta = np.deg2rad(60.)
        ke_h = 1.
        ke_v = 1.
        C = CanopyHomoRT(ke_h=ke_h, ke_v=ke_v, ks_v=ks_v, ks_h=ks_v, d=d, theta=theta, stype=stype)
        self.assertAlmostEqual(C.t_v, np.exp(-2.))
        self.assertAlmostEqual(C.t_h, np.exp(-2.))



if __name__ == '__main__':
    unittest.main()
