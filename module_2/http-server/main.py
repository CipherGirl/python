# Python’s built-in HTTP framework built on top of the socket module

from http.server import HTTPServer, BaseHTTPRequestHandler
import time

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        self.wfile.write(b"Hello! This is a simple Python HTTP server.")
    
    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        self.wfile.write(bytes('{"time": "}' + date + '"}', "utf-8"))


server_address = ("0.0.0.0", 8080)   
server = HTTPServer(server_address, SimpleHandler)

print("Server running on http://localhost:8080")
server.serve_forever()
