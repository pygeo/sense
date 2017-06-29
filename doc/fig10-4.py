"""
soil dielectric model behavior
comparison with figure 10-4 in Ulaby 2014
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + os.sep + '..')

from sense.soil import Soil

plt.close('all')


mv = np.linspace(0.001,0.38)

f = plt.figure()
ax = f.add_subplot(111)

c = 'blue'
S = Soil(sand=0.306, clay=0.135, mv=mv, s=0.01, f=1.4)
ax.plot(mv, np.real(S.eps), color=c)
ax.plot(mv, np.imag(S.eps), color=c, linestyle='--')


c = 'red'
S = Soil(sand=0.306, clay=0.135, mv=mv, s=0.01, f=6.)
ax.plot(mv, np.real(S.eps), color=c)
ax.plot(mv, np.imag(S.eps), color=c, linestyle='--')


c = 'green'
S = Soil(sand=0.306, clay=0.135, mv=mv, s=0.01, f=12.)
ax.plot(mv, np.real(S.eps), color=c)
ax.plot(mv, np.imag(S.eps), color=c, linestyle='--')


c = 'black'
S = Soil(sand=0.306, clay=0.135, mv=mv, s=0.01, f=18.)
ax.plot(mv, np.real(S.eps), color=c)
ax.plot(mv, np.imag(S.eps), color=c, linestyle='--')






ax.set_xlim(0.,0.5)
ax.set_ylim(0.,30.)
ax.grid()



plt.show()
