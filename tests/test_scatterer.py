import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + os.sep + "..")

from sense.scatterer import Scatterer, ScatIso, ScatRayleigh


class TestSingle(unittest.TestCase):
    def setUp(self):
        self.s_s_hh = 1.
        self.s_s_vv = 2.
        self.s_s_hv = 3.

    def test_scatterer_init(self):
        S = Scatterer(sigma_s_hh = self.s_s_hh, sigma_s_vv = self.s_s_vv, sigma_s_hv = self.s_s_hv)

    def test_iso(self):
        S = ScatIso(sigma_s_hh = self.s_s_hh, sigma_s_vv = self.s_s_hh, sigma_s_hv = self.s_s_hh)
        r = S.sigma_v_back(1.)
        self.assertTrue(isinstance(r, dict))
        self.assertEqual(len(r), 3)

    def test_rayleigh(self):
        S = ScatRayleigh(sigma_s_hh = self.s_s_hh, sigma_s_vv = self.s_s_vv, sigma_s_hv = self.s_s_hv)
        r = S.sigma_v_back(1.)
        self.assertTrue(isinstance(r, dict))
        self.assertEqual(len(r), 3)

if __name__ == '__main__':
    unittest.main()
