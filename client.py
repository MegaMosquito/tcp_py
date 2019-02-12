import socket

TCP_PORT = 5005
TCP_IP = '127.0.0.1'
MESSAGE = "Hello, World!"

print("Client sending to TCP IP: " + TCP_IP)
print("Client sending to TCP port: " + str(TCP_PORT))
print("Client sending message: \"" + MESSAGE + "\"")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((TCP_IP, TCP_PORT))
sock.send(MESSAGE)

BUFFER_SIZE = 1024
data = sock.recv(BUFFER_SIZE)
print("Client received response: \"" + data + "\"")
sock.close()

print("Client exiting.")
