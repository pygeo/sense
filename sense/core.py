import numpy as np

class Fresnel0(object):
    def __init__(self, e):
        """
        calculate the Nadir Fresnel reflectivity
        e.g. Ulaby (2014), eq. 10.36
        
        Parameters
        ----------
        e : complex
            complex relative dielectric permitivity
        """
        self.x = self._calc(e)

    def _calc(self, e):
        return np.abs( (1.-np.sqrt(e))/(1.+np.sqrt(e))   )**2.
