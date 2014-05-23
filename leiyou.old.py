# -*- coding: utf-8 -*-
import time 
import thread
from pyaudio import PyAudio, paInt16 
import numpy as np 
from datetime import datetime 
import wave 
import pylab as pl


NUM_SAMPLES = 1024	# pyAudio内部缓存的块的大小
SAMPLING_RATE = 8000	# 取样频率
LEVEL = 1500            # 声音保存的阈值
COUNT_NUM = 20          # NUM_SAMPLES个取样之内出现COUNT_NUM个大于LEVEL的取样则记录声音
SAVE_LENGTH = 8         # 声音记录的最小长度：SAVE_LENGTH * NUM_SAMPLES 个取样

# 开启声音输入
pa = PyAudio() 
stream = pa.open(format=paInt16, channels=1, rate=SAMPLING_RATE, input=True, 
	frames_per_buffer=NUM_SAMPLES)

time = np.arange(0, NUM_SAMPLES) * (1.0/SAMPLING_RATE);

Y_MIN = -35537
Y_MAX =  35537

pl.figure(figsize=(8, 4))

def Loop():
	pl.hold(False)
	while True: 
		# 读入NUM_SAMPLES个取样
		string_audio_data = stream.read(NUM_SAMPLES) 
		# 将读入的数据转换为数组
		audio_data = np.fromstring(string_audio_data, dtype=np.short) 

		print len(time), len(audio_data)

		freqs = np.linspace(0, SAMPLING_RATE/2, NUM_SAMPLES/2 + 1)
		xf = np.fft.rfft(audio_data)/NUM_SAMPLES;
	#	xfp = 20*np.log10(np.clip(np.abs(xf), 1e-20, 1e100))
		xfp = np.abs(xf);

		print len(freqs), len(xfp)

		print "np.max = ", np.max(abs(xfp))

	#	continue 
		pl.subplot(211)
		pl.ylim(Y_MIN, Y_MAX) 
		pl.plot(time, audio_data)
		pl.axis((0, (0.+NUM_SAMPLES)/SAMPLING_RATE, Y_MIN, Y_MAX))
		
		pl.subplot(212)
		pl.ylim(Y_MIN, Y_MAX)
		pl.plot(freqs, xfp)
		pl.draw()

		if (np.max(abs(xfp)) >= 80000):
			time.sleep(1024)
		

print "run..."
thread.start_new_thread(Loop, ())

pl.show()
