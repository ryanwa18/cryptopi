#!/bin/bash
# Simple setup script to configure Raspberry Pi
# for use the adafruit 2.13" eink bonnet.
echo "Install Prerequisites"
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install python3-pip
sudo pip3 install --upgrade setuptools

echo "Clone CryptoPi"
cd ~ 
git clone https://github.com/ryanwa18/cryptopi.git

echo "Install Blinka"
sudo pip3 install --upgrade adafruit-python-shell
wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
sudo python3 raspi-blinka.py

