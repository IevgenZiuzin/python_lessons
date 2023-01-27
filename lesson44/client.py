from threading import Thread
import socket
import json


HOST = '127.0.0.1'
PORT = 9999


def check():
    global HOST
    global PORT
    while True:
        sock = socket.socket()
        sock.connect((HOST, PORT))
        try:
            login = input('Your login: ')
            password = input('Your password: ')
            sock.send(json.dumps({login: password}).encode('utf-8'))
            message = sock.recv(1024).decode('utf-8')
            if message == '1':
                sock.send(login.encode('utf-8'))
                return sock
            else:
                print(message)
                sock.close()
        except ConnectionAbortedError as e:
            print(e)
        except KeyboardInterrupt:
            break


def receive(sock):
    while True:
        try:
            message = sock.recv(1024).decode('utf-8')
            print(message)
        except:
            sock.close()
            break


def send(sock):
    while True:
        try:
            message = input(': ')
            if message == 'exit()':
                sock.send('is out'.encode('utf-8'))
                sock.close()
                break
            sock.send(message.encode('utf-8'))
        except:
            sock.close()
            break


def run():
    sock = check()
    if isinstance(sock, socket.socket):
        print('You are in')
        Thread(target=receive, args=(sock, )).start()
        Thread(target=send, args=(sock, )).start()


run()
