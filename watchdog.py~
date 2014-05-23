# -*- coding: utf-8 -*-
import os
import thread
from pyaudio import PyAudio, paInt16 
import numpy as np 
from datetime import datetime 
import wave 
import pylab as pl


NUM_SAMPLES	=	4000	# 内部缓存的块的大小
SAMPLING_RATE	=	8000	# 取样频率
THRESHOLD	=	800	# THRESHOLD value for dy/dx
MAXQUEUE	=	6
MAXDELTA	=	0.08

event = []

def push(v):
	event.append(v)
	if (len(event) > MAXQUEUE):
		del event[0]

def play():
#	os.system("aplay shuia.wav")
#	os.system("aplay b.wav")
	print "***------ shuia ------***"

	
def main():
	# 开启声音输入
	pa = PyAudio() 
	stream = pa.open(format=paInt16, channels=1, rate=SAMPLING_RATE, input=True, 
		frames_per_buffer=NUM_SAMPLES);

	time = np.arange(0, NUM_SAMPLES) * (1.0/SAMPLING_RATE);
	delta = 0
	
	while True: 
		print "delta = ", delta
		delta += NUM_SAMPLES * (1.0/SAMPLING_RATE)
		# 读入NUM_SAMPLES个取样
		string_audio_data = stream.read(NUM_SAMPLES) 
		# 将读入的数据转换为数组
		audio = np.fromstring(string_audio_data, dtype=np.short) 
		
		curr = filter(lambda i : abs(audio[i] - audio[i-1]) > THRESHOLD, range(1, len(time)))
		curr = map(lambda i: delta + time[i], curr)

		blk_sum = 0
		blk_num = 0
		for i in range(1, len(curr)):
			if (curr[i] - curr[i-1] < MAXDELTA):
				blk_sum += curr[i]
				blk_num += 1
			else:
				if (blk_num > 60 and blk_num < 400):
					print "blk::sum, num = ", blk_sum/blk_num, blk_num
					push(blk_sum/blk_num)
				blk_sum = 0
				blk_num = 0

		if (blk_num > 60 and blk_num < 400):
			print "blk::sum, num = ", blk_sum/blk_num, blk_num
			push(blk_sum/blk_num)

		cnt = 0
		for i in range(1, len(event)):
			if (event[i] - event[i-1] < 0.4):
				cnt += 1
			else:
				cnt = 0

			if (cnt >= 2):
				thread.start_new_thread(play, ())
				del event[0:i+1]
				break 
	#	print event

			
if __name__ == '__main__':
	main()
