"""
implements the I2EM model (see Ulaby (2014), Chapter 10
backscattering model for single scale random surfaces
"""
from . scatter import SurfaceScatter
import numpy as np

class I2EM(SurfaceScatter):
    def __init__(self, eps, ks, kl, theta):
        """
        Parameters
        ----------
        eps : complex
            relative dielectric permitivity
        ks : float
            vertical surface roughness
        theta : float
            incidence angle [rad]
        """
        super(I2EM, self).__init__(eps, ks, theta, kl=kl)
        self._calc_sigma_backscatter()

    def _calc_sigma_backscatter(self):
        # define backscatter geometry
        theta_s = self.theta*1.
        phi_s = np.deg2rad(180.)

        # calculate backscattering coefficients
        self.vv, self.hh = self._i2em_bistatic()
        self.hv = self._i2em_cross()

    def _i2em_bistatic(self):
        return None, None

    def _i2em_cross(self):
        return None
