import socket
import time

s = socket.socket()
HOST = '127.0.0.1'
PORT = 9999


def ui(board):
    print("\n"
          f"{board['1']}  | {board['2']} | {board['3']}\n"
          "---+---+--\n"
          f"{board['4']}  | {board['5']} | {board['6']}\n"
          "---+---+--\n"
          f"{board['7']}  | {board['8']} | {board['9']}\n")


def game():
    welcome = s.recv(1024).decode('utf-8')
    print(welcome)

    name = input("Enter name: ")
    s.send(name.encode('utf-8'))

    while True:
        try:
            response = s.recv(1024).decode('utf-8')
            if response == "INPUT":
                while True:
                    try:
                        answer = input("Enter the cell: ")
                        s.send(answer.encode('utf-8'))
                        break
                    except:
                        print('Error INPUT')

            elif response == 'ERROR':
                print(f'Error from server - {response}')
            elif response == 'BOARD':
                print(response)
                board = s.recv(1024).decode('utf-8')
                ui(eval(board))
            elif response == "":
                time.sleep(5)
                break
            else:
                print(response)

        except KeyboardInterrupt:
            print('KeyboardInterrupt')
            time.sleep(1)
            break
        except Exception as e:
            print(e)


def client():
    try:
        s.connect((HOST, PORT))
        print(f"Connected to: {HOST}:{PORT}")
        game()
        s.close()
    except socket.error as e:
        print(f'Client socket error - {e}')


client()
