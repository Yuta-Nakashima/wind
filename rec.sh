#!/bin/sh
while true;do
day=$(date "+%Y_%m_%d")
time=$(date "+%H_%M_%S")
if [ -d /home/pi/audio_data/$day ] ; then
	cd /home/pi/audio_data/$day
else
	cd /home/pi/audio_data
	mkdir $day
	cd $day

fi

rec -c 1 -r 16k $time.wav trim 0 10

if [ $? -ne 0 ]; then
	break
fi

done
sudo reboot

