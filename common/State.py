import json


class State:
    def __init__(self):
        print("State init")
        self.state = {}

    def update(self, conn, data):
        if conn not in self.state:
            self.state[conn] = data
            return
        self.state[conn] = data

    def get(self):
        return json.dumps(self.state).encode()

    def get_msg(self, ip):
        n = {i: self.state[i] for i in self.state if i != ip}
        return json.dumps(n).encode()
