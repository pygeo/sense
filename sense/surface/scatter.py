"""
Major surface scatter class
"""
class SurfaceScatter(object):
    def __init__(self, eps, ks, theta, kl=None, **kwargs):
        self.eps = eps
        self.ks = ks
        self.theta = theta
        self.kl = kl
        self._check()

    def _check(self):
        assert isinstance(self.eps, complex)
    
