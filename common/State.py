from client.Tank import Tank
from client.Bullet import Bullet


class State:
    def __init__(self):
        print("State init")
        self.state = {}

    def update(self, conn, data):
        if conn not in self.state:
            self.state[conn] = data
            return
        self.state[conn] = data
