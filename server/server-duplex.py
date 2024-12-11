import socket
import threading

HOST = 'localhost'
PORT = 3000
request_queue_size = 5


def handle(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            return
        print(data)
        conn.send("Pong".encode())
        return


def send_thread(conn: socket.socket):
    print('Send ping')
    conn.send('ping'.encode())


def receive_thread(conn: socket.socket):
    while True:
        msg = conn.recv(1024)
        if len(msg) == 0:
            return
        print(f'Recv {msg.decode()}')


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    print(f"Binding to {s.getsockname()}")
    s.listen(request_queue_size)
    while True:
        (conn, client) = s.accept()
        print(f"connection from {client}")
        sender = threading.Thread(target=send_thread, args=(conn,))
        receiver = threading.Thread(target=receive_thread, args=(conn,))

        receiver.setDaemon(True)

        sender.start()
        receiver.start()
        sender.join()
        receiver.join()

        conn.close()


if __name__ == "__main__":
    main()