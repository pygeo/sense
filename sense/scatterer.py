"""
Definition of scatter types
"""

class Scatterer(object):
    def __init__(self, **kwargs):
        self.sigma_s_hh = kwargs.get('sigma_s_hh', None)  # particle scattering cross area
        assert self.sigma_s_hh is not None, 'Particle HH scattering cross section needs to be specified [m**-2]'

        self.sigma_s_vv = kwargs.get('sigma_s_vv', None)  # particle scattering cross area
        assert self.sigma_s_vv is not None, 'Particle VV scattering cross section needs to be specified [m**-2]'

        self.sigma_s_hv = kwargs.get('sigma_s_hv', None)  # particle scattering cross area
        assert self.sigma_s_hv is not None, 'Particle HV scattering cross section needs to be specified [m**-2]'


class ScatIso(Scatterer):
    """
    Isotropic scatterer definition
    see 11.2 in Ulaby (2014)
    """
    def __init__(self, **kwargs):
        super(ScatIso, self).__init__(**kwargs)
        # scattering coefficients need to be the same in isotropic case (eq. 11.19)
        assert self.sigma_s_hh == self.sigma_s_vv
        assert self.sigma_s_hh == self.sigma_s_hv

    def sigma_v_back(self, Nv):
        """
        volume backscattering coefficient
        for the isotropic case this corresponds to the
        volume scattering coefficient ks
        """
        return {'hh' : Nv*self.sigma_s_hh, 'vv' : Nv*self.sigma_s_vv, 'hv' : Nv*self.sigma_s_hv}

    def sigma_v_bist(self, Nv):
        # same as volume backscattering coefficient (Eq. 11.19)
        return self.sigma_v_back(Nv)



class ScatRayleigh(Scatterer):
    """
    Isotropic scatterer definition
    see 11.2 in Ulaby (2014)
    """
    def __init__(self, **kwargs):
        super(ScatRayleigh, self).__init__(**kwargs)

    def sigma_v_back(self, Nv):
        print 'Nv: ', Nv
        return {'hh' : 1.5*Nv*self.sigma_s_hh, 'vv' : 1.5*Nv*self.sigma_s_vv, 'hv' : 1.5*Nv*self.sigma_s_hv}

    def sigma_v_bist(self, Nv):
        # same as sigma_v_back (Eq. 11.22)
        return self.sigma_v_back(Nv)
