import socket
from threading import Thread
import time

sock = socket.socket()
HOST = '127.0.0.1'
PORT = 9999
sock.bind((HOST, PORT))
sock.listen()
clients = []
nicknames = []


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} is out'.encode('utf-8'))
            nicknames.remove(nickname)
            break


def receive():
    while True:
        conn, addr = sock.accept()
        print(f'Connected with {str(addr)}')
        conn.send('Nickname'.encode('utf-8'))
        nick = conn.recv(1024).decode('utf-8')
        nicknames.append(nick)
        clients.append(conn)
        print(f'User {nick} is in.')
        broadcast(f'{nick} is in'.encode('utf-8'))
        conn.send('You are in'.encode('utf-8'))
        thread = Thread(target=handle, args=(conn, ))
        thread.start()


receive()
