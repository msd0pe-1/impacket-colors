#/bin/bash

echo "Adding the color plugin to IMPACKET : /usr/lib/python3/dist-packages/impacket/examples/colors.py"
cp colors.py /usr/lib/python3/dist-packages/impacket/examples/colors.py

echo "Adding the plugin to :"
echo "[+] WMIEXEC : /usr/share/doc/python3-impacket/examples/wmiexec.py"
sed '32 i from impacket.examples import colors' /usr/share/doc/python3-impacket/examples/wmiexec.py > /tmp/.i; cat /tmp/.i > /usr/share/doc/python3-impacket/examples/wmiexec.py; rm -f /tmp/.i
sed 's/print(self.__outputBuffer)/colors.Colors(data,self.__outputBuffer)/g' /usr/share/doc/python3-impacket/examples/wmiexec.py > /tmp/.i; cat /tmp/.i > /usr/share/doc/python3-impacket/examples/wmiexec.py; rm -f /tmp/.i
echo "[+] DCOMEXEC : /usr/share/doc/python3-impacket/examples/dcomexec.py"
sed '53 i from impacket.examples import colors' /usr/share/doc/python3-impacket/examples/dcomexec.py > /tmp/.i; cat /tmp/.i > /usr/share/doc/python3-impacket/examples/dcomexec.py; rm -f /tmp/.i
sed 's/print(self.__outputBuffer)/colors.Colors(data,self.__outputBuffer)/g' /usr/share/doc/python3-impacket/examples/dcomexec.py > /tmp/.i; cat /tmp/.i > /usr/share/doc/python3-impacket/examples/dcomexec.py; rm -f /tmp/.i
echo "[+] ATEXEC : /usr/share/doc/python3-impacket/examples/atexec.py"
sed '27 i from impacket.examples import colors' /usr/share/doc/python3-impacket/examples/atexec.py > /tmp/.i; cat /tmp/.i > /usr/share/doc/python3-impacket/examples/atexec.py; rm -f /tmp/.i
sed 's/print(data.decode(CODEC))/colors.Colors(self.__command,data)/g' /usr/share/doc/python3-impacket/examples/atexec.py > /tmp/.i; cat /tmp/.i > /usr/share/doc/python3-impacket/examples/atexec.py; rm -f /tmp/.i
