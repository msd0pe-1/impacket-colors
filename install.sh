#!/bin/bash

echo "[*] Installing depency"
sudo apt install python3-pip
pip3 install --upgrade pip
pip3 install impacket
pip3 install colorama
path=$(find /home/$USER/.local/lib/python3.*/*/impacket/ -iname "logger.py" | sed 's/logger.py//g')
echo
echo "[*] Adding the color plugin to IMPACKET : "$path"colors.py"
cp colors.py $path/colors.py
echo
echo "[*] Creating impacket-colors alias"
sudo cp impacket-colors /bin/
sudo chmod +x /bin/impacket-colors
echo
echo "[+] You can now run :"
echo "	impacket-colors on"
echo "	impacket-colors off"
echo
echo "[?] To take full advantage of the features of impacket-colors :"
echo "	wget https://s3.amazonaws.com/rds.nsrl.nist.gov/RDS/current/RDS_modern.iso (~4Go)"
echo "	unzip the iso"
echo "	unzip NSRLFILE.zip"
echo "	sudo mkdir /usr/share/nsrl; sudo cp NSRLFile.txt /usr/share/nsrl/"
echo
