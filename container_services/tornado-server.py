import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.websocket
import os
import sys
import base64

if len(sys.argv) != 3:
    filename = os.path.basename(__file__)
    print("[USAGE] python3 " + os.path.basename(__file__) + " <SERVICE_NAME> <NON_TEXT_FILE_NAME>")
    exit(0)

SERVICE_NAME = sys.argv[1]
file_name = sys.argv[2]

script_dir = os.path.dirname(__file__)
abs_file_path = os.path.join(script_dir, "files/sample.txt")
non_text_file = os.path.join(script_dir, "files/" + file_name)

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    
    def initialize(self):
        print("serving file:" + abs_file_path)
        with open(abs_file_path, "rb") as imageFile:
            self.str = imageFile.read()

    def open(self):
        print('new connection')
        self.write_message(self.str)

    def on_message(self, message):
        print(message)

    def on_close(self):
        print('connection closed')


class WebSocketFileHandler(tornado.websocket.WebSocketHandler):

    def initialize(self):
        print("serving file:" + non_text_file)
        print("call came")
        with open(non_text_file, "rb") as nfile:
            self.str = base64.b64encode(nfile.read())

    def open(self):
        print('new connection')
        self.write_message(self.str)

    def on_message(self, message):
        print(message)

    def on_close(self):
        print('connection closed')

if __name__ == '__main__':
    application = tornado.web.Application([
    (r'/service' + SERVICE_NAME, WebSocketHandler),
    (r'/file' + SERVICE_NAME, WebSocketFileHandler)
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()