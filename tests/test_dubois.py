import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + os.sep + "..")

from sense.surface import Dubois95
import numpy as np

class Test_Dubois95(unittest.TestCase):
    def setUp(self):
        self.eps = 4.+0.j
        self.ks = 1.
        self.theta = 0.5

    def tearDown(self):
        pass
    
    def test_init(self):
        O = Dubois95(self.eps, self.ks, self.theta, lam=0.05)

    def test_scat(self):
        O = Dubois95(self.eps, self.ks, self.theta, lam=0.0)
        self.assertEqual(O.hh, 0.)
        self.assertEqual(O.vv, 0.)
       

        lam=0.05
        lam1 = lam*100.
        O = Dubois95(self.eps, self.ks, self.theta, lam=lam)

        # test for VV
        a = 10.**-2.35
        cs = np.cos(self.theta)
        ss = np.sin(self.theta)
        b = cs**3./ss**3.
        c = 10.**(0.046*np.real(self.eps)*np.tan(self.theta))
        d = (self.ks*ss)**1.1
        e = lam1**0.7
        self.assertEqual(O.vv,a*b*c*d*e)

        # test for HH
        a = 10.**-2.75
        b = (cs**1.5)/(ss**5.)
        c = 10.**(0.028*np.real(self.eps)*np.tan(self.theta))
        d = (self.ks*ss)**1.4
        e = lam1**0.7
        self.assertAlmostEqual(O.hh, a*b*c*d*e)


if __name__ == '__main__':
    unittest.main()
