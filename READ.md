wnid detection
====

Overview
This is a detection program whether the wind is blowing.

## Description
This program is analyzing wav data and save csv file as the wind blowing is '1' and not blowing is '0'

For example,Something like wind bell sounds whether the wind is blowing. And Raspberry Pi run rec.sh and save wav data ,every 10 seconds. 
Next,Natural frequency of wind bell is examined and the natural freqency is inputed in fft_dir.py.

## Requirement
Python versions <<3.4
librosa



