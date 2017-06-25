"""
compare results of implemented models
against Fig 11.07 from Ulaby (2014)
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

f  = 3.  # GHz
lam = f2lam(f)  # m

s = 0.01  # m
l = 0.1  # m

omega = 0.1


#guessed from figure in chapter 4 for the time being

# canopy
ke=1.
ks=omega*ke

# results strongly depend on the surface scattering model chosen!
# Oh92 gives a much smoother response at low incidence angles compared
# to the Dubois95 model

# shape of ACL would certailny also play an important role!

models = {'surface' : 'Dubois95', 'canopy' : 'turbid_rayleigh'}
S = Soil(f=f, s=s, l=l, mv=0.2, sand=0.3, clay=0.3)

pol='vv'


d = 2.3
C = OneLayer(ke_h=ke, ke_v=ke, d=d, ks_v=ks, ks_h=ks)
RT = SingleScatRT(theta=theta, models=models, surface=S, canopy=C, freq=f)
RT.sigma0()

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(theta_deg, 10.*np.log10(RT.stot[pol]), label='STOT', color='k')
ax.plot(theta_deg, 10.*np.log10(RT.s0g[pol]), label='SIGGROUND', color='r')
ax.plot(theta_deg, 10.*np.log10(RT.s0c[pol]), label='SIG can', color='b')
ax.plot(theta_deg, 10.*np.log10(RT.s0cgt[pol]), label='SIG can ground', color='g')
ax.plot(theta_deg, 10.*np.log10(RT.s0gcg[pol]), label='SIG ground can ground', color='k', linestyle='--')
#ax.plot(theta_deg, 10.*np.log10(RT.G.rt_s.vv), label='surface', linestyle='-.')

#ax.legend()
ax.set_title('d='+str(d))


ax.grid()
ax.set_xlabel('incidence angle')
ax.set_ylabel('sigma')
ax.set_xlim(0.,70.)
ax.set_ylim(-50.,10.)

plt.show()
