#! /usr/bin/env python3 
from scapy import RandMAC , RandIP , Ether , IP , sendp 

for i in (1000):
    interface = 'eth1'
    randomMac = RandMAC()
    randomIP = RandIP()
    mac = Ether(src=randomMac,dst=randomMac)
    ip = IP(src=randomip , dst=randomIP)
    packet = mac/ip
    sendp(packet)



