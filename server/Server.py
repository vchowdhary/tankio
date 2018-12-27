import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 3000        # Port to listen on (non-privileged ports are > 1023)


class Server:

    def __init__(self):
        print("Init server")
        self.running = False

    def start(self):
        self.loop()

    def loop(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            self.running = True
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while self.running:
                    data = conn.recv(1024)
                    if not data:
                        break
                    conn.sendall(data)


