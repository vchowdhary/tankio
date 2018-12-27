import socket
from socket import gethostbyname

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 3000        # Port to listen on (non-privileged ports are > 1023)


class Server:

    def __init__(self):
        print("Init server")
        self.hostName = gethostbyname('0.0.0.0')
        self.running = False

    def start(self):
        self.loop()

    def loop(self):
        print(self.hostName)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.hostName, PORT))
            s.listen()
            self.running = True
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while self.running:
                    data = conn.recv(1024)
                    if not data:
                        continue
                    conn.sendall(data)

            conn.close()


if __name__ == "__main__":
    # execute only if run as a script
    c = Server()
    c.start()
