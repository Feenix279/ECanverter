import socket
    
PORT = 9999  # Reserve a port for your service every new transfer wants a new port or you must wait.
HOST = "localhost"  # Get local machine name

def init():
    """basic setup for socket"""
    global s
    s = socket.socket()  # Create a socket object
    s.bind((HOST, PORT))  # Bind to the port
    print('TCP Server listening....')
    s.listen(5)  # Now wait for client connection.

def handle_data(data):
    print('TCP Server received', data)

def start_server():
    """Enters a loop that infintely connects to a client and waits for incoming messages. Set function handle_data to the function you want to compute the data with, the only arg given is a bytestring"""
    global conn
    while True:

        print("Connecting to TCP-Client...")
        conn, address = s.accept()  # Establish connection with client.
        print('Got connection from', address)

        while True:
            try:
                data = conn.recv(1024)
                handle_data(data)
                #conn.send(b"Message")

            except Exception as e:
                print(f"")
                break

def send_message(msg:bytes)->None:
    conn.sendall()

def close_server():
    conn.close()

if __name__ == "__main__":
    init()
    start_server()
    close_server()