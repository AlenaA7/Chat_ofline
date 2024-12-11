import socketserver


class ChatHandler(socketserver.BaseRequestHandler):
    def handle(self) -> None:
        data = self.request.recv(1024).strip()
        print(f"{self.client_address[0]}: {data}")
        
        answer = input("> ")
        self.request.sendall(answer.encode())
    
    def finish(self) -> None:
        print(f'Connection closed with {self.client_address[0]}')


def main():
    HOST, PORT = "localhost", 3000
    with socketserver.TCPServer((HOST, PORT), ChatHandler) as server:
        print(f'Listen to {HOST}:{PORT}')
        server.serve_forever()


if __name__ == '__main__':
    main()