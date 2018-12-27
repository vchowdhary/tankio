import socket


HOST = '192.168.1.155'  # Standard loopback interface address (localhost)
PORT = 3000        # Port to listen on (non-privileged ports are > 1023)


class Client:
    def __init__(self):
        print("Init server")
        self.running = False

    def connect(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.close()
            s.connect((HOST, PORT))
            s.sendall(b'Hello, world')
            data = s.recv(1024)

        print('Received', repr(data))

        s.close()


if __name__ == "__main__":
    # execute only if run as a script
    c = Client()
    c.connect()
