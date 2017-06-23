import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + os.sep + "..")

import numpy as np
from sense import model
from sense.soil import Soil
from sense.canopy import OneLayer
from sense.surface import Dubois95

class TestModel(unittest.TestCase):
    def test_init(self):
        M = model.Model(theta=np.arange(10))

class TestSingle(unittest.TestCase):
    def setUp(self):
        self.theta = np.arange(1.,80.)
        self.freq  = 5.

    def test_init(self):
        # some dummy variables
        models = {'surface': 'abc', 'canopy':'efg'}
        S = model.SingleScatRT(surface='abc', canopy='def', models=models, theta=self.theta, freq=self.freq)

    def test_scat_isotropic(self):
        # some dummy variables

        stype='turbid_isotropic'

        models = {'surface': 'Oh92', 'canopy': stype}
        eps = 5. -3.j
        soil = Soil(eps=eps, f=5., s=0.02)
        can = OneLayer(ke_h=0.05, ke_v=0.05, d=3., ks_h = 0.02, ks_v = 0.02)
        S = model.SingleScatRT(surface=soil, canopy=can, models=models, theta=self.theta, freq=self.freq)
        S.sigma0()

        models = {'surface': 'Dubois95', 'canopy': stype}
        eps = 5. -3.j

        S = model.SingleScatRT(surface=soil, canopy=can, models=models, theta=self.theta, freq=self.freq)
        S.sigma0()

    def test_scat_rayleigh(self):

        stype = 'turbid_rayleigh'
        models = {'surface': 'Oh92', 'canopy': stype}
        eps = 5. -3.j
        d = 3
        ke = 0.05
        omega=0.2
        soil = Soil(eps=eps, f=5., s=0.02)
        can = OneLayer(ke_h=ke, ke_v=ke, d=d, ks_h = omega*ke, ks_v = omega*ke)
        S = model.SingleScatRT(surface=soil, canopy=can, models=models, theta=self.theta, freq=self.freq)
        S.sigma0()

        models = {'surface': 'Dubois95', 'canopy': stype}
        eps = 5. -3.j

        S = model.SingleScatRT(surface=soil, canopy=can, models=models, theta=self.theta, freq=self.freq)
        S.sigma0()

        # compare results against results obtained through Eq. 11.23 (analytic way)
        theta = self.theta*1.
        ks = 0.02
        SMODEL = Dubois95(eps, ks, theta, lam=0.05)
        s_hh_surf = SMODEL.hh

        trans = np.exp(-d*ke/np.cos(theta))
        n=2.  # 2== coherent
        RHO_h = S.G.rho_h
        ref_hh = trans**2. * s_hh_surf + (3.*omega/4.)*np.cos(theta)*(1.-trans**2.)*(1.+RHO_h**2.*trans**2.)+3.*n*omega*ke*d*RHO_h*trans**2.

        pol = 'hh'
        self.assertEqual(len(ref_hh), len(S.stot[pol]))
        #for i in xrange(len(ref_hh)):
        #self.assertEqual(ref_hh, S.stot['hh'])
        #self.assertEqual(ref_vv, res['vv'])


if __name__ == '__main__':
    unittest.main()
