import src.w01mgr as mgr
import time

mgr.open_socket()
msgs = ["88230DF118000FFFFFFFFFFFFF","88230DF1180102FF5C3DFFFFFF","880df50b23 ff c1 00 00 00 f3 01 ff","8818eaffff 14 F0 01 FF FF FF FF FF"]
inp = input("Message: ")
msgs.append(inp)
for msg in msgs:
    if msg:
        bmsg = bytes.fromhex(msg)
        print(f"length: {len(bmsg)}")
        mgr.send_bytes(bmsg)
        print(f"Injected >{msg}<")
        time.sleep(0.1)