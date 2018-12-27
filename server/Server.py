import socket
from socket import gethostbyname
from threading import Thread

import GameMessage

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 3000        # Port to listen on (non-privileged ports are > 1023)


class Server:

    def __init__(self):
        print("Init server")
        self.hostName = gethostbyname('0.0.0.0')
        self.running = False
        self.conns = []
        self.addrs = []
        self.socket = None

    def start(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.hostName, PORT))

        t = Thread(target=self.listen)
        t.start()

        GameMessage.load("Hello")
        # self.loop()

    # listen for new connections continuously
    def listen(self):
        while True:
            print("listening")
            self.socket.listen()
            conn, addr = self.socket.accept()
            self.conns.append(conn)
            self.addrs.append(addr)
            print("Found connection:", conn, addr)

    # send data to all active connections
    def send_all_data(self, states):
        for conn in self.conns:
            conn.sendall(states)


if __name__ == "__main__":
    # execute only if run as a script
    c = Server()
    c.start()
