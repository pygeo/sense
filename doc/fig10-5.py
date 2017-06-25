"""
Fig 10-5 in Ulaby (2014)
check of Dobson 85 model


TODO final check
"""
import os
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + os.sep + '..')

from sense.dielectric import Dobson85
from sense.core import Reflectivity

fig = plt.figure(figsize=(8,3))

ax1 = fig.add_subplot(131)
ax2 = fig.add_subplot(132)
ax3 = fig.add_subplot(133)

theta_deg = np.linspace(0.,90.)
theta = np.deg2rad(theta_deg)

freq = 1.5

# Fresnel reflectivity (looks o.k.)
mv = 0.35
D = Dobson85(sand=0.3333, clay=0.33,freq=freq, mv=mv)
G1 = Reflectivity(D.eps, theta)
ax1.plot(theta_deg, G1.h, 'b-')
ax1.plot(theta_deg, G1.v, 'r-')
mv = 0.05
D = Dobson85(sand=0.3333, clay=0.33,freq=freq, mv=mv)
G2 = Reflectivity(D.eps, theta)
ax1.plot(theta_deg, G2.h, 'b--')
ax1.plot(theta_deg, G2.v, 'r--')

ax1.grid()
ax1.set_xlim(0.,90.)
ax1.set_ylim(0.,1.)

plt.show()
