import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + os.sep + "..")

from sense.surface import GaussianSpectrum, ExponentialSpectrum
import numpy as np

class TestRoughness(unittest.TestCase):
    def setUp(self):
        self.niter=3
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

    def test_exp15(self):
        S = ExponentialSpectrum(niter=self.niter, l=self.l, theta=self.theta, thetas=self.thetas, phi=self.phi, phis=self.phis, freq=self.freq)
        S.wn()





if __name__ == '__main__':
    unittest.main()
