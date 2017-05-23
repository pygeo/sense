'''
Basic class for scattering modelling
'''

import numpy as np

class Model(object):
    def __init__(self):
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
        s0cgt

        return s0g + s0c + s0cgt + s0gcg

