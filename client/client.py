import socket


def main():
    HOST, PORT = "localhost", 3000
    print(f'Connecting to {HOST}:{PORT}')

    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((HOST, PORT))
            msg = input('> ')
            sock.send(msg.encode())
            res = sock.recv(1024)
            print(res.decode())
        finally:
            sock.close()


if __name__ == "__main__":
    main()