import http.server
import json
from pathlib import Path

PORT = 8000

data_store = {
    "items": [
        {"id": 1, "name": "Item 1", "description": "First item"},
        {"id": 2, "name": "Item 2", "description": "Second item"}
    ]
}
next_id = 3


class CustomHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.serve_html('index.html')
        elif self.path == '/api/items':
            self.send_json_response(200, data_store["items"])
        else:
            super().do_GET()
    
    def do_POST(self):
        if self.path == '/api/items':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            item_data = json.loads(post_data.decode('utf-8'))
            
            global next_id
            new_item = {
                "id": next_id,
                "name": item_data.get("name", ""),
                "description": item_data.get("description", "")
            }
            next_id += 1
            data_store["items"].append(new_item)
            
            self.send_json_response(201, new_item)
        else:
            self.send_json_response(404, {"error": "Not found"})
    
    def do_PUT(self):
        if self.path.startswith('/api/items/'):
            item_id = int(self.path.split('/')[-1])
            content_length = int(self.headers['Content-Length'])
            put_data = self.rfile.read(content_length)
            item_data = json.loads(put_data.decode('utf-8'))
            
            for item in data_store["items"]:
                if item["id"] == item_id:
                    item["name"] = item_data.get("name", item["name"])
                    item["description"] = item_data.get("description", item["description"])
                    self.send_json_response(200, item)
                    return
            
            self.send_json_response(404, {"error": "Item not found"})
        else:
            self.send_json_response(404, {"error": "Not found"})
    
    def do_DELETE(self):
        if self.path.startswith('/api/items/'):
            item_id = int(self.path.split('/')[-1])
            
            for i, item in enumerate(data_store["items"]):
                if item["id"] == item_id:
                    deleted_item = data_store["items"].pop(i)
                    self.send_json_response(200, {"message": "Deleted", "item": deleted_item})
                    return
            
            self.send_json_response(404, {"error": "Item not found"})
        else:
            self.send_json_response(404, {"error": "Not found"})
    
    def send_json_response(self, status_code, data):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))
    
    def serve_html(self, filename):
        try:
            with open(filename, 'rb') as f:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(f.read())
        except FileNotFoundError:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'File not found')


server_address = ("", 8000)   
server = http.server.HTTPServer(server_address, CustomHTTPRequestHandler)

print("Server running on http://localhost:8000")
server.serve_forever()

with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
    print(f"Server running at http://localhost:{PORT}/")
    print("Press Ctrl+C to stop the server")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped")
        httpd.shutdown()