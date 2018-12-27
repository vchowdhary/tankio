import socket
from socket import gethostbyname
from threading import Thread
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 3000        # Port to listen on (non-privileged ports are > 1023)


class Server:

    def __init__(self):
        print("Init server")
        self.hostName = gethostbyname('0.0.0.0')
        self.running = False
        self.conn = None
        self.addr = None
        self.socket = None

    def start(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.hostName, PORT))

        t = Thread(target=self.listen)
        t.start()

        # self.loop()

    def listen(self):
        while True:
            print("listening")
            self.socket.listen()
            self.conn, self.addr = self.socket.accept()
            print("Found connection:", self.conn, self.addr)

    def loop(self):
        print(self.hostName)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((self.hostName, PORT))
            s.listen()
            self.running = True
            self.conn, self.addr = s.accept()
            with self.conn:
                print('Connected by', self.addr)
                while self.running:
                    data = self.conn.recv(1024)
                    if not data:
                        continue
                    self.conn.sendall(data)

            self.conn.close()

    def send_all_data(self, states):
        self.conn.sendall(states)


if __name__ == "__main__":
    # execute only if run as a script
    c = Server()
    c.start()
