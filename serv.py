import http.server
import socketserver
PORT = 8123
DIRECTORY = "./"


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, )

try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port:", PORT)
        httpd.serve_forever()
except:
      #Sometimes that socket may be bound so we will skip ahead one port number
      with socketserver.TCPServer(("", PORT+1), Handler) as httpd:
        print("serving at port:", PORT)
        httpd.serve_forever()
