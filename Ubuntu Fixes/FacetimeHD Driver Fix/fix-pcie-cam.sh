#!/bin/bash
echo Installing git...
sudo apt install git
echo git installed.
echo Installing other dependencies
sudo apt install curl xzcat cpio
echo Dependencies installed.
cd /tmp
echo Building drivers...
git clone https://github.com/patjak/facetimehd-firmware.git
cd facetimehd-firmware
make
sudo make install
echo Drivers built.
cd ..
echo Doing some strange kernel magic.
git clone https://github.com/patjak/bcwc_pcie.git
cd bcwc_pcie
make
sudo make install
sudo depmod
sudo modprobe -r bdc_pci
sudo modprobe facetimehd
echo It should be ready, i have no idea.
