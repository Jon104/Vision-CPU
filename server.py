1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
# Websocket demo, from iosoft.blog
 
import signal, sys, struct
from SimpleWebSocketServer import WebSocket, SimpleWebSocketServer
import numpy as np
from array import array
import json
import random
import time

PORTNUM = 8001
rList = [1, 2, 3, 4]

class Data:
    def __init__(self, index):
       self.index=index

    def getData(self):
        chata = [
            -0.99,0,
            -0.98,0,
            -0.97,0,
            -0.95,0.05,
            -0.945,0.03,
            -0.93,-0.7,
            -0.926,-0.77,
            -0.92,-0.8,
            -0.914,-0.77,
            -0.91,-0.7,
            -0.89,0,
            -0.86,0.8,
            -0.83,0,
            -0.80,-0.6,
            -0.77,0,
            -0.74,0.3,
            -0.71,0,
            -0.68,-0.05,
            -0.65,0,
            -0.06,0,
            -0.05,-0.02,
            -0.04,0.13,
            -0.03,-0.27,
            -0.02,0.27,
            -0.01,-0.13,
            0.0,0.02,
            0.01,0,
            0.06,0,
            0.07,0.05,
            0.08,-0.2,
            0.09,0.4,
            0.1,-0.4,
            0.11,0.15,
            0.12,-0.05,
            0.13,0,
            0.5,0,
            0.73,0,
            0.75,0,
            0.749,0,
            0.741,0,
            0.74,0.5,
            0.749,0.8,
            0.9,0,
            1.0,0
        ];

        if (self.index % 2 == 1):
            chata.append(0.4)
        else:
            chata.append(0.8)
            
        chata.append(1.0)
        self.index = self.index + 1
        return chata


index = 1
# Websocket class to echo received data
class Echo(WebSocket):
    def handleMessage(self):
        for x in range(1):
            global index
            data=Data(index)
            yop = json.dumps({"header": "ascan", "a": data.getData()})
            self.sendMessage(yop.encode())
            index = index + 1
 
    def handleConnected(self):
        print("Connected")
 
    def handleClose(self):
        print("Disconnected")

# Handle ctrl-C: close server
def close_server(signal, frame):
    server.close()
    sys.exit()
 
if __name__ == "__main__":
    print("Websocket server on port %s" % PORTNUM)

    server = SimpleWebSocketServer('0.0.0.0', PORTNUM, Echo)
    print(server)
    signal.signal(signal.SIGINT, close_server)
    server.serveforever()