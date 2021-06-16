#!/usr/bin/env python3

import subprocess
import socket
import ipget

#LCD初期化
subprocess.run([‘i2cset’,’-y’,’1′,’0x3c’,’0x00′,’0x02′])
subprocess.run([‘i2cset’,’-y’,’1′,’0x3c’,’0x00′,’0x0c’])
subprocess.run([‘i2cset’,’-y’,’1′,’0x3c’,’0x00′,’0x01′])
subprocess.run([‘i2cset’,’-y’,’1′,’0x3c’,’0x00′,’0xff’])

subprocess.run([‘i2cset’,’-y’,’1′,’0x3c’,’0x00′,’0x80′])

ip = ipget.ipget()
wifi_ip = ip.ipaddr(“wlan0”)
eth_ip = ip.ipaddr(“eth0”)
print(wifi_ip)
print(eth_ip)

for tmp1 in range(len(wifi_ip)):
wifi_ip_part = str(hex(ord(wifi_ip[tmp1])))
#print(myip_part)
subprocess.run([‘i2cset’,’-y’,’1′,’0x3c’,’0x40′,wifi_ip_part])
subprocess.run([‘i2cset’,’-y’,’1′,’0x3c’,’0x40′,’0x20′])

subprocess.run([‘i2cset’,’-y’,’1′,’0x3c’,’0x00′,’0xa0′])

for tmp1 in range(len(eth_ip)):
eth_ip_part = str(hex(ord(eth_ip[tmp1])))
#print(myip_part)
subprocess.run([‘i2cset’,’-y’,’1′,’0x3c’,’0x40′,eth_ip_part])

#テキスト出力
subprocess.run([‘i2cset’,’-y’,’1′,’0x3c’,’0x40′,’0x20′])

#print(myip)