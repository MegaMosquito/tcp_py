import socket
import sys
import threading
import time

TCP_PORT = 5005
BIND_ALL = "0.0.0.0"
LOCALHOST = "127.0.0.1"
BUFFER_SIZE = 1024

DATA = "Hello, World!"

class TcpListenThread(threading.Thread):
  def run(self):
    print("LISTENER started!")
    print("LISTENER binding to TCP IP: " + BIND_ALL)
    print("LISTENER listening on TCP port: " + str(TCP_PORT))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((BIND_ALL, TCP_PORT))
    REQUEST_QUEUE_LENGTH = 1
    sock.listen(REQUEST_QUEUE_LENGTH)
    while True:
      print("LISTENER accepting connections...")
      conn, addr = sock.accept()
      print("LISTENER received connection from: " + addr[0])
      if conn:
        data = conn.recv(BUFFER_SIZE)
        if data:
          print("LISTENER received message: \"" + data + "\"")
        # Echo the data back to the sender
        print("LISTENER responding with: \"" + data + "\"")
        conn.send(data)
      conn.close()

class TcpPublishThread(threading.Thread):
  def run(self):
    data = self.getName()
    print("PUBLISHER started!  data: \"{}\"".format(self.getName()))
    print("PUBLISHER sending to TCP IP: " + LOCALHOST)
    print("PUBLISHER sending to TCP port: " + str(TCP_PORT))
    print("PUBLISHER sending message: \"" + data.encode() + "\"")
    while True:
      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      print("PUBLISHER sending to {}, port {}: \"{}\".".format(LOCALHOST, TCP_PORT, self.getName()))
      sock.connect((LOCALHOST, TCP_PORT))
      sock.send(data.encode())
      resp = sock.recv(BUFFER_SIZE)
      print("PUBLISHER received response: \"" + resp + "\"")
      sock.close()
      time.sleep(10)

if __name__ == '__main__':
  tcp_listener = TcpListenThread()
  tcp_listener.start()
  time.sleep(5)
  tcp_publisher = TcpPublishThread(name = DATA)
  tcp_publisher.start()
  tcp_listener.join()
  tcp_publisher.join()

