"""
implements the I2EM model (see Ulaby (2014), Chapter 10
backscattering model for single scale random surfaces
"""


class I2EM(object):
    def __init__(self, eps, ks, theta):
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
        self.eps = eps
        self.ks = ks
        self.theta = theta
        self._calc_sigma_backscatter()

    def _calc_sigma_backscatter(self):
        # define backscatter geometry
        theta_s = self.theta*1.
        phi_s = np.deg2rad(180.)

        # calculate backscattering coefficients
        self.vv, self.hh = self.i2em_bistatic()
        self.hv = self.i2em_cross()
