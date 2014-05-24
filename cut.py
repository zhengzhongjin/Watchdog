# -*- coding: utf-8 -*-
import sys
import math
import wave
import numpy as np
import pylab as pl

# 绘制波形

def plot_graph(array, scale=1.0):
	size = len(array)
	time = np.arange(0, size)*scale

	pl.subplot(111) 
	pl.plot(time, array)
#	pl.xlabel("time (seconds)")
	pl.show()

def get_upperbound(array):
	array = abs(array)
	array = sorted(array, reverse=True)
	return array[len(array)/100]

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

#plot_graph(wave_data)

upbound = get_upperbound(wave_data)
shout = filter(lambda i: abs(wave_data[i]) > upbound, range(0, len(wave_data))) 
shout = map(lambda i: i*1.0 / framerate, shout)

maxdelta = 0.01
s = 0
n = 0
blk = []
for i in range(1, len(shout)):
	if abs(shout[i] - shout[i-1]) > maxdelta:
		if n > 0:
			blk.append(s / n)
		s = shout[i]
		n = 1
	else:
		s += shout[i]
		n += 1
if n > 0:
	blk.append(s / n)
print blk 
if len(blk) != 3:
	print "block != 3"

begin = shout[0]
end = ((blk[2] - blk[0]) / 2.0) * 3.0 + begin

print "begin, end = ", begin, end

cutout = filter(lambda i: i*1.0/framerate >= begin and i*1.0/framerate <= end, range(0, len(wave_data)))
cutout = map(lambda i: wave_data[i], cutout)

plot_graph(cutout, 1.0/framerate)
