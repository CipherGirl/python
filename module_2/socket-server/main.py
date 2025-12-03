import socket
import time

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8080

# 1st Param for internet protocol address, 2nd Param for TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 1st Param for  Protocl Level, 2nd Resude the address as soon it closes and used again
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# server_socket.setblocking(False)
# 127.0.0.1 for local 
# Following can be accessed from any device
server_socket.bind((SERVER_HOST, SERVER_PORT))
# Argument will listen to total 5 connections
server_socket.listen(5)

print("Listening on PORT", SERVER_PORT)


# while True:
#     try:
#         client_socket, client_address = server_socket.accept()
#         print(client_socket, client_address)
#     except:
#         time.sleep(1)
#         continue

while True:
    client_socket, client_address = server_socket.accept()
    request = client_socket.recv(1500).decode() # Receiving Limitation of Data in Bytes and decodes it
    print(request)
    headers = request.split('\n')
    first_header_components = headers[0].split()

    http_method = first_header_components[0]
    path = first_header_components[1]

    if http_method == 'GET':
        if path == '/':
            fin = open('/Users/welldev/Code/Personal/python/module_2/socket-server/index.html')
            content = fin.read()
            fin.close()

            # STATUS
            # HEADERS
            # MESSAGE BODY

            response = 'HTTP/1.1 200 OK \n\n' + content
            client_socket.sendall(response.encode())
            client_socket.close()
    else:
        response = 'HTTP/1.1 405 Method Not Allowed\n\n'
        client_socket.sendall(response.encode())
        client_socket.close()
