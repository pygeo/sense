import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + os.sep + "..")

from sense.surface import GaussianSpectrum, ExponentialSpectrum
import numpy as np

class TestRoughness(unittest.TestCase):
    def setUp(self):
        self.niter=2
        self.l = 0.1
        self.theta = np.deg2rad(60.)
        self.thetas = self.theta*1.
        self.phi = 0.
        self.phis = np.deg2rad(180.)
        self.freq = 6.

    def tearDown(self):
        pass

    def test_gauss(self):
        S = GaussianSpectrum(niter=self.niter, l=self.l, theta=self.theta, thetas=self.thetas, phi=self.phi, phis=self.phis, freq=self.freq)
        S.wn()

        # 1st  test
        S.wvnb = 0.
        wn = S.wn()
        self.assertEqual(wn[0], self.l**2. / 2.)
        self.assertEqual(wn[1], self.l**2. / 4.)
        self.assertTrue(len(wn), 2)
        wn1 = wn*1.

        # test 2
        S.wvnb = 1.
        wn = S.wn()
        self.assertEqual(wn1[0]*np.exp(-(self.l**2./4.)), wn[0])
        self.assertEqual(wn1[1]*np.exp(-(self.l**2./8.)), wn[1])

    def test_exp(self):
        S = ExponentialSpectrum(niter=self.niter, l=self.l, theta=self.theta, thetas=self.thetas, phi=self.phi, phis=self.phis, freq=self.freq)
        S.wn()

        # test 1
        S.wvnb = 0.
        wn = S.wn()
        self.assertEqual(self.l**2. * 1.**-1.5, wn[0])
        self.assertEqual(self.l**2.*0.25*1.**-1.5, wn[1])

        # test 2
        S.wvnb = 1.
        wn = S.wn()
        self.assertEqual(self.l**2.*(1.+self.l**2.)**-1.5, wn[0])
        self.assertEqual(0.25*self.l**2.*(1.+self.l**2./4.)**-1.5, wn[1])


if __name__ == '__main__':
    unittest.main()
