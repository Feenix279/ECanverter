import src.w01mgr as w01mgr
import time
import json


file = open("./database/pilotcommands.json","r")
commands = json.loads(file.read())
file.close()

def init():
    w01mgr.open_socket()
    time.sleep(1)
    w01mgr.send_bytes(b"hello")

def send_command(command:list)->None:
    print("Sende command...")
    for packet in command:
        print(packet)
        w01mgr.send_bytes(bytes.fromhex(packet))

def auto():
    send_command(commands["auto"])
    print("auto")
def standby():
    send_command(commands["standby"])
    print("standby")
def wind():
    send_command(commands["wind"])
    print("wind")
def minusone():
    send_command(commands["minus1"])
    print("-1")
def minusten():
    send_command(commands["minus10"])
    print("-10")
def plusone():
    send_command(commands["plus1"])
    print("+1")
def plusten():
    send_command(commands["plus10"])
    print("+10")

if __name__ == "__main__":
    funcs = {
        1:auto,
        2:standby,
        3:wind,
        4:plusone,
        5:minusone,
        6:plusten,
        7:minusten
    }
    while True:
        usrin = input("Befehl: ")
        try:
            funcs[int(usrin)]()
        except (ValueError, KeyError):
            print("Keine gültige Zahl")