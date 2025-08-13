import src.w01mgr as mgr
import time

mgr.open_socket()
msgs = []
inp = input("Message: ")
msgs.append(inp)
for msg in msgs:
    if msg:
        bmsg = bytes.fromhex(msg)
        print(f"length: {len(bmsg)}")
        mgr.send_bytes(bmsg)
        print(f"Injected >{msg}<")
        time.sleep(0)