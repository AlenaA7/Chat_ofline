# SERVER
import socket
import threading
from typing import Dict, Tuple

HOST = '0.0.0.0'
PORT = 9000

clients: Dict[Tuple, socket.socket] = {} # РєР»СЋС‡ - СЌС‚Рѕ ip:port Р° Р·РЅР°С‡РµРЅРёРµ - client (РїРѕС‚РѕРј РёРјСЏ)


def client_loop(client: socket.socket, addr):
    print(f'Connected: {addr}')
    try:
        while True:
            # TODO: РѕР±СЂР°Р±РѕР°С‚С‹РІР°С‚СЊ РёСЃРєР»СЋС‡РµРЅРёСЏ sendall Рё recv
            data = client.recv(1024)
            if len(data) == 0:
                print(f'[WARN] Empty res addr={addr}')
                break
            txt = data.decode().strip()
            if len(txt) = 0:
                print(f'[WARN] Empty string addr={addr}')
                continue
            
            print(f'{addr[0]}:{addr[1]}> {txt}')
            #client.sendall(b'OK')
            
            msg = f'FROM: {addr[0]}:{addr[1]}\r\n{txt}'
            for client_addr in clients:
                if client_addr != addr:
                    clients[client_addr].sendall(msg.encode())
    except Exception as err:
        print(f'[ERROR] {addr}', err)

    print(f'Client disconnected {addr}')
    clients.pop(addr)
    client.close()


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print(f'Listening {HOST}:{PORT}')
    sock.bind((HOST, PORT))
    sock.listen(5)

    while True:
        try:
            print('wait for connection')
            client, addr = sock.accept()
            clients[addr] = client
            ct = threading.Thread(
                target=client_loop,
                args=(client, addr),
            )
            ct.start()
        except Exception as err:
            print('[ERROR] ', err)

if __name__ == '__main__':
    main()