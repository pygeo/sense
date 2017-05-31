"""
Basic class for scattering modelling
"""

import numpy as np
from . surface import Oh92

class Model(object):
    def __init__(self, **kwargs):
        self.theta = kwargs.get('theta', None)

        self._check1()

    def _check1(self):
        assert self.theta is not None, 'ERROR: no incidence angle was specified!'

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
            assert False, 'Not supported for dictionaries yet!'
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
        surface : Surface description
            object describing the surface
        canopy : Canopy description
            object describing the canopy
        models : dict
            dictionary with configuration of scattering models
        """
        super(SingleScatRT, self).__init__(**kwargs)
        self.surface = kwargs.get('surface', None)
        self.canopy = kwargs.get('canopy', None)
        self.models = kwargs.get('models', None)
        
        #self.cground = kwargs.get('canopy_ground', None)
        #self.gcg = kwargs.get('ground_canopy_ground', None)
        self._check()

    def _check(self):
        assert self.surface is not None
        assert self.canopy is not None
        assert self.models is not None

        for k in ['surface', 'canopy']:
            assert k in self.models.keys()  # check that all models have been specified

    def _sigma0(self):
        """
        basic calculation of Sigma0
        based on Eq. 11.17 in Ulaby and Long (2014)
        """

        # ground backscatter = attenuated surface
        G = Ground(self.surface, self.canopy, self.models['surface'], self.models['canopy'], theta=self.theta)
        s0g = G.sigma()
        # canopy contribution
        #s0c = self.canopy.sigma()
        # total canopy ground contribution
        #s0cgt = self.cground.sigma()
        # ground-canopy-ground interaction
        #s0gcg = self.gcg.sigma()

        return None #s0g + s0c + s0cgt + s0gcg



class Ground(object):
    """
    calculate the (attenuated) ground contribution
    sigma_pq
    where p is receive and q is transmit polarization
    """
    def __init__(self, S, C, RT_s, RT_c, theta=None):
        """
        calculate the attenuated ground contribution
        to the scattering

        Parameters
        ----------
        S : object
            descibing the surface properties
        C : object
            describing the canopy properties
        RT_s : str
            key describing the surface scattering model
        RT_c : str
            key specifying the canopy scattering model
        """
        self.S = S
        self.C = C
        self.theta = theta
        self._check(RT_s, RT_c)
        self._set_models(RT_s, RT_c)

    def _set_models(self, RT_s, RT_c):
        # set surface model
        if RT_s == 'Oh92':
            self.rt_s = Oh92(self.S.eps, self.S.ks, self.theta)
        else:
            assert False


        # set canopy models
        if RT_c == 'dummy':
            print('Still need to implement the canopy model here')
        else:
            assert False, 'Invalid canopy scattering model'

    def _check(self, RT_s, RT_c):
        valid_surface = ['Oh92']
        valid_canopy = ['dummy']
        assert RT_s in valid_surface, 'ERROR: invalid surface scattering model was chosen!'
        assert RT_c in valid_canopy
        assert self.theta is not None

    def sigma(self):
        """
        calculate the backscattering coefficient
        Eq. 11.4, p.463 Ulaby (2014)
        """

        # canopy transmisivities
        t_h = self.C.t_h
        t_v = self.C.t_v

        # backscatter
        s_hh = self.rt_s.hh*t_h*t_h
        s_vv = self.rt_s.vv*t_v*t_v
        s_hv = self.rt_s.hv*t_v*t_h

        return {'vv' : s_vv, 'hh' : s_hh, 'hv' : s_hv}



class CanopyHomo(object):
    """
    homogeneous canopy
    assumes homogeneous vertical distribution of scatterers

    in that case the Lambert Beer law applies
    """
    def __init__(self, **kwargs):
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
        self.ke_h = kwargs.get('ke_h', None)
        self.ke_v = kwargs.get('ke_v', None)
        self.theta = kwargs.get('theta', None)
        self.d = kwargs.get('d', None)

        self.tau_h = self._tau(self.ke_h)
        self.tau_v = self._tau(self.ke_v)
        self.t_h = np.exp(-self.tau_h)
        self.t_v = np.exp(-self.tau_v)

    def _tau(self, k):
        # assumption: extinction is isotropic
        return k*self.d/np.cos(self.theta)



# 502-503




