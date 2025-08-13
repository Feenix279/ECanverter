from queue import Queue
import configparser

import src.jsmgr as jsmgr
import src.funcs as funcs

import src.w01mgr as w01mgr
import src.broadcast as opencpn

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

w01mgr.open_socket()
w01mgr.return_data = catch_data
w01mgr.read_udp()

print("Ending Sequence")
jsmgr.end_subprocess()
opencpn.close()        