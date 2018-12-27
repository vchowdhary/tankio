import socket
import sys
from socket import gethostbyname
from threading import Thread
from common.State import State

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 3000        # Port to listen on (non-privileged ports are > 1023)


class Server:

    def __init__(self):
        print("Init server")
        self.hostName = gethostbyname('0.0.0.0')
        self.running = False
        self.conns = []
        self.addrs = []
        self.state = State()
        self.socket = None

    def start(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.hostName, PORT))

        t = Thread(target=self.listen)
        t.start()

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

            Thread(target=self.client_thread, args=conn.start())

    # send data to all active connections
    def send_all_data(self, states):
        for conn in self.conns:
            conn.sendall(states)

    def client_thread(self, connection, max_buffer_size=5120):
        is_active = True

        while is_active:
            self.receive_input(connection, max_buffer_size)

    def receive_input(self, connection, max_buffer_size):
        client_input = connection.recv(max_buffer_size)
        client_input_size = sys.getsizeof(client_input)

        if client_input_size > max_buffer_size:
            print("The input size is greater than expected {}".format(client_input_size))

        decoded_input = client_input.decode("utf8").rstrip()  # decode and strip end of line
        self.process_input(connection, decoded_input)

    def process_input(self, connection, input_str):
        print("Processing the input received from client")

        data = input_str

        self.state.update(connection, data)


if __name__ == "__main__":
    # execute only if run as a script
    c = Server()
    c.start()
