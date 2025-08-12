import threading
from queue import Queue
import configparser

import src.jsmgr as jsmgr
import src.funcs as funcs

import src.w01mgr as w01mgr
import src.broadcast as opencpn
import src.tcplistener as remote

config = configparser.ConfigParser()
config.read("config.ini")

decoded_queue = Queue()

print("Starting Node-JS...")
jsmgr.DECODED_QUEUE=decoded_queue
jsmgr.init("./js/src/yta.js")

print("Init UDP...")
opencpn.PORT = int(config.get("BROADCAST", "Port"))
opencpn.HOST = config.get("BROADCAST", "IP")
opencpn.init()

#executes when data is received by ecanw01
def catch_data(data):
    #returns lists with header, canid and data
    chunks = funcs.split_raw(data)
    #turns lists into n2k format
    reslist = funcs.chunkton2k(chunks, decoded_queue, jsmgr.sendtojs)
    #sends every converted datastring to tcp client
    for res in reslist:
        opencpn.send_message(res.encode("ascii"))
        print(str(res[:-1]))

#def relay_data(data:bytes)->None:
#    #string = data.decode().replace(" ","").replace("\r","").replace("\n","")
#    #print(string)
#    string = "8818eaffff 14 F0 01 FF FF FF FF FF"
#    #string = string.ljust(26,"F") + "\n"
#    #print(string)
#    bstr = bytes.fromhex(string)
#    print(f"Sending {len(bstr)} bytes of message: >{string}<")
#    w01mgr.send_bytes(bstr)
#
#remote.init()
#remote.handle_data = relay_data
#threading.Thread(target=remote.start_server, daemon=True).start()

w01mgr.ECAN_IP = config.get("UDPW01", "IP")
w01mgr.ECAN_PORT = int(config.get("UDPW01", "Port"))

w01mgr.open_socket()
w01mgr.return_data = catch_data
w01mgr.read_udp()

print("Ending Sequence")
jsmgr.end_subprocess()
opencpn.close()        