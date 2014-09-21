#!/bin/sh

sudo apt-get update
sudo apt-get install -y python-dev
sudo apt-get install -y libasound2 alsa-utils alsa-oss libasound2-dev 
sudo apt-get install -y jack libjack-dev
sudo pip install rtmidi-python python-rtmidi
sudo pip install mingus