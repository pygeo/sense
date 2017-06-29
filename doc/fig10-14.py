"""
comparison with figure 10-14
in Ulaby 2014

can actully not use this fugure as not e´nough information
in the reference to reproduce the figure


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


theta_deg = np.linspace(0.,70., 4)
theta = np.deg2rad(theta_deg)

f = plt.figure()
ax1 = f.add_subplot(121)
ax2 = f.add_subplot(122)

f = 3.

l = 10./100.



hh1=[]
hh2=[]
vv1=[]
vv2=[]
hv1=[]
hv2=[]
xpol = False
auto=False
ks = []

theta = np.deg2rad(30.)


S = np.linspace(0.001,0.1,4)


for s in S:
    I1 = I2EM(f, 4.7-0.6j, s, l, theta, acf_type='gauss', xpol=xpol, auto=auto)
    hh1.append(I1.hh)
    vv1.append(I1.vv)
    ks.append(I1.ks)
    if xpol:
        hv1.append(I1.hv)

hh1 = np.array(hh1)
vv1 = np.array(vv1)
if xpol:
    hv1 = np.array(hv1)
ks = np.array(ks)

p1 = hh1/vv1
if xpol:
    q1 = hv1/vv1



ax1.plot(ks, db(p1), color='red')
ax1.set_xlim(0.,4.)
ax1.set_ylim(-3.5,0.5)

if xpol:
    ax2.plot(ks, db(q1), color='red')



plt.show()
