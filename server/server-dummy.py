from collections.abc import Callable, Iterable, Mapping
import socket
import socketserver
import threading
from typing import Any

request_queue_size = 5
  
def handle(conn):
  while True:
    data = conn.recv(1024)
    if not data:
      return
    print(data)
    conn.send('Pong'.encode())
    return

def main():
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  try:
    s.bind(('0.0.0.0', 3000))
    print(f'Binding to {s.getsockname()}')
    s.listen(request_queue_size)
    while True:
      (conn, client) = s.accept()
      print(f'connection from {client}')
      handle(conn)
  finally:
    s.close()

if __name__ == '__main__':
  main()