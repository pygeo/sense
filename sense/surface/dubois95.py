"""
implements the Dubois95 model
as described in Ulaby (2014), Chapter 10.6
"""
class Dubois95(object):
    def __init__(self, eps, theta):
        self.theta = theta
        self.vv, self.hh = self._calc_sigma()

    def _calc_sigma(self):
        lam = 
        return self._vv(), self._hh()

    def _hh(selfi, lam, ks):
        """
        lam : float
            wavelength in cm


        """
        return 10**(-2.75)*((np.cos(self.theta)**1.5)/np.sin(self.theta)**5.)*(10.**(0.028*real(self.eps))*np.tan(self.theta))*(ks*np.sin(self.theta)**1.4*lam**0.7)  # eq. 10.41a0

    def _vv(self, lam, ks):
        return 10.**(-2.35)*(np.cos(self.theta)**3./np.sin(self.theta)**3.)*(10.**0.046*np.real(self.eps)*np.tan(self.theta))*(ks*np.sin(self.theta))**1.1*lam**0.7
