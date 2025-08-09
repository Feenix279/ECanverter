import src.w01mgr as w01mgr
import src.jsmgr as jsmgr
import src.funcs as funcs
import threading

from queue import Queue
import json

decoded_queue = Queue()

pgnfilter =  [130306,129025,130311,128259,129026,128267,127258,129540,128275]

jsmgr.DECODED_QUEUE = decoded_queue
jsmgr.init("./js/src/atj.js")

file = open("./rawdata/jsons.txt","w")
print("check 1")
def catch_data(data):
    chunks = funcs.split_raw(data)
    #turns lists into n2k format
    reslist = funcs.chunkton2k(chunks, decoded_queue, jsmgr.sendtojs)
    #sends every converted datastring to tcp client
    for res in reslist:
        try:
            dictres = json.loads(res)

            if not dictres["pgn"] in []:
                file.write(res)
                print(str(res[:-1]))
        except: pass
w01mgr.open_socket()

w01mgr.return_data = catch_data
threading.Thread(target=w01mgr.read_udp, daemon=True).start()
while True:
    try:
        usrin = input("Senden? : ")
        w01mgr.send_udp(usrin+"\n")
    except KeyboardInterrupt:
        break
print("Ended Program")
w01mgr.sock.close()        
file.close()
