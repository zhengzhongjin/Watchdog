# -*- coding: utf-8 -*-
import numpy as np
import pylab as pl
import cut

from cut import framerate

def del_low_freq(value, freq):
	for i in range(0, len(value)):
		if abs(freq[i]) < 100:
			value[i] = 0
	return value

def dot(a, b):
	res = 0.0
	for i in range(len(a)/4, len(a)/2):
		res += a[i] * b[i].conjugate()
	return res
	
wave_data = cut.get_wave(r"./dong1.wav")
wave_data = cut.get_cut(wave_data)
cut.plot_graph(wave_data)
v = np.fft.fft(wave_data)
f = np.fft.fftfreq(len(wave_data), 1.0/framerate)
v = del_low_freq(v, f)
print dot(v, v)

print v
pl.subplot(211)
l = len(f)
#pl.ylim(-1.5*10**7, 1.5*10**7)
pl.plot(f[0:l/2], v.real[0:l/2])
pl.subplot(212)
l = len(f)
#pl.ylim(-2.0*10**7, 2.0*10**7)
pl.plot(f[0:l/2], v.imag[0:l/2])
pl.show()
