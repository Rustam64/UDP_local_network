# importing the socket library
import socket
localIP = "127.0.0.1"   # Ip address used for the socket
localPort = 6464        # Port used for socket
bufferSize = 4096       # buffer size

# Setting up the UDP connection
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))

print("UDP server is running...")


# Listen for incoming datagrams
def write_csv():    # Function to write to a CSV file when CSV data is received
    while 1:
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)     # Client addr and data

        message = bytesAddressPair[0]   # Client message
        address = bytesAddressPair[1]   # Client address
        msg = "{}".format(message)      # Decoding the message

        f = open("ServerSideCSV.csv", "a")  # Opening the CSV file to write(append)
        f.write(msg[2:-1])  # Writing data without the byte header
        f.write("\n")       # New line
        f.close()

        # Sending a reply to client
        reply_from_server = "Pong!"
        bytes_to_resend = str.encode(reply_from_server)     # Encoding response
        UDPServerSocket.sendto(bytes_to_resend, address)    # Sending response


def write_json():
    while 1:
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)     # Client addr and data

        message = bytesAddressPair[0]       # Client address
        address = bytesAddressPair[1]       # Client data
        msg = "{}".format(message)      # Decoding the message

        f = open("ServerSideTXT.txt", "a")      # Opening the CSV file to write(append)
        f.write(msg[2:-1])      # Writing data without the byte header
        f.write("\n")       # New line
        f.close()

        # Sending a reply to client
        reply_from_server = "Pong!"
        bytes_to_resend = str.encode(reply_from_server)     # Encoding response
        UDPServerSocket.sendto(bytes_to_resend, address)    # Sending response


def write_img():
    while 1:
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

        message = bytesAddressPair[0]       # Client address
        address = bytesAddressPair[1]       # Client message
        msg = "{}".format(message)      # Decoding the message

        f = open("ServerSideIMG.png", "a")      # Opening the CSV file to write(append)
        f.write(msg[2:-1])      # Writing data without the byte header
        f.close()

        # Sending a reply to client
        reply_from_server = "Pong!"
        bytes_to_resend = str.encode(reply_from_server)        # Encoding response
        UDPServerSocket.sendto(bytes_to_resend, address)       # Sending response


while 1:
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    clientMsg = "{}".format(message)        # Decoding the message
    clientIP = "Client IP :{}".format(address)
    print(clientMsg[2:-1])      # Printing the type of data received.
    if clientMsg[2:-1] == "JSON":
        write_json()
    elif clientMsg[2:-1] == "IMG":
        write_img()
    else:
        write_csv()
    print(clientMsg)
    print(clientIP)