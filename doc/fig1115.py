"""
compare results of implemented models
against Fig 11.15 from Ulaby (2014)
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + os.sep + '..')

import numpy as np

#from sense.surface import Dubois95, Oh92
from sense.util import f2lam
from sense.model import SingleScatRT

from sense.soil import Soil
from sense.canopy import OneLayer

import matplotlib.pyplot as plt

plt.close('all')

theta_deg = np.arange(0.,70.)
theta = np.deg2rad(theta_deg)

f  = 13.  # GHz
lam = f2lam(f)  # m

s = 0.0015  # m
l = 0.015  # m



omega = 0.1


#guessed from figure in chapter 4 for the time being
eps = 15. - 4.0j


models = {'surface' : 'Dubois95', 'canopy' : 'turbid_rayleigh'}

pol='vv'

# short alfalfa
d = 0.17
tau = 2.5
ke = tau/d
omega = 0.27
ks=omega*ke
S = Soil(f=f, s=s, l=l, eps=eps)
C = OneLayer(ke_h=ke, ke_v=ke, d=d, ks_v=ks, ks_h=ks)
RT = SingleScatRT(theta=theta, models=models, surface=S, canopy=C, freq=f)
RT.sigma0()

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(theta_deg, 10.*np.log10(RT.stot[pol]), label='short', color='b')

# tall alfalfa
d = 0.55
tau = 0.45
ke = tau/d
omega = 0.175
ks=omega*ke
S = Soil(f=f, s=s, l=l, eps=eps)
C = OneLayer(ke_h=ke, ke_v=ke, d=d, ks_v=ks, ks_h=ks)
RT = SingleScatRT(theta=theta, models=models, surface=S, canopy=C, freq=f)
RT.sigma0()
ax.plot(theta_deg, 10.*np.log10(RT.stot[pol]), label='tall', color='r')

ax.legend()
ax.set_title('Fig 11-15 Alfalfa')


ax.grid()
ax.set_xlabel('incidence angle')
ax.set_ylabel('sigma')
ax.set_xlim(0.,70.)
ax.set_ylim(-16.,6.)

plt.show()
