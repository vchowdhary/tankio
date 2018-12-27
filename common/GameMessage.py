
class GameMessage:
    def __init__(self, tanks, bullets):
        self.tanks = tanks
        self.bullets = bullets

    def get(self):
        msg = []

        for tank in self.tanks:
            msg.append(tank.toJSON())

        for b in self.bullets:
            msg.append(b.toJSON())

        return msg

    @staticmethod
    def load(msg):
        print(msg)

