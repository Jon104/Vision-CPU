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
 
import signal, sys
from SimpleWebSocketServer import WebSocket, SimpleWebSocketServer
 
PORTNUM = 8002
 
# Websocket class to echo received data
class Echo(WebSocket):
 
    def handleMessage(self):
        print("Echoing '%s'" % self.data)
        self.sendMessage(self.data)
 
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