import socket

#change in config.ini
HOST = ''
PORT = 8888

def init()->None:
    global conn
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen(1)
    print("Server online...")
    conn, addr = sock.accept()
    print("Client connected\n-----------")

def send_message(message)->None:
    try:
        conn.sendall(message)
    except ConnectionAbortedError:
        print("Client not connected")
        close()


def close()->None:
    conn.close()