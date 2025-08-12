import socket
import time
import threading
# IP und Port of eCAN W01
ECAN_IP = '192.168.4.101'
ECAN_PORT = 8881

def open_socket():
    global sock
    
    # Lokale address
    LOCAL_IP = '0.0.0.0'  # receives on all interfaces
    LOCAL_PORT = ECAN_PORT     # Has to be the same as the ecan one
    
    # create UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   
    sock.bind((LOCAL_IP, LOCAL_PORT))

def close():
    sock.close()

def send_str(message:str):
    sock.sendto(message.encode(),(ECAN_IP,ECAN_PORT))

def send_bytes(message:bytes):
    sock.sendto(message,(ECAN_IP, ECAN_PORT))
    
def return_data(data):
    print(data)

def timeout_thread():
    global dms
    while True:
        try:
            while not dms:
                print("Timeouted")
                send_str("13")
                time.sleep(5)
            dms = False
            time.sleep(10)
        except KeyboardInterrupt:
            break

def read_udp():
    global dms
    #print(f"sending start message on {ECAN_IP}:{ECAN_PORT} ...")
    START_MESSAGE = b'13'
    sock.sendto(START_MESSAGE, (ECAN_IP, ECAN_PORT))
    dms = True
    threading.Thread(target=timeout_thread, daemon=True).start()
    try:
        counter = 0
        while True:
            
            data, addr = sock.recvfrom(2048) # Empfängt max. 1024 Bytes
            #print(len(data))
            if len(data) % 13 == 0:
                dms = True
                counter = 0
                #print(data)
                return_data(data)
            else:
                counter+=1
                print(counter)
            if counter % 5000 == 0:
                sock.sendto(START_MESSAGE, (ECAN_IP, ECAN_PORT))

    except KeyboardInterrupt:
        print("\nBeendet durch Benutzer.")
        return
    finally:
        close()