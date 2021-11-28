# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 00:44:57 2021

@author: yuki1
"""
import math
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Generate the Signal
x = np.array([1, 1, 1, 1, 0, 0, 0, 0])
n = np.arange(0, len(x))

# Plot the Signal
fig1 = plt.figure()
ax1 = fig1.add_subplot(1, 1, 1)
ax1.stem(n, x, use_line_collection=True, basefmt = " ")
ax1.set_xlim(0, len(x))
ax1.set_ylim(np.min(x), np.max(x))
ax1.grid()
ax1.set_xlabel('Time $n$')
ax1.set_ylabel('$x[n]$')


# Discrete Time Fourier Transform (DTFT)
w = np.linspace(-np.pi, np.pi, 1024, endpoint=False)
_, Xejw = signal.freqz(x, 1, w)
fig2 = plt.figure()
ax2 = fig2.add_subplot(1, 1, 1)
maxX = np.max(np.abs(Xejw))
ax2.plot(w, np.abs(Xejw))
ax2.set_xlim(-np.pi, np.pi)
ax2.set_ylim(0, maxX)
ax2.grid()
ax2.set_xlabel('Frequency $\omega$ [rad]')
ax2.set_ylabel('$|X(e^{j\omega})|$')


# Fast Fourier Transform (FFT)
k = n
print('k = \n', k)
X = np.fft.fft(x)
print('X = \n', X)
magX = np.abs(X)
print('magX = \n', magX)
fig3 = plt.figure()
ax3 = fig3.add_subplot(1, 1, 1)
ax3.stem(k, magX, use_line_collection=True, basefmt = " ")
ax3.set_xlim(0, len(k))
ax3.set_ylim(0, maxX)
ax3.grid()
ax3.set_xlabel('Frequency $k$')
ax3.set_ylabel('$|X[k]|$')

# Shift Show
kshift = k - math.floor(len(k) / 2)
Xshift = np.fft.fftshift(X)
magXshift = np.abs(Xshift)
fig4 = plt.figure()
ax4 = fig4.add_subplot(1, 1, 1)
ax4.stem(kshift, magXshift, use_line_collection=True, basefmt = " ")
ax4.set_xlim(-len(k)/2, len(k)/2)
ax4.set_ylim(0, maxX)
ax4.grid()
ax4.set_xlabel('Frequency $k$')
ax4.set_ylabel('$|X[k]|$')
