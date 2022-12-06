# importing required libraries and pandas to view the CSV file before sending.
import socket
import time
import json
import pandas
import pandas as pd

# msgFromClient = "ping"
# bytesToSend = str.encode(msgFromClient)

# Setting the custom IP address and port as well as a buffer limiter
serverAddressPort = ("127.0.0.1", 6464)
bufferSize = 4096

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


# A switch statement to regulate which JSON data to send.
def switch(day):
    f = open("wheel_rotation_ sensor_data.json", "r")   # Opening a file
    type_send = str.encode("JSON")  # Encoding data
    UDPClientSocket.sendto(type_send, serverAddressPort)    # Sending the encoded data.
    if day == 1:    # loop for sending data in case 1
        g = 0
        while g < 10:
            start = time.time()  # Timer used to calculate RTT
            bytesToSend = str.encode(str(f.readline()))  # Encoding the data line by line

            UDPClientSocket.sendto(bytesToSend, serverAddressPort)  # Sending the data line by line
            time.sleep(1)   # Waiting for ACK from server
            msgFromServer = UDPClientSocket.recvfrom(bufferSize)    # Catching server response
            msg = "Message from Server {}".format(msgFromServer[0])    # Viewing server response

            if msg == "Message from Server b'Pong!'":   # If ACK was received:
                print("RTT: ", time.time()-start)  # Timer used to calculate RTT
                print("ACK from server received.")      # Inform the user that the ACK was received.
                g += 1
            else:
                g -= 1

# A switch statement to regulate which JSON data to send.
    elif day == 2:  # loop for sending data in case 1
        g = 0
        for x in range(10):
            f.readline()
        while g < 10:
            start = time.time()  # Timer used to calculate RTT
            bytesToSend = str.encode(str(f.readline()))     # Encoding the data line by line

            UDPClientSocket.sendto(bytesToSend, serverAddressPort)      # Sending the data line by line
            time.sleep(1)       # Waiting for ACK from server
            msgFromServer = UDPClientSocket.recvfrom(bufferSize)        # Catching server response
            msg = "Message from Server {}".format(msgFromServer[0])     # Viewing server response

            if msg == "Message from Server b'Pong!'":       # If ACK was received:
                print("RTT: ", time.time() - start)         # Timer used to calculate RTT
                print("ACK from server received.")          # Inform the user that the ACK was received.
                g += 1
            else:
                g -= 1
    else:
        g = 0
        for x in range(20):
            f.readline()
        while g < 10:
            start = time.time()  # Timer used to calculate RTT
            bytesToSend = str.encode(str(f.readline()))         # Encoding the data line by line

            UDPClientSocket.sendto(bytesToSend, serverAddressPort)      # Sending the data line by line
            time.sleep(1)       # Waiting for ACK from server
            msgFromServer = UDPClientSocket.recvfrom(bufferSize)        # Catching server response
            msg = "Message from Server {}".format(msgFromServer[0])     # Viewing server response

            if msg == "Message from Server b'Pong!'":       # If ACK was received:
                print("RTT: ", time.time() - start)         # Timer used to calculate RTT
                print("ACK from server received.")          # Inform the user that the ACK was received.
                g += 1
            else:
                g -= 1


def switch1(user_choice):
    if user_choice == "IMG":
        g = 0
        type_send = str.encode("IMG")   # Encoding the data type
        UDPClientSocket.sendto(type_send, serverAddressPort)    # Sending the data type
        time.sleep(1)   # Waiting for the server

        file = open('tux.png', 'rb')
        image = file.read(1024)
        while image:
            start = time.time()
            bytesToSend = str.encode(str(image))                   # Encoding the data line by line
            UDPClientSocket.sendto(bytesToSend, serverAddressPort)      # Sending the data line by line
            time.sleep(1)   # Timer used to calculate RTT
            msgFromServer = UDPClientSocket.recvfrom(bufferSize)        # Catching server response
            msg = "Message from Server {}".format(msgFromServer[0])     # Viewing server response

            if msg == "Message from Server b'Pong!'":   # If ACK was received:
                print("RTT: ", time.time() - start)     # Timer used to calculate RTT
                print("ACK from server received.")      # Inform the user that the ACK was received.
                g += 1
            else:
                g -= 1
            image = file.read(1024)
        file.close()

    elif user_choice == "JSON":
        D = input("Choose the day:")    # Request user choice
        switch(D)       # Call the switch function
    else:
        type_send = str.encode("CSV")   # Encoding the data line by line
        UDPClientSocket.sendto(type_send, serverAddressPort)    # Sending the data line by line
        time.sleep(1)   # Timer used to calculate RTT
        print("\n\n")
        df = pd.read_csv('pokemon.csv')     # Reading the CSV file using pandas
        print(df.head(5))       # Viewing the first 5 Rows with headers
        print("\n\n")
        g = 0
        f = open("Pokemon.csv", "r")    # Opening the CSV file
        while g < 10:
            start = time.time()     # Timer used to calculate RTT
            bytesToSend = str.encode(str(f.readline()))     # Encoding the data line by line

            UDPClientSocket.sendto(bytesToSend, serverAddressPort)      # Sending the data line by line
            time.sleep(1)   # Waiting for ACK from server
            msgFromServer = UDPClientSocket.recvfrom(bufferSize)       # Catching server response
            msg = "Message from Server {}".format(msgFromServer[0])    # Viewing server response

            if msg == "Message from Server b'Pong!'":   # If ACK was received:
                print("RTT: ", time.time() - start)     # Timer used to calculate RTT
                print("ACK from server received.")      # Inform the user that the ACK was received.
                g += 1
            else:
                g -= 1


# Request user choice
choice = input("""\n-IMG -> Image\n-CSV -> Csv File\n-JSON -> Json File \nWhat would you like to send?:""")
switch1(choice) # Start switch function

UDPClientSocket.close()     # Close the connection



