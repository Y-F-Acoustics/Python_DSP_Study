# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 01:48:27 2021

@author: Y.F.A

Chapter 2: Discrete Time Signal
Section 2.1.2: Fundamental Periodic Time Signal
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import art3d

# Period
omega = np.pi / 8
Tend = 64
T = np.arange(0, Tend)


# Euler's Formula
euler = np.exp(1j * omega * T)
cosine = np.real(euler)
sine = np.imag(euler)


# Cosine
fig1 = plt.figure()
ax1 = fig1.add_subplot(1, 1, 1)
ax1.stem(T, cosine, use_line_collection=True, markerfmt = "x", basefmt=" ")
ax1.grid()
ax1.set_xlabel("Time $n$")
ax1.set_ylabel("Real Part")


# Sine
fig2 = plt.figure()
ax2 = fig2.add_subplot(1, 1, 1)
ax2.stem(T, sine, use_line_collection=True, markerfmt = ".", basefmt=" ")
ax2.grid()
ax2.set_xlabel("Time $n$")
ax2.set_ylabel("Imaginary Part")


# Complex Exponential Function on Complex Plane
fig3 = plt.figure()
ax3 = fig3.add_subplot(1, 1, 1)
ax3.plot(cosine, sine, "o")
ax3.axis("Square")
for i in T:
    ax3.plot([0, cosine[i]], [0, sine[i]], "Blue")
    
ax3.grid()
ax3.set_xlabel("Real Part")
ax3.set_ylabel("Imaginary Part")


# Complex Exponential Function in 3D
fig4 = plt.figure()
ax4 = Axes3D(fig4)
ax4.plot(T, cosine, sine, "o", label="$e^{j\omega n}$")
for l, m, n in zip(T, cosine, sine):
    line = art3d.Line3D(*zip((l, 0, 0), (l, m, n)))
    ax4.add_line(line)

Rmax = 3
Real_plane = -Rmax * np.ones(len(T))
Imag_plane = -Real_plane
ax4.plot(T, cosine, Real_plane, "x", label="$\cos \ \omega n$")
ax4.plot(T, Imag_plane, sine, ".", label="$\sin \ \omega n$")
ax4.set_xlim(0, Tend)
ax4.set_ylim(-Rmax, Rmax)
ax4.set_zlim(-Rmax, Rmax)
ax4.set_xlabel("Time $n$")
ax4.set_ylabel("Real Part")
ax4.set_zlabel("Imaginary Part")
ax4.legend(loc="upper left")