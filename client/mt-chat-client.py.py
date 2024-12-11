# CLIENT
import sys
import socket
import threading

HOST = '192.168.1.103'
PORT = 9000

def handle_messages(sock: socket.socket):
    # TODO: РµСЃР»Рё СЃРµС‚СЊ РїСЂРѕРїР°Р»Р°, С‚Рѕ РІС‹С…РѕРґРёРј РёР· РїСЂРёР»РѕР¶РµРЅРёСЏ
    while True:
        res = sock.recv(1024)
        if len(res) == 0:
            print('[WARN] Empty res')
            break
        # TODO: СЂР°Р·Р±РёС‚СЊ СЃС‹СЂРѕРµ СЃРѕРѕР±С‰РµРЅРёРµ СЃ СЃРµСЂРІРµСЂР° РЅР° С‡Р°СЃС‚Рё
        print(res.decode())


def handle_input(sock: socket.socket):
    while True:
        msg = input()
        if msg == 'exit':
            print('Exiting')
            break
        sock.sendall(msg.encode())


def main():
    sock = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
    )
    # TODO: СЃРµСЂРІРµСЂ РґРѕР»Р¶РµРЅРѕС‚РїСЂР°РІР»СЏС‚СЊ PING РєР°Р¶РґС‹Рµ 5 СЃРµРєСѓРЅРґ
    #  С‡С‚РѕР±С‹ РєР»РёРµРЅС‚ Р·РЅР°Р», С‡С‚Рѕ СЃРµСЂРІРµСЂ Р¶РёРІ
    # sock.settimeout(10)
    sock.connect((HOST, PORT))

    mt = threading.Thread(target=handle_messages, args=(sock,))
    mt.daemon = True
    it = threading.Thread(target=handle_input, args=(sock,))

    mt.start()
    it.start()

    it.join()
    sock.close()


if __name__ == '__main__':
    main()