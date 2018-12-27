import pygame
import math
from Bullet import Bullet

color = (255, 255, 255)
windowWidth = 400
windowHeight = 300


class Tank(pygame.sprite.Sprite):
    # Constructor for tank, pass in position and state
    # state = 0 if not shooting, 1 if shooting
    def __init__(self, x, y, angle, id):
        super().__init__()

        self.image = pygame.Surface([x, y], pygame.SRCALPHA)
        self.image.fill(color)
        self.original = self.image
        self.orientation = angle
        self.x = x
        self.y = y
        self.id = id

        pygame.draw.rect(self.image, color, [x-20, y-30, x, y])

        self.rect = self.image.get_rect()

    def to_json(self):
        tank_json = {
            "id": self.id,
            "center x": self.rect.center[0],
            "center y": self.rect.center[1],
            "rect x": self.rect.x,
            "rect y": self.rect.y,
            "orientation": self.orientation
        }
        return tank_json

    def move(self, pixels):
        pygame.Rect.move_ip(self.rect, pixels*math.cos(self.orientation), pixels*math.sin(self.orientation))

        if self.rect.x > windowWidth:
            self.rect.x = 0
        if self.rect.y > windowHeight:
            self.rect.y = 0
        if self.rect.x < 0:
            self.rect.x = windowWidth
        if self.rect.y < 0:
            self.rect.y = windowHeight

        print("move called")

    def rotate(self, angle):
        center = self.rect.center
        self.orientation += angle
        print("Rotating", angle, self.orientation)
        self.image = pygame.transform.rotate(self.original, self.orientation)
        self.rect = self.image.get_rect(center=center)

    def shoot(self):
        return Bullet(self.rect.center[0]+10, self.rect.y+10, self.orientation, self.id)

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y








