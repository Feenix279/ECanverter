#broadcast.py
#opens udp server and may be used to broadcast
import socket

#change in config.ini
HOST = ""
PORT = 8888

def init()->None:
    global sock
    print("Öffne UDP-Socket...")
    sock = socket.socket(socket.AF_INET, # Internet
                       socket.SOCK_DGRAM) # UDP
    
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)# enable socket for network wide broadcast
  
def send_message(message):
    sock.sendto(message, (HOST, PORT))

def close():
    sock.close()