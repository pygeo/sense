"""
comparison with figure 10-11 
in Ulaby 2014

for copol this works pretty good.
only very slight deviations for very large incidence angles
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + os.sep + '..')

import numpy as np

from sense.surface import I2EM

import matplotlib.pyplot as plt

def db(x):
    return 10.*np.log10(x)


plt.close('all')


theta_deg = np.linspace(0.,70.)
theta = np.deg2rad(theta_deg)

f = plt.figure()
ax = f.add_subplot(111)


eps = 11.3-1.5j
f = 3.
acf_type='exp15'




s1 = 0.5/100.
s2 = 1.5/100.
l = 0.1



hh1=[]
hh2=[]
vv1=[]
vv2=[]
hv1=[]
hv2=[]
for t in theta:
    I1 = I2EM(f, eps, s1, l, t, acf_type=acf_type, xpol=False)
    I2 = I2EM(f, eps, s2, l, t, acf_type=acf_type, xpol=False)
    hh1.append(I1.hh)
    hh2.append(I2.hh)
    vv1.append(I1.vv)
    vv2.append(I2.vv)
    #hv1.append(I1.hv)
    #hv2.append(I2.hv)

hh1 = np.array(hh1)
hh2 = np.array(hh2)
vv1 = np.array(vv1)
vv2 = np.array(vv2)
hv1 = np.array(hv1)
hv2 = np.array(hv2)



ax.plot(theta_deg, db(hh2), color='red', label='hh')
ax.plot(theta_deg, db(hh1), color='blue', label='hh')

ax.plot(theta_deg, db(vv2), color='red', label='vv', linestyle='--')
ax.plot(theta_deg, db(vv1), color='blue', label='vv', linestyle='--')

#ax.plot(theta_deg, db(hv2), color='red', label='hv', linestyle='.')
#ax.plot(theta_deg, db(hv1), color='blue', label='hv', linestyle='.')

ax.grid()
ax.set_xlim(0.,70.)
ax.set_ylim(-50.,30.)

plt.show()
