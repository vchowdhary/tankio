import socket


HOST = '192.168.1.155'  # Standard loopback interface address (localhost)
PORT = 3000        # Port to listen on (non-privileged ports are > 1023)


class Client:
    def __init__(self):
        print("Init server")
        self.running = False
        self.socket = None

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.socket.connect((HOST, PORT))
        self.socket.sendall(b'Hello, world')
        data = self.socket.recv(1024)

        print('Received', repr(data))

        # self.socket.close()

    def send_data(self, data):
        self.socket.sendall(data)
        print("Sent data")

    def close_connection(self):
        self.socket.close()


if __name__ == "__main__":
    # execute only if run as a script
    c = Client()
    c.connect()
