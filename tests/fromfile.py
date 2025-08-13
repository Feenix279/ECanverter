import src.jsmgr as jsmgr
import src.funcs as funcs
import time


jsmgr.init("./js/src/atj.js")
Queue = jsmgr.DECODED_QUEUE

file = open("./rawdata/Recording3_depth.log","br")
data = file.read()
file.close()

chunks = funcs.split_raw(data)

results = funcs.chunkton2k(chunks, Queue, jsmgr.sendtojs)

results=[]
timer = time.time() + 1
while not timer<time.time():
    while not Queue.empty():
        timer = time.time()+1
        results.append(Queue.get())

    time.sleep(.3)

for res in results:
    print(res[:-1])
