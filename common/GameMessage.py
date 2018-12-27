import json


class GameMessage:
    def __init__(self, tank, bullets):
        self.tank = tank
        self.bullets = bullets

    def get(self):
        msg = [self.tank.toJSON()]

        for b in self.bullets:
            msg.append(b.toJSON())

        return json.dumps(msg)

    @staticmethod
    def load(msg):
        print(msg)

