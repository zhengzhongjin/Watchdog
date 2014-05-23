# -*- coding: utf-8 -*-
import math
import wave
import numpy as np
import pylab as pl

# 绘制波形
def plot_wave(array):
	size = len(array)
	time = np.arange(0, size) * (1.0/framerate)

	pl.subplot(111) 
	pl.plot(time, array)
	pl.xlabel("time (seconds)")
	pl.show()


#打开wav文件
#open返回一个的是一个Wave_read类的实例，通过调用它的方法读取WAV文件的格式和数据
f = wave.open(r"./dong1.wav","rb")

# 读取格式信息
# (nchannels, sampwidth, framerate, nframes, comptype, compname)
params = f.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]

# above info must be (1, 2, 8000, ...)

print params

# 读取波形数据
str_data = f.readframes(nframes)
f.close()

#将波形数据转换为数组
wave_data = np.fromstring(str_data, dtype=np.short)

print len(wave_data)

plot_wave(wave_data[10000:15000])

