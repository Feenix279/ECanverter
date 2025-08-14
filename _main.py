import configparser
import threading

import src.jsmgr as jsmgr
import src.funcs as funcs

import src.w01mgr as w01mgr
import src.broadcast as opencpn

import src.remotemgr as remotemgr

config = configparser.ConfigParser()
config.read("config.ini")

print("Starting Node-JS...")
jsmgr.init("./js/src/yta.js")
decoded_queue = jsmgr.DECODED_QUEUE

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

w01mgr.ECAN_IP = config.get("UDPW01", "IP")
w01mgr.ECAN_PORT = int(config.get("UDPW01", "Port"))

remotemgr.w01mgr = w01mgr
remotemgr.PORT = int(config.get("REMOTETCP","Port"))
remotemgr.HOST = config.get("REMOTETCP", "Host")
threading.Thread(target=remotemgr.main, daemon=True).start()
if config.get("Startup","pilotcontrolui") == "True":
    import src.pilotcontrolui as pcui
    pcui.pc = remotemgr.pc
    threading.Thread(target=pcui.start_window, daemon=True).start()

w01mgr.open_socket()
w01mgr.return_data = catch_data
w01mgr.read_udp()

print("Ending Sequence")
jsmgr.end_subprocess()
opencpn.close()        