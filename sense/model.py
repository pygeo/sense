"""
Basic class for scattering modelling
"""

import numpy as np

class Model(object):
    def __init__(self, **kwargs):
        pass

    def sigma0(self, **kwargs):
        '''
        calculate sigma

        Parameters
        ----------
        dB : bool
            return results in decibel
        pol : list
            list with polarizations pq
            whereas p=receive, q=transmit
            p,g can be either H or V
        '''

        self.dB = kwargs.get('dB', False)
        self.pol = kwargs.get('pol', [])
        self._check_pol()

        if self.dB:
            return 10.*np.log10(self._sigma0())
        else:
            return self._sigma0()

    def _sigma0(self, **kwargs):
        assert False, 'routine should be implemented in child class!'

    def _check_pol(self):
        if len(self.pol) == 0:
            assert 'ERROR: polarization needs to be specified'
        for k in self.pol:
            if k not in ['HH','VV','HV','VH']:
                assert False, 'Invalid polarization: ' + k



class SingleScatRT(Model):
    def __init__(self, **kwargs):
        """
        Single scattering model according to Ulaby and Long (2014)
        Eq. 11.17

        Parameters
        ----------
        ground : Model
            model for ground scattering
        canopy : Model
            Model for canopy scattering
        canopy_ground : Model
            model for canopy-ground scattering
        ground_canopy_ground : Model
            model for ground canopy interaction
        """
        super(SingleScatRT, self).__init__(**kwargs)
        self.ground = kwargs.get('ground', None)
        self.canopy = kwargs.get('canopy', None)
        self.cground = kwargs.get('canopy_ground', None)
        self.gcg = kwargs.get('ground_canopy_ground', None)
        self._check()

    def _check(self):
        assert self.ground is not None
        assert self.canopy is not None
        assert self.cground is not None
        assert self.gcg is not None

    def _sigma0(self):
        """
        basic calculation of Sigma0
        based on Eq. 11.17 in Ulaby and Long (2014)
        """

        # ground backscatter
        s0g = self.ground.sigma()
        # canopy contribution
        s0c = self.canopy.sigma()
        # total canopy ground contribution
        s0cgt = self.cground.sigma()
        # ground-canopy-ground interaction
        s0gcg = self.gcg.sigma()

        return s0g + s0c + s0cgt + s0gcg



class Ground(Model):
    """
    calculate the (attenuated) ground contribution
    sigma_pq
    where p is receive and q is transmit polarization
    """
    def __init__(self, S, C):
        """
        calculate the attenuated ground contribution
        to the scattering

        Parameters
        ----------
        S : Surface Model
            class of surface model. Needs to have
            attributes vv, hh, hv
        """
        super(Ground, self).__init__()





    def _sigma(self, C, S):
        """
        calculate the backscattering coefficient
        Eq. 11.4, p.463 Ulaby (2014)
        """

        # canopy transmisivities
        t_h = C.t_h
        t_v = C.t_v

        # backscatter
        s_hh = S.hh*t_h*t_h
        s_vv = S.vv*t_v*t_v
        s_hv = S.hv*t_v*t_h



class CanopyHomo(object):
    """
    homogeneous canopy
    assumes homogeneous vertical distribution of scatterers

    in that case the Lambert Beer law applies
    """
    def __init__(self, ke_h, ke_v, d, theta):
        """
        Parameters
        ----------
        ke_h, ke_v : float
            volume extinction coefficient [Np/m]
        d : float
            height of canopy layer
        theta : float, ndarray
            incidence angle [rad]
        """
        self.ke_h = ke_h
        self.ke_v = ke_v
        self.theta = theta
        self.d = d

        self.tau_h = self._tau(self.ke_h)
        self.tau_v = self._tau(self.ke_v)
        self.t_h = np.exp(-self.tau_h)
        self.t_v = np.exp(-self.tau_v)

    def _tau(self, k):
        # assumption: extinction is isotropic
        return k*self.d/np.cos(self.theta)



# 502-503




