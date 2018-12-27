import socket
from client.Game import Game
from threading import Thread
import time
import json

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

    def receive_data(self, max_buffer_size=5120):
        while self.running:
            try:
                data = self.socket.recv(max_buffer_size).decode().rstrip()
                if data is None or len(data) == 0:
                    continue
                print("Received:", data)
                self.game.update_game(json.loads(data))

            except ConnectionResetError:
                print("Connection closed.")
                self.running = False

    def start(self):
        self.start_game()
        self.game.start()

    def start_game(self):
        self.game = Game()
        self.running = True
        t = Thread(target=self.send_data, args=[self.game])
        t.start()
        r = Thread(target=self.receive_data)
        r.start()

    def send_data(self, game):
        while self.running:
            # try:
                # print(game.get_data())
            self.socket.sendall(game.get_data())
                # print("Sent data:", game.get_data())
            time.sleep(0.01)
            # except:
            #     self.running = False
            #     self.close_connection()

    def close_connection(self):
        self.socket.close()


if __name__ == "__main__":
    # execute only if run as a script
    c = Client()
    c.connect()
