"""
implements the I2EM model (see Ulaby (2014), Chapter 10
backscattering model for single scale random surfaces


The code originates from ideas obtained from the supplement
of Ulaby et al (2014)
"""
from scatter import SurfaceScatter
import numpy as np

from .. util import f2lam
import math

class I2EM(SurfaceScatter):
    def __init__(self, f, eps, s, l, theta):
        """
        Parameters
        ----------
        f : float
            frequency [GHz]
        eps : complex
            relative dielectric permitivity
        s : float
            vertical surface roughness  [m]
        l : float
            autocorrelation length [m]
        theta : float
            incidence angle [rad]
        """


        self.freq = f
        lam = f2lam(self.freq)
        k = 2.*np.pi/lam
        self.k = k
        self.s = s
        self.l = l
        super(I2EM, self).__init__(eps, k*s, theta, kl=k*l)
        
        # assume backscatter geometry
        self.phi = 0.
        self.thetas = self.theta*1.
        self.phis = np.deg2rad(180.)

        # do initializations for backscatter calculations
        self._init_hlp()
        self.init_model()

        # calculate the actual backscattering coefficients
        self._calc_sigma_backscatter()

    def init_model(self):
        """
        initialize model for calculations
        """
        self.niter = self._estimate_itterations()

    def _estimate_itterations(self):
        """
        estimate the number of necessary itterations for 
        the integral calculations
        """

        err = 1.E8
        Ts = 1
        while err > 1.0e-8:
            Ts += 1
            err = ((self._ks2 *(self._cs + self._css)**2 )**Ts) / math.factorial(Ts)
        return Ts


    def _init_hlp(self):
        """ initiate help variables """
        self._ks2 = self.ks**2.
        self._cs = np.cos(self.theta)
        self._s = np.sin(self.theta)
        self._sf = np.sin(self.phi)
        self._cf = np.cos(self.phi)
        self._ss = np.sin(self.thetas)
        self._css = np.cos(self.thetas)
        self._cfs = np.cos(self.phis)
        self._sfs = np.sin(self.phis)
        self._s2 = self.s**2.
        self._kx = self.k*self.s*self._cf
        self._ky = self.k*self.s*self._sf
        self._kz = self.k*self._cs

        self._ksx = self.k * self._ss *self._cfs
        self._ksy = self.k * self._ss *self._sfs
        self._ksz = self.k * self._css

    def _calc_sigma_backscatter(self):
        assert isinstance(self.theta, float), 'Currently array processing not supported yet!'
        # calculate backscattering coefficients
        self.vv, self.hh = self._i2em_bistatic()
        self.hv = self._i2em_cross()

    def _i2em_bistatic(self):
        sigvv = 0.
        sighh = 0.
        
        Ivv, Ihh = self._calc_Ipp()
        Ivv_abs = np.abs(Ivv)
        Ihh_abs = np.abs(Ihh)
        wn = self.calc_roughness_spectrum() 

        # calculate shadowing effects
        ShdwS = self._calc_shadowing()

        # calculate the integral
        idx = np.arange(self.niter)+1
        fac = map(math.factorial, idx)
        a0 = wn / fac * (self.s**(2.*idx))

        # final backscatter calculation
        hlp = 0.5*self.k**2*np.exp(-self.s**2*(self._kz**2.+self._ksz**2.))
        sigvv = np.sum(a0 * Ivv_abs**2.) * ShdwS * hlp
        sighh = np.sum(a0 * Ihh_abs**2.) * ShdwS * hlp
        return  sigvv, sighh

    def _i2em_cross(self):
        print('TODO: CROSS SPECTRUM')
        return None


    def _calc_shadowing(self):
        print('TODO: shadowing')
        return 1.  ## todo

    def calc_roughness_spectrum(self):
        # todo
        print('TODO: roughness spectrum')
        return np.ones(self.niter)

    def _calc_Ipp(self):
        Ivv = 1.
        Ihh = 1.
        print('TODO Ipp')
        return Ivv, Ihh


