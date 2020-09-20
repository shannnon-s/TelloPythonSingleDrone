#
# Tello Python3 Control Demo
#
# http://www.ryzerobotics.com/
#
# 1/1/2018

import threading
import socket
import sys
import time


host = ''
port = 9000
locaddr = (host,port)


# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_address = ('192.168.10.1', 8889)

sock.bind(locaddr)

def recv():
    count = 0
    while True:
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\nExit . . .\n')
            break


recvThread = threading.Thread(target=recv)
recvThread.start()









try:
        msg = "command" ;
        # Send data
        msg = msg.encode(encoding="utf-8")
        sent = sock.sendto(msg, tello_address)

        msg1 = "takeoff";
        # Send data
        msg1 = msg1.encode(encoding="utf-8")
        sent = sock.sendto(msg1, tello_address)
        time.sleep(8)
        msg2 = "down 20";
        # Send data
        msg2 = msg2.encode(encoding="utf-8")
        sent = sock.sendto(msg2, tello_address)

        time.sleep(5)
        msg2 = "up 20";
        # Send data
        msg2 = msg2.encode(encoding="utf-8")
        sent = sock.sendto(msg2, tello_address)

        time.sleep(2)
        msg3 = "flip l";
        # Send data
        msg3 = msg3.encode(encoding="utf-8")
        sent = sock.sendto(msg3, tello_address)

        time.sleep(3)
        msg5 = "flip r";
        # Send data
        msg5 = msg5.encode(encoding="utf-8")
        sent = sock.sendto(msg5, tello_address)

        time.sleep(3)
        msg5 = "cw 360";
        # Send data
        msg5 = msg5.encode(encoding= "utf-8")
        sent = sock.sendto(msg5, tello_address)

        msgbat = "battery?";
        # Send data
        msgbat = msgbat.encode(encoding="utf-8")
        sent = sock.sendto(msgbat, tello_address)

except KeyboardInterrupt:
        print ('\n . . .\n')
        sock.close()
