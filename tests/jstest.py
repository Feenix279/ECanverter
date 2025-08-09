import threading
import src.jsmgr as jsmgr
import time

jsmgr.init("./js/src/jty.js")
jsmgr.sendtojs('{"canId":486494067,"prio":7,"src":115,"pgn":65359,"dst":255,"fields":{"manufacturerCode":"Raymarine","industryCode":"Marine Industry","sid":0,"headingMagnetic":4.188},"description":"Seatalk: Pilot Heading","id":"seatalkPilotHeading","timestamp":"2025-08-08T16:13:11.580Z"}')

time.sleep(2)

for i in jsmgr.empty_queue():
    print("Ergebnis: " + str(i))

#18eaffff 14 f0 01
#{
#  "PGN": 127245,
#  "ControlStatus": "Auto",
#  "Instance": 0
#}
