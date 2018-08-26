from scapy.all import rdpcap, wrpcap
from scapy.layers.inet import IP,TCP
#from scapy.all import *
import re
# https://github.com/invernizzi/scapy-http

# rdpcap comes from scapy and loads in our pcap file
packets = rdpcap('test.pcap')

request_str = 'GET / HTTP/1.1\r\nHost: www.baidu.com\r\n\r\n'

# https://stackoverflow.com/questions/27293924/change-tcp-payload-with-nfqueue-scapy
for packet in packets:
    if packet.haslayer(TCP):
        if str(packet[TCP].payload).startswith('GET'):
            packet.show()
            payload_before = len(packet[TCP].payload)
            packet[TCP].remove_payload()
            packet[TCP].add_payload(request_str)
            #packet = packet/request_str
            payload_after = len(packet[TCP].payload)
            payload_dif = payload_after - payload_before
            packet[IP].len = packet[IP].len + payload_dif
            del packet[IP].chksum

            del packet[TCP].chksum

            del packet[IP].len
            packet.show()
            break
 
wrpcap('testout.pcap', packets)