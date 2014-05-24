# -*- coding: utf-8 -*-
import math
import wave
import numpy as np
import pylab as pl

#打开wav文件
#open返回一个的是一个Wave_read类的实例，通过调用它的方法读取WAV文件的格式和数据
f = wave.open(r"./dong1.wav","rb")

# 读取格式信息
# (nchannels, sampwidth, framerate, nframes, comptype, compname)
params = f.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]

print params

# 读取波形数据
str_data = f.readframes(nframes)
f.close()

#将波形数据转换为数组
wave_data = np.fromstring(str_data, dtype=np.short)
#wave_data.shape = -1, 2
#wave_data = wave_data.T
time = np.arange(0, nframes) * (1.0 / framerate)

freqs = np.linspace(0, framerate/2.0, nframes/2.0 + 1)
xf = np.fft.rfft(wave_data)/sampwidth2
xfp = np.abs(xf)

# 绘制波形
pl.subplot(211) 
pl.plot(time, wave_data)
pl.xlabel("time (seconds)")

pl.subplot(212)
print len(freqs), len(xfp)
pl.plot(freqs, xfp)
pl.show()
