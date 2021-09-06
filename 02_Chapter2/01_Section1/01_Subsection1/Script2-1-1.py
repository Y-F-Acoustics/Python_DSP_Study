# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 01:54:56 2021

@author: Y.F.A

Chapter 2: Discrete Time Signal
Section 2.1.1: Fundamental Discrete Time Signal

"""

import numpy as np
import matplotlib.pyplot as plt

# Time Range
T = np.arange(-5, 11)
Tbegin = T[0]
Tend = T[-1]

# Unit Impulse
Impulse = np.zeros(len(T))
Impulse[5] = 1
fig1 = plt.figure()
ax1 = fig1.add_subplot(1, 1, 1)
ax1.stem(T, Impulse, use_line_collection=True, basefmt = " ")
ax1.grid()
ax1.set_xlabel("Time $n$")
ax1.set_ylabel("$\delta[n]$")

# Unit Step
Step = np.zeros(len(T))
Step[5:] = 1
fig2 = plt.figure()
ax2 = fig2.add_subplot(1, 1, 1)
ax2.stem(T, Step, use_line_collection=True, basefmt = " ")
ax2.grid()
ax2.set_xlabel("Time $n$")
ax2.set_ylabel("$u_0[n]$")

# Ramp
Ramp = T * Step
fig3 = plt.figure()
ax3 = fig3.add_subplot(1, 1, 1)
ax3.stem(T, Ramp, use_line_collection=True, basefmt = " ")
ax3.grid()
ax3.set_xlabel("Time $n$")
ax3.set_ylabel("$r[n]$")

# Exponential
alpha = 0.75
Exponential = (alpha ** T) * Step
fig4 = plt.figure()
ax4 = fig4.add_subplot(1, 1, 1)
ax4.stem(T, Exponential, use_line_collection=True, basefmt = " ")
ax4.grid()
ax4.set_xlabel("Time $n$")
ax4.set_ylabel("$a[n]$")
