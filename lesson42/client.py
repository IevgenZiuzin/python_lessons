import socket
import time
from threading import Thread

nick = input('Enter nickname: ')

sock = socket.socket()
HOST = '127.0.0.1'
PORT = 9999
sock.connect((HOST, PORT))


def receive():
    while True:
        try:
            message = sock.recv(1024).decode('utf-8')
            if message == 'Nickname':
                sock.send(nick.encode('utf-8'))
            else:
                print(message)
        except:
            print('Error')
            sock.close()
            break


def write():
    while True:
        message = input('>> ')
        sock.send(f'{nick}: {message}'.encode('utf-8'))
        write_th = Thread(target=write)
        write_th.start()


receive_th = Thread(target=receive)
receive_th.start()



write()
