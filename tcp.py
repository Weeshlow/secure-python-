#Cookie digging tool 
#Obedience (Hacking Ninja)
#Evil Python - Active State
#Anonymous Libraries

import socket
socket.setdefaulttimeout(2)
s = socket.socket()
s.connect (("hostname for the target", 21))
ans = s.rcv(1024)
print ans

