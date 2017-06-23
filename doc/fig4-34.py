"""
Fig 4.34 in Ulaby (2014)
check of Dobson 85 model


TODO final check
"""
import os
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + os.sep + '..')
from sense.dielectric import Dobson85


f = np.linspace(1.,18.)

fig = plt.figure()

ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

MV = [0.37,0.344,0.275,0.215,0.158,0.079,0.023]


for mv in MV:
    D = Dobson85(sand=0.3333, clay=0.33,freq=f,mv=mv)
    e = D.eps

    ax1.plot(f, np.real(e))
    ax2.plot(f, np.imag(e))

ax1.grid()
ax2.grid()

ax1.set_xlim(0.,18.)
ax1.set_ylim(0.,25)
ax2.set_xlim(ax1.get_xlim())
ax2.set_ylim(0.,10.)

plt.show()
