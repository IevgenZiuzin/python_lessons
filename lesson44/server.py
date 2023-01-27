from auth import check_auth_data, json
import socket
from threading import Thread

db_path = 'users.json'
sock = socket.socket()
HOST = '127.0.0.1'
PORT = 9999
sock.bind((HOST, PORT))
sock.listen()
clients = []


def client_registered(client):
    global clients, logins
    try:
        log_pass_dict = json.loads(client.recv(1024).decode('utf-8'))
        login = next(iter(log_pass_dict))
        password = log_pass_dict[login]
        if check_auth_data(db_path, login, password):
            clients.append(client)
            return True
        else:
            return False
    except:
        print('Error')


def broadcast(message):
    for client in clients:
        client.send(message.encode('utf-8'))


def display(connection, login):
    while True:
        try:
            message = connection.recv(1024).decode("utf - 8")
            print(f'{login}: {message}')
            broadcast(f'{login}: {message}')
        except:
            clients.remove(connection)
            connection.close()
            break



def handle():
    print('Server is running')
    while True:
        conn, address = sock.accept()
        if client_registered(conn):
            conn.send('1'.encode('utf-8'))
            login = conn.recv(1024).decode('utf-8')
            print(f'{login} is in')
            Thread(target=display, args=(conn, login,)).start()
        else:
            conn.send('Wrong auth data'.encode('utf-8'))
            conn.close()


handle()

