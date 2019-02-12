import socket

BIND_ALL = "0.0.0.0"
TCP_IP = BIND_ALL
TCP_PORT = 5005

print("Server binding to TCP IP: " + TCP_IP)
print("Server listening on TCP port: " + str(TCP_PORT))
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((TCP_IP, TCP_PORT))

BUFFER_SIZE = 1024
REQUEST_QUEUE_LENGTH = 1
sock.listen(REQUEST_QUEUE_LENGTH)
while True:
  print("Server accepting connections...")
  conn, addr = sock.accept()
  print("Server received connection from: " + addr[0])
  if conn:
    data = conn.recv(BUFFER_SIZE)
    if data:
      print("Server received message: \"" + data + "\"")
      # Echo the data back to the sender
      print("Server responding with: \"" + data + "\"")
      conn.send(data)
    conn.close()

