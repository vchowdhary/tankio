import socket
import sys
from socket import gethostbyname
from threading import Thread
from common.State import State
import json
import time

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

        send = Thread(target=self.send_all_data)
        send.start()
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

            t = Thread(target=self.client_thread, args=[conn, str(addr[0])])
            t.start()

    # send data to all active connections
    def send_all_data(self):
        self.running = True
        while self.running:
            for i in range(len(self.conns)):
                msg = self.state.get_msg(self.addrs[i][0])
                try:
                    self.conns[i].sendall(msg)
                except BrokenPipeError:
                    print("Broken pipe error")
                    i -= 1
                    self.conns.remove(self.conns[i])
                    self.addrs.remove(self.addrs[i])
            time.sleep(1)

    def client_thread(self, connection, ip, max_buffer_size=5120):
        is_active = True

        while is_active:
            try:
                is_active = self.receive_input(connection, ip, max_buffer_size)
            except:
                is_active = False

    def receive_input(self, connection, ip, max_buffer_size):
        client_input = connection.recv(max_buffer_size)
        client_input_size = sys.getsizeof(client_input)

        if client_input_size > max_buffer_size:
            print("The input size is greater than expected {}".format(client_input_size))

        decoded_input = client_input.decode().rstrip()  # decode and strip end of line
        print("Rec:", decoded_input)
        if len(decoded_input) == 0:
            print("bad input")
            return False
        self.process_input(ip, decoded_input)
        return True

    def process_input(self, ip, input_str):
        data = input_str
        self.state.update(ip, json.loads(data))


if __name__ == "__main__":
    # execute only if run as a script
    c = Server()
    c.start()
