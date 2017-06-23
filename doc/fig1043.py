"""
compare results of implemented models
against Fig 10.43 from Ulaby (2014)
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + os.sep + '..')

import numpy as np

from sense.surface import Dubois95, Oh92
from sense.util import f2lam

import matplotlib.pyplot as plt

plt.close('all')

theta = np.deg2rad(40.)
#eps = 5.46 -0.37j



s_vv_o = []
s_hh_o = []
s_vv_d = []
s_hh_d = []


f  = 1.6  # GHz
lam = f2lam(f)  # m
k = 2.*np.pi/lam

ks = 0.4
s = ks/k
l=6.*s

DC = np.arange(3.,35.)

for dc in DC:

    eps = dc -0.37j  #todo imaginary part dynamic as well

    # Dubois 95
    D = Dubois95(eps, ks, theta, lam)
    s_hh_d.append(D.hh)
    s_vv_d.append(D.vv)

    # Oh 1992
    O = Oh92(eps, ks, theta)
    s_vv_o.append(O.vv)
    s_hh_o.append(O.hh)



s_vv_o = 10.*np.log10(np.array(s_vv_o))
s_hh_o = 10.*np.log10(np.array(s_hh_o))

s_vv_d = 10.*np.log10(np.array(s_vv_d))
s_hh_d = 10.*np.log10(np.array(s_hh_d))

f = plt.figure()
ax1 = f.add_subplot(121)
ax2 = f.add_subplot(122)

ax1.plot(DC, s_vv_d, color='red', label='SMART, Dubois95')
ax1.plot(DC, s_vv_o, color='blue', label='PRISM1, Oh92')
ax1.grid()
ax1.legend()
ax1.set_xlim(3.,33.)
ax1.set_ylim(-22.,-6.)
ax1.set_xlabel('DC')
ax1.set_ylabel('backscattering coefficient VV [dB]')

ax2.plot(DC, s_hh_d, color='red', label='SMART, Dubois95')
ax2.plot(DC, s_hh_o, color='blue', label='PRISM1, Oh92')
ax2.grid()
ax2.legend()
ax2.set_xlim(3.,33.)
ax2.set_ylim(-22.,-6.)
ax2.set_xlabel('DC')
ax2.set_ylabel('backscattering coefficient HH [dB]')






plt.show()
