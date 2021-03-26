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
 

PORTNUM = 8003
rList = [1, 2, 3, 4]

data = [
  -0.99,0,
  -0.98,0,
  -0.97,0,
  -0.851,0,
  -0.85,0,
  -0.849,0,
  -0.76,0,
  -0.75,0,
  -0.749,0,
  -0.747,0,
  -0.746,0.5,
  -0.745,0,
  0.5,0,
  0.73,0,
  0.75,0,
  0.749,0,
  0.741,0,
  0.74,0.5,
  0.749,0.8,
  0.9,0,
  1.0,0,
];
 
# Websocket class to echo received data
class Echo(WebSocket):

    def handleMessage(self):
        yop = json.dumps({"a": data})
        self.sendMessage(yop.encode())
 
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