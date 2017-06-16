"""
Definition of scatter types
"""

class Scatterer(object):
    def __init__(self, **kwargs):
        pass

class ScatIso(Scatterer):
    """
    Isotropic scatterer definition
    see 11.2 in Ulaby (2014)
    """
    def __init__(self, **kwargs):
        super(ScatIso, self).__init__(**kwargs)
        print('todo, not clear how Nv needs to be incorporated !')

class ScatRayleigh(Scatterer):
    """
    Isotropic scatterer definition
    see 11.2 in Ulaby (2014)
    """
    def __init__(self, **kwargs):
        super(ScatRayleigh, self).__init__(**kwargs)
        print('todo, not clear how Nv needs to be incorporated !')
