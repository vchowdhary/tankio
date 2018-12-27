import socket
from client.Game import Game
from threading import Thread
import time

HOST = '192.168.1.155'  # Standard loopback interface address (localhost)
PORT = 3000        # Port to listen on (non-privileged ports are > 1023)


class Client:
    def __init__(self):
        print("Init server")
        self.running = False
        self.socket = None
        self.game = None

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.socket.connect((HOST, PORT))
        # data = self.socket.recv(1024)

        # print('Received', repr(data))

        # self.socket.close()

    def start(self):
        self.start_game()
        self.game.start()

    def start_game(self):
        self.game = Game()
        self.running = True
        t = Thread(target=self.send_data, args=[self.game])
        # t.start()

    def send_data(self, game):
        while self.running:
            try:
                # print(game.get_data())
                self.socket.sendall(game.get_data())
                # print("Sent data")
                time.sleep(1)
            except:
                self.running = False
                self.close_connection()

    def close_connection(self):
        self.socket.close()


if __name__ == "__main__":
    # execute only if run as a script
    c = Client()
    c.connect()
