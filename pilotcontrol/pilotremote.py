import socket
import json
import tkinter as tk
import pathlib
import time

path = pathlib.Path(__file__).resolve().parent

conffile = open(f"{path}/config.json","r")
config = json.loads(conffile.read())
#change in config.json
HOST = config["HOST"]
PORT = config["IP"]

def auto():
    send_message("auto")
def standby():
    send_message("standby")
def wind():
    send_message("wind")
def minusone():
    send_message("minus1")
def plusone():
    send_message("plus1")
def minusten():
    send_message("minus10")
def plusten():
    send_message("plus10")
def minushundred():
    send_message("minus100")
def plushundred():
    send_message("plus100")

def init()->None:
    global sock
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Client online...")
    
def connect():
    print("Connecting...")
    try:
        sock.connect((HOST,PORT))
        print("Client connected\n-----------")
    except ConnectionRefusedError:
        time.sleep(5)
        connect()
    

def start_window()->None:
    root = tk.Tk()
    root.title("Pilot Control")
    root.configure(bg="#444444")
    font = ("Helvetica",14,"bold")
    buttons = [
    tk.Button(master=root,command=minusone, text="-1", fg="#FF0000",bg="#000000",height=5, width=10,font=font),
    tk.Button(master=root,command=plusone, text="+1", fg="#00FF00",bg="#000000",height=5, width=10,font=font),
    tk.Button(master=root,command=minusten, text="-10", fg="#FF0000",bg="#000000",height=5, width=10,font=font),
    tk.Button(master=root,command=plusten, text="+10", fg="#00FF00",bg="#000000",height=5, width=10,font=font),
    tk.Button(master=root,command=minushundred, text="-100", fg="#FF0000",bg="#000000",height=5, width=10,font=font),
    tk.Button(master=root,command=plushundred, text="+100", fg="#00FF00",bg="#000000",height=5, width=10,font=font),
    tk.Button(master=root, command=standby, text = "Standby", bg="#FF0000",height=5, width=10,font=font),
    tk.Button(master=root, command=auto,text="Auto", bg="#FF0000",height=5, width=10,font=font),
    tk.Button(master=root, command=wind,text="Wind", bg="#FF0000",height=5, width=10,font=font),
    tk.Button(master=root,text="Ich mach\n nix :(", bg="#FF0000",height=5, width=10, font=font)
    ]

    for button in buttons:
        ind = buttons.index(button) + 1
        if ind % 2 != 0:
            col = 0
            row = int((ind+1)/2)
        else:
            col = 1
            row = int(ind/2)

        button.grid(row=row, column=col, padx=10, pady=10)


    root.mainloop()

def send_message(message:str)->None:
    try:
        bmsg = message.encode("ascii")
        sock.sendall(bmsg)
    except:
        print("Client not connected")
        sock.close()
        init()
        connect()


def close()->None:
    sock.close()

if __name__ == "__main__":
    init()
    connect()
    time.sleep(1.5)
    start_window()