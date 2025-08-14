import src.w01mgr as w01mgr
import src.jsmgr as jsmgr
import src.funcs as funcs

import json



pgnfilter =  [130306,129025,130311,128259,129026,128267,127258,129540,128275]

jsmgr.init("./js/src/atj.js")
decoded_queue = jsmgr.DECODED_QUEUE

file = open("./rawdata/keystrokes.txt","w")

def catch_data(data):
    chunks = funcs.split_raw(data)
    #turns lists into n2k format
    file.write(str(chunks)+"\n")  #<- also add received bytes to the file, can be helpful for certain tasks
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
w01mgr.read_udp()

print("Ended Program")
w01mgr.sock.close()        
file.close()
