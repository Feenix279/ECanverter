import threading
import src.jsmgr as jsmgr
import time

jsmgr.init("./js/src/jty.js")
jsmgr.sendtojs('{"canId":234162979,"prio":3,"src":35,"pgn":128267,"dst":255,"fields":{"depth":1.93,"offset":0.499},"description":"Water Depth","id":"waterDepth","timestamp":"2025-08-12T16:11:28.306Z"}')
time.sleep(2)

for i in jsmgr.empty_queue():
    print("Ergebnis: " + str(i))

#18eaffff 14 f0 01
#{
#  "PGN": 127245,
#  "ControlStatus": "Auto",
#  "Instance": 0
#}
