# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 01:41:35 2021

@author: Y.F.A

Chapter 2: Discrete Time Signal
Section 2.2.1: Definition of Discrete Time Fourier Transform
"""

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Frequency Range and weight
w = np.linspace(-np.pi, np.pi, 1024, endpoint=False)

# Unit Impulse
Impulse = np.zeros(9)
Impulse[4] = 1
_, hImpulse = signal.freqz(Impulse, 1, w)
fig1 = plt.figure()
ax1 = fig1.add_subplot(1, 1, 1)
ax1.plot(w, np.abs(hImpulse))
ax1.set_xlim(-np.pi, np.pi)
ax1.grid()
ax1.set_xlabel("Frequency $\omega$ [rad]")
ax1.set_ylabel("$|\delta(e^{j\omega})$|")


# Square rc[n] = [1, 1, 1, 1, 1, 1, 1, 1]
rc = np.ones(8)
_, hSquare = signal.freqz(rc, 1, w)
fig2 = plt.figure()
ax2 = fig2.add_subplot(1, 1, 1)
ax2.plot(w, np.abs(hSquare))
ax2.set_xlim(-np.pi, np.pi)
ax2.grid()
ax2.set_xlabel("Frequency $\omega$ [rad]")
ax2.set_ylabel("$|R_\mathrm{c}(e^{j\omega})$|")


# Exponential Function a[n] = (0.5 ** n) * u0[n]
n = np.arange(0, 2**12)
a = 0.5 ** n
_, hA = signal.freqz(a, 1, w)
fig3 = plt.figure()
ax3 = fig3.add_subplot(1, 1, 1)
ax3.plot(w, np.abs(hA))
ax3.set_xlim(-np.pi, np.pi)
ax3.grid()
ax3.set_xlabel("Frequency $\omega$ [rad]")
ax3.set_ylabel("$|A(e^{j\omega})$|")
