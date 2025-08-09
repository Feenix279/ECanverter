import queue

#Conversionlib for CANverter
def split_raw(raw_data:bytes)->list:
        chunk_size = 13
        chunks = []

        for i in range(0, len(raw_data), chunk_size):
            chunk = raw_data[i:i+chunk_size]
            header = chunk[:1]
            fid = chunk[1:5]
            data = chunk[-8:]
            spchunk = [header, fid, data]
            chunks.append(spchunk)
        return chunks

def chunkton2k(chunks:list, decoded_queue:queue.Queue, sendtojs=None)->list:
    reslist = []
    #for each data string
    for chunk in chunks:
        #convert to ydgw format
        ydgw = f"{chunk[1].hex()} "
        for i in range(0,8):
            ydgw += chunk[2].hex()[i*2:(i*2)+2] + " "

        #convert ydgw to n2k 

        #send to js
        sendtojs(line=ydgw)
        #puts all entries from receiver thread into list
        while not decoded_queue.empty():
            reslist.append(decoded_queue.get())

    return reslist