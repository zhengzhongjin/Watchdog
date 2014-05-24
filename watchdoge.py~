# -*- coding: utf-8 -*-
import os
import math
import thread
from pyaudio import PyAudio, paInt16 
import numpy as np 
from datetime import datetime 
import wave 
import pylab as pl
import cut


NUM_SAMPLES	=	8000	# 内部缓存的块的大小
SAMPLING_RATE	=	8000	# 取样频率
MAXQUEUE	=	6
MAXDELTA	=	0.08
WINDOWSIZE	=	0
BUFFSIZE	= 	0

event = []

def push(v):
	event.append(v)
	if (len(event) > MAXQUEUE):
		del event[0]

def play():
	print "***------ shuia ------***"

def dot(a, b):
	return reduce(lambda x, i:x + a[i] * b[i].conjugate(), range(0, min(len(a), len(b))))
	
def get_standard():
	global WINDOWSIZE
	std_wave = cut.get_wave(r"./dong1.wav")
	std_wave = cut.get_cut(std_wave)
	WINDOWSIZE = len(std_wave)
	print "WINDOWSIZE", WINDOWSIZE
	return np.fft.fft(std_wave)
	

def main():
	# 开启声音输入
	f_std = get_standard()
	BUFFSIZE = int( NUM_SAMPLES*3.0/2 )
	buff = [0 for i in range(0, BUFFSIZE)]
	
	pa = PyAudio() 
	stream = pa.open(format=paInt16, channels=1, rate=SAMPLING_RATE, input=True, 
		frames_per_buffer=NUM_SAMPLES);

	time = np.arange(0, NUM_SAMPLES) * (1.0/SAMPLING_RATE);
	
	while True: 
		audio = np.fromstring(stream.read(NUM_SAMPLES), dtype=np.short)
		print "get"
		buff[0:BUFFSIZE/3] = buff[BUFFSIZE*2/3:BUFFSIZE]
		buff[BUFFSIZE*2/3:BUFFSIZE] = audio

		max_like = 0.0
		l1 = math.sqrt(dot(f_std, f_std))
		for i in range(0, BUFFSIZE - WINDOWSIZE):
			if i % 1000 == 0:
				f_cur = np.fft.fft(buff[i:i+WINDOWSIZE])
				like = abs(dot(f_cur, f_std))/math.sqrt(dot(f_cur, f_cur))/l1
				max_like = max(max_like, like)
		print max_like

if __name__ == '__main__':
	main()
