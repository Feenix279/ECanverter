import src.w01mgr as w01mgr
import src.jsmgr as jsmgr
import time
import json

w01mgr.open_socket()

jsmgr.init("./js/src/jty.js")

jsonobj = {"canId":502267763,
           "prio":7,
           "src":115,
           "pgn":126720,
           "dst":255,
           "fields":{"manufacturerCode":"Raymarine",
                     "industryCode":"Marine Industry",
                     "proprietaryId":"Seatalk 1 Encoded",
                     "command":"Seatalk1",
                     "seatalk1Command":"Keystroke",
                     "unknown1":6182,
                     "pilotMode":"auto",
                     "subMode":0,
                     "pilotModeData":0,
                     "unknown2":"00 05 05 00 d6 af 66 00 22 00"},
            "description":"Seatalk1: Pilot Mode",
            "id":"seatalk1PilotMode"}
jsonstring = json.dumps(jsonobj)
print(jsonstring)
jsmgr.sendtojs(jsonstring)
time.sleep(1)
ress = jsmgr.empty_queue()

for res in ress:
    singles = res.split(",")
    print(singles)
    print(singles)
    for single in singles:
        fullhex = "88" + single.replace(" ", "").replace("\n","") + "\n"
        print(len(fullhex))
        bhex = bytes.fromhex(fullhex)
        print(bhex)
        w01mgr.send_bytes(bhex)
        print("sent message")
        time.sleep(.2)
