import socket
import threading
import hashlib
import base64
import json

HOST = '127.0.0.1'
PORT = 8000

# In-memory data store
items = [
    {"id": 1, "name": "Item 1", "description": "First item"},
    {"id": 2, "name": "Item 2", "description": "Second item"}
]
next_id = 3

# Connected WebSocket clients
clients = []


def websocket_handshake(key):
    """Perform WebSocket handshake"""
    magic = '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'
    accept_key = base64.b64encode(hashlib.sha1((key + magic).encode()).digest()).decode()
    
    response = "HTTP/1.1 101 Switching Protocols\r\n"
    response += "Upgrade: websocket\r\n"
    response += "Connection: Upgrade\r\n"
    response += f"Sec-WebSocket-Accept: {accept_key}\r\n\r\n"
    
    return response


def decode_frame(data):
    """Decode WebSocket frame - simplified version"""
    if len(data) < 6:
        return None
    
    # Get payload length from second byte
    payload_len = data[1] & 0x7F
    
    # Get masking key (4 bytes after length)
    mask_start = 2
    if payload_len == 126:
        mask_start = 4
    elif payload_len == 127:
        mask_start = 10
    
    masking_key = data[mask_start:mask_start+4]
    payload_start = mask_start + 4
    
    # Unmask the payload
    payload = bytearray()
    for i in range(payload_len):
        payload.append(data[payload_start + i] ^ masking_key[i % 4])
    
    return payload.decode('utf-8')


def encode_frame(message):
    """Encode message into WebSocket frame"""
    msg_bytes = message.encode('utf-8')
    frame = bytearray()
    
    # First byte: FIN=1, opcode=1 (text)
    frame.append(0x81)
    
    # Payload length
    length = len(msg_bytes)
    if length <= 125:
        frame.append(length)
    elif length <= 65535:
        frame.append(126)
        frame.append((length >> 8) & 0xFF)
        frame.append(length & 0xFF)
    else:
        frame.append(127)
        for i in range(7, -1, -1):
            frame.append((length >> (8 * i)) & 0xFF)
    
    frame.extend(msg_bytes)
    return bytes(frame)


def broadcast(message, exclude=None):
    """Send message to all clients"""
    for client in clients[:]:
        if client != exclude:
            try:
                client.sendall(encode_frame(message))
            except:
                clients.remove(client)


def handle_message(client, message):
    """Handle incoming WebSocket message"""
    global next_id
    
    data = json.loads(message)
    action = data.get('action')
    
    if action == 'GET_ITEMS':
        response = {'action': 'ITEMS_LIST', 'data': items}
        client.sendall(encode_frame(json.dumps(response)))
    
    elif action == 'CREATE_ITEM':
        new_item = {
            "id": next_id,
            "name": data.get("name", ""),
            "description": data.get("description", "")
        }
        next_id += 1
        items.append(new_item)
        
        response = {'action': 'ITEM_CREATED', 'data': new_item}
        broadcast(json.dumps(response))
    
    elif action == 'UPDATE_ITEM':
        item_id = data.get('id')
        for item in items:
            if item["id"] == item_id:
                item["name"] = data.get("name", item["name"])
                item["description"] = data.get("description", item["description"])
                
                response = {'action': 'ITEM_UPDATED', 'data': item}
                broadcast(json.dumps(response))
                return
    
    elif action == 'DELETE_ITEM':
        item_id = data.get('id')
        for i, item in enumerate(items):
            if item["id"] == item_id:
                items.pop(i)
                
                response = {'action': 'ITEM_DELETED', 'data': {'id': item_id}}
                broadcast(json.dumps(response))
                return


def handle_websocket(client, addr):
    """Handle WebSocket client"""
    clients.append(client)
    print(f"Client connected: {addr}")
    
    try:
        while True:
            data = client.recv(4096)
            if not data:
                break
            
            message = decode_frame(data)
            if message:
                handle_message(client, message)
    
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if client in clients:
            clients.remove(client)
        client.close()
        print(f"Client disconnected: {addr}")


def handle_client(client, addr):
    """Handle initial connection"""
    try:
        request = client.recv(4096).decode('utf-8')
        lines = request.split('\r\n')
        
        # Check for WebSocket upgrade
        if 'Upgrade: websocket' in request:
            # Extract WebSocket key
            key = ''
            for line in lines:
                if 'Sec-WebSocket-Key:' in line:
                    key = line.split(':')[1].strip()
                    break
            
            # Send handshake
            client.sendall(websocket_handshake(key).encode('utf-8'))
            
            # Handle as WebSocket
            handle_websocket(client, addr)
        
        # Serve HTML file
        elif 'GET / ' in lines[0]:
            with open('index.html', 'r') as f:
                content = f.read()
            
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type: text/html\r\n"
            response += f"Content-Length: {len(content)}\r\n\r\n"
            response += content
            
            client.sendall(response.encode('utf-8'))
            client.close()
    
    except Exception as e:
        print(f"Error: {e}")
        client.close()


def start_server():
    """Start the server"""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(5)
    
    print(f"WebSocket server running at http://{HOST}:{PORT}/")
    print("Press Ctrl+C to stop")
    
    try:
        while True:
            client, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(client, addr))
            thread.daemon = True
            thread.start()
    
    except KeyboardInterrupt:
        print("\nServer stopped")
    finally:
        server.close()

start_server()