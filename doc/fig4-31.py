"""
Fig 4.31 in Ulaby (2014)
check of Dobson 85 model


TODO final check
"""
import os
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + os.sep + '..')
from sense.dielectric import Dobson85


mv = np.linspace(0.,0.5, 100)
f = 5.

fig = plt.figure()
ax1 = fig.add_subplot(111)

D = Dobson85(sand=0.5, clay=0.33,freq=f,mv=mv)
e = D.eps

ax1.plot(mv, np.real(e), color='blue')
ax1.plot(mv, np.imag(e), color='red')
ax1.grid()
ax1.set_title('Fig 4-31')
ax1.set_xlim(0.,0.45)
ax1.set_ylim(0.,27.)

plt.show()
