import src.jsmgr as jsmgr
import src.funcs as funcs
import queue
import time

Queue = queue.Queue()

jsmgr.DECODED_QUEUE = Queue
jsmgr.init("./js/src/atj.js")

file = open("./rawdata/Recording3_depth.log","br")
data = file.read()
file.close()

chunks = funcs.split_raw(data)

results = funcs.chunkton2k(chunks, Queue, jsmgr.sendtojs)
time.sleep(10)
results = jsmgr.empty_queue()

print(results)

for res in results:
    print(res)
