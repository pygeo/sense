"""
compare results of implemented models
against Fig 10.42 from Ulaby (2014)
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + os.sep + '..')

import numpy as np

from sense.surface import Dubois95, Oh92, I2EM
from sense.util import f2lam

import matplotlib.pyplot as plt

plt.close('all')

theta = np.deg2rad(40.)
eps = 5.46 -0.37j



s_vv_o = []
s_hh_o = []
s_vv_d = []
s_hh_d = []
s_vv_i = []
s_hh_i = []


f  = 1.6  # GHz
lam = f2lam(f)  # m
k = 2.*np.pi/lam



l = 0.014   #todo
acf_type='exp15'

S= np.linspace(0.0001,0.03, 500)

KS = []
for s in S:

    ks = k*s
    # Dubois 95
    D = Dubois95(eps, ks, theta, lam)
    s_hh_d.append(D.hh)
    s_vv_d.append(D.vv)

    # Oh 1992
    O = Oh92(eps, ks, theta)
    s_vv_o.append(O.vv)
    s_hh_o.append(O.hh)

    # IEM
    I = I2EM(f, eps, s, l, theta, acf_type=acf_type)
    s_vv_i.append(I.vv)
    s_hh_i.append(I.hh)

    KS.append(ks)

KS = np.array(KS)

s_vv_o = 10.*np.log10(np.array(s_vv_o))
s_hh_o = 10.*np.log10(np.array(s_hh_o))

s_vv_d = 10.*np.log10(np.array(s_vv_d))
s_hh_d = 10.*np.log10(np.array(s_hh_d))

s_vv_i = 10.*np.log10(np.array(s_vv_i))
s_hh_i = 10.*np.log10(np.array(s_hh_i))

f = plt.figure()
ax1 = f.add_subplot(121)
ax2 = f.add_subplot(122)

ax1.plot(KS, s_vv_d, color='red', label='SMART, Dubois95')
ax1.plot(KS, s_vv_o, color='blue', label='PRISM1, Oh92')
ax1.plot(KS, s_vv_i, color='green', label='I2EM')
ax1.grid()
ax1.legend()
ax1.set_xlim(0.06,0.82)
ax1.set_ylim(-35.,-10.)
ax1.set_xlabel('ks')
ax1.set_ylabel('backscattering coefficient VV [dB]')

ax2.plot(KS, s_hh_d, color='red', label='SMART, Dubois95')
ax2.plot(KS, s_hh_o, color='blue', label='PRISM1, Oh92')
ax2.plot(KS, s_hh_i, color='green', label='I2EM')
ax2.grid()
ax2.legend()
ax2.set_xlim(0.06,0.82)
ax2.set_ylim(-35.,-10.)
ax2.set_xlabel('ks')
ax2.set_ylabel('backscattering coefficient HH [dB]')






plt.show()
