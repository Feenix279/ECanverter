import src.w01mgr as w01mgr
import src.tcpmgr as tcpmgr
import src.funcs as funcs

tcpmgr.init()

def catch_messages(data):
    chunks = funcs.split_raw(data)
    for chunk in chunks:
        split_dat = chunk[2].hex()
        for i in range(2, len(split_dat)*2, 3):
            split_dat = split_dat[:i] + " " + split_dat[i:]         
        resstr = (chunk[1].hex() + " " + split_dat).strip()
        tcpmgr.send_message((resstr+"\n").encode("ascii"))
        

w01mgr.open_socket()
w01mgr.return_data = catch_messages
w01mgr.read_udp()