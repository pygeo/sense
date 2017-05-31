import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + os.sep + "..")

from sense.surface import Oh92
import numpy as np

class TestOh92(unittest.TestCase):
    def setUp(self):
        self.eps = 4.+0.j
        self.ks = 1.
        self.theta = 0.5

    def tearDown(self):
        pass
    
    def test_init(self):
        O = Oh92(self.eps, self.ks, self.theta)

    def test_pq(self):
        # test with inc=0
        O = Oh92(self.eps, 0., 0.)
        self.assertEqual(O.q, 0.)
        self.assertEqual(O.p, 1.)

        # some non zero inc
        O = Oh92(self.eps, 0., np.pi)
        self.assertEqual(O.q, 0.)
        self.assertEqual(O.p, 49.)

    def test_scat(self):
        O = Oh92(self.eps, self.ks, self.theta)
        self.assertEqual(O.hh, O.p*O.vv)
        self.assertEqual(O.hv, O.q*O.vv)


    def test_vv(self):
        O = Oh92(self.eps, 0., self.theta)
        self.assertEqual(O.vv, 0.)





if __name__ == '__main__':
    unittest.main()
