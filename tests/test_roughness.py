import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + os.sep + "..")

from sense.surface import GaussianSpectrum

class TestRoughness(unittest.TestCase):
    def setUp(self):
        self.niter=3
        self.l = 0.1

    def tearDown(self):
        pass

    def test_gauss(self):
        S = GaussianSpectrum(niter=self.niter, l=self.l)





if __name__ == '__main__':
    unittest.main()
