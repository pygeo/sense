import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + os.sep + "..")

import numpy as np
from sense import model
from sense.soil import Soil
from sense.canopy import OneLayer

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
        can = OneLayer(ke_h=0.05, ke_v=0.02, d=3., ks_h = 0.02, ks_v = 0.003)
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
        soil = Soil(eps=eps, f=5., s=0.02)
        can = OneLayer(ke_h=0.05, ke_v=0.02, d=3., ks_h = 0.02, ks_v = 0.003)
        S = model.SingleScatRT(surface=soil, canopy=can, models=models, theta=self.theta, freq=self.freq)
        S.sigma0()

        models = {'surface': 'Dubois95', 'canopy': stype}
        eps = 5. -3.j

        S = model.SingleScatRT(surface=soil, canopy=can, models=models, theta=self.theta, freq=self.freq)
        S.sigma0()




if __name__ == '__main__':
    unittest.main()
