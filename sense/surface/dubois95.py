"""
implements the Dubois95 model
as described in Ulaby (2014), Chapter 10.6
"""
import numpy as np

class Dubois95(object):
    def __init__(self, eps, ks, theta, lam=None):
        """
        Parameters
        ----------
        lam : float
            wavelength in meter
        """
        self.theta = theta
        self.ks = ks
        self.eps = eps
        self.lam = lam
        assert self.lam is not None
        self.vv, self.hh = self._calc_sigma()

    def _calc_sigma(self):
        lam = self.lam*100. 
        return self._vv(lam, self.ks), self._hh(lam, self.ks)

    def _hh(self, lam, ks):
        """
        lam : float
            wavelength in cm
        """
        return 10**(-2.75)*((np.cos(self.theta)**1.5)/np.sin(self.theta)**5.)*(10.**(0.028*np.real(self.eps))*np.tan(self.theta))*(ks*np.sin(self.theta)**1.4*lam**0.7)  # eq. 10.41a0

    def _vv(self, lam, ks):
        """ eq. 10.41b """
        b = 10.**(-2.35)*((np.cos(self.theta)**3.) / (np.sin(self.theta)**3.))
        c = 10.**(0.046*np.real(self.eps)*np.tan(self.theta))
        d = (ks*np.sin(self.theta))**1.1*lam**0.7

        return b*c*d

