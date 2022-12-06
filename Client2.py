# CLIENT 2
# importing necessary libraries
import socket
import struct

# setting up the IP/PORT and buffer size
serverip = "224.1.1.1"
serverport = 6464
bufferSize = 2048

# Setting up the connection by connecting our code to the socket
ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
ClientSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ClientSocket.bind(('', serverport))  # Binding the socket to the ip and port

# Code below is used to enable UDP multicast
var = struct.pack("4sl", socket.inet_aton(serverip), socket.INADDR_ANY)
ClientSocket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, var)

# Listen for messages from the server/sender and decoding it
msgFromServer = ClientSocket.recvfrom(bufferSize)
msg = "Message from Server {}".format(msgFromServer[0].decode())

# Printing the message received for user view
print(msg)