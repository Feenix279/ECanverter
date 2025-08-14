import src.pilotcontrol as pc
import src.tcplistener as tcplist
import src.w01mgr as w01mgr
import time

PORT = None
HOST = None

def catch_data(data:bytes):
    command = data.decode("ascii")
    print(f"Command received: >{command}<")
    commands = {
        "auto":pc.auto,
        "wind":pc.wind,
        "standby":pc.standby,
        "plus10":pc.plusten,
        "minus10":pc.minusten,
        "plus1":pc.plusone,
        "minus1":pc.minusone,
        "plus100":pc.plushundred,
        "minus100":pc.minushundred
    }
    commands[command]()


def main():
    """Starts TCP Server and redirects correct bytes to w01mgr. Replace the latter if already initiated"""
    pc.w01mgr = w01mgr
    if PORT:
        tcplist.PORT = PORT
    if HOST:
        tcplist.HOST = HOST
    tcplist.init()
    tcplist.handle_data = catch_data
    tcplist.start_server()

if __name__ == "__main__":
    w01mgr.open_socket()
    w01mgr.send_bytes(b"Hello")
    time.sleep(1)
    main()


