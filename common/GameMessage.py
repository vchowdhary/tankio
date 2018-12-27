import json


class GameMessage:
    def __init__(self, tank, bullets):
        self.tank = tank
        self.bullets = bullets

    def get(self):
        msg = [self.tank.to_json()]

        for b in self.bullets:
            msg.append(b.to_json())

        return json.dumps(msg).encode()

    @staticmethod
    def load(msg):
        print(msg)

