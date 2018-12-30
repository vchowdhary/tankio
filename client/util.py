from client.Settings import *


def out_of_bounds(x, y):
    if x > windowWidth or y > windowHeight or y < 0 or x < 0:
        return True
    return False