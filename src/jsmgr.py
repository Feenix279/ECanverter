import subprocess
from queue import Queue
import threading



def init(filename:str)->None:
    global proc
    global DECODED_QUEUE
    
    DECODED_QUEUE = Queue()

    # Starting Node-JS as Subprocess
    proc = subprocess.Popen(
        ['node', filename],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        #stderr=subprocess.PIPE,
        text=True,                   # text instead of bytes
        bufsize=1                    # line buffer
    )
    threading.Thread(target=reader_thread, daemon=True).start()
    
def sendtojs(line:str)->None:
    proc.stdin.write(line.strip()+ '\n')
    proc.stdin.flush()

def reader_thread()->None:
    #global proc
    while True:
        line = proc.stdout.readline()
        if not line:
            break
        try:
            if line.replace("\n",""):
                DECODED_QUEUE.put(line)
        except Exception as e:
            print("JS false string return:", line.strip(), e)

def empty_queue()->list:
    returnlist = []
    while not DECODED_QUEUE.empty():
        returnlist.append(DECODED_QUEUE.get())
    
    return returnlist

def end_subprocess()->None:
    #print("Ending subprocess")
    proc.stdin.close()
    proc.terminate()
    proc.wait()