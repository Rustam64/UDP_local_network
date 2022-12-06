# SERVER
# IMPORTING THE SOCKET LIBRARY REQUIRED FOR THE SENDER/SERVER
import socket

# SETTING THE IP AND PORT USED FOR CREATING A SOCKET
Addr = '224.1.1.1'
port = 6464

# 2-hop restriction in network
ttl = 2

# Setting up the socket for a multicast that allows sending and receiving a broadcast.
sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM,
                     socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP,
                socket.IP_MULTICAST_TTL,
                ttl)
# The code below sends a broadcast to client 1 and client 2
sock.sendto(b"This is a message that was broadcasted!", (Addr, port))
