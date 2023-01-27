import socket
import time

s = socket.socket()
HOST = '127.0.0.1'
PORT = 9999
board = {
    '1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' '
}

player_one = 'X'
player_two = 'O'

player_conn = []
player_addr = []
player_name = []

turn = ''


def ui():
    global board
    print("\n"
          f"{board['1']} | {board['2']} | {board['3']}\n"
          "---+---+--\n"
          f"{board['4']} | {board['5']} | {board['6']}\n"
          "---+---+--\n"
          f"{board['7']} | {board['8']} | {board['9']}\n")


def is_winner():
    global board
    return ((board['1'] == board['2'] == board['3'] != ' ') or
            (board['4'] == board['5'] == board['6'] != ' ') or
            (board['7'] == board['8'] == board['9'] != ' ') or
            (board['1'] == board['4'] == board['7'] != ' ') or
            (board['2'] == board['5'] == board['8'] != ' ') or
            (board['3'] == board['6'] == board['9'] != ' ') or
            (board['3'] == board['5'] == board['7'] != ' ') or
            (board['1'] == board['5'] == board['9'] != ' '))


def validate_input(answer, conn):
    if answer not in board:
        print("\nWrong cell! Enter again")
        conn.send("ERROR".encode('utf-8'))
        return False
    elif board[answer] != " ":
        print("Already entered! Enter again")
        conn.send("ERROR".encode('utf-8'))
        return False
    return True


def get_input(current_player):
    global turn
    if current_player == player_one:
        mess = "Player One Turn"
        turn = player_one
        conn = player_conn[0]
    else:
        mess = "Player Two Turn"
        turn = player_two
        conn = player_conn[1]
    ui()
    print(mess)
    broadcast(mess.encode('utf-8'))
    while True:
        try:
            broadcast("BOARD".encode('utf-8'))
            broadcast(str(board).encode('utf-8'))
            conn.send("INPUT".encode('utf-8'))
            data = conn.recv(1024)
            conn.settimeout(20)
            answer = data.decode('utf-8')
            if validate_input(answer, conn):
                board[answer] = current_player
                break
        except:
            conn.send('ERROR'.encode('utf-8'))
            print("Error occurred! Try again ")


def start_game():
    try:
        res = ''
        i = 0
        while not res and i < 9:
            if i % 2 == 0:
                get_input(player_one)
            else:
                get_input(player_two)
            res = is_winner()
            i += 1
        mess = 'Unknown!'
        if res and turn == player_one:
            mess = f'Player one - {player_name[0]} is winner'
        elif res and turn == player_two:
            mess = f'Player one - {player_name[1]} is winner'
        else:
            mess = 'Draw'

        broadcast(mess.encode('utf-8'))
        time.sleep(1)
        for conn in player_conn:
            conn.close()
    except Exception as e:
        print(f"Start game error - {e}")


def broadcast(message):
    for client in player_conn:
        client.send(message)
    time.sleep(1)


def accept_players():
    try:
        welcome = "Welcome to Tic Tac Toe server"
        for i in range(2):
            conn, addr = s.accept()
            conn.send(welcome.encode('utf-8'))
            name = conn.recv(2048 * 10).decode('utf-8')
            player_conn.append(conn)
            player_addr.append(addr)
            player_name.append(name)

            print(f'Player {i + 1} - {name} [{addr[0]}:{addr[1]}]')

            conn.send(f"Hi {name}, you are player {i + 1}".encode('utf-8'))
        start_game()
        s.close()
    except socket.error as e:
        print(f"Player connection in server error - {e}")
    except Exception as e:
        print(f"Error occurred - {e}")


def main():
    try:
        s.bind((HOST, PORT))
        print(f"Server started {HOST}:{PORT}")
        s.listen(2)
        accept_players()
    except socket.error as e:
        print(f'Server binding error - {e}')


main()
