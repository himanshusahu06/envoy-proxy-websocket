import websocket
import sys
import os

if len(sys.argv) != 4:
    filename = os.path.basename(__file__)
    print("[USAGE] python3 " + os.path.basename(__file__) + " <host> <port>")
    exit(0)

host = sys.argv[1]
port = sys.argv[2]
service_endpoint = sys.argv[3]
## websocket endpoint
websocket_endpoint = "ws://" + host + ":" + port + service_endpoint

class WSClient():
    def __init__(self):
        websocket.enableTrace(False)
        self.ws = websocket.WebSocketApp(websocket_endpoint,
        on_message = self.on_message,
        on_error = self.on_error,
        on_close = self.on_close)
        self.ws.on_open = self.on_open
        self.ws.run_forever()

    def on_message(self, ws, message):
        print(message)

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws):
        print("connection closed")

    def on_open(self, ws):
        print("connected")

if __name__ == "__main__":
    client = WSClient()