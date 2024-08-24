from scapy.layers.http import HTTPRequest

def process(packet):
    if packet.haslayer(HTTPRequest):
        print(packet[HTTPRequest].Host.decode()+packet[HTTPRequest].path.decode())

scapy_cap=rdpcap("error_reporting.pcap")
for packet in scapy_cap:
    if packet.getlayer(ICMP):
        print(packet.load)

