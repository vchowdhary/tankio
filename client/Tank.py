import pygame
import math
from client.Bullet import Bullet
from client.Settings import *


class Tank(pygame.sprite.Sprite):
    # Constructor for tank, pass in position and state
    # state = 0 if not shooting, 1 if shooting
    def __init__(self, x, y, angle, id):
        super().__init__()

        self.image = pygame.image.load("tank.png")
        self.image = pygame.transform.scale(self.image,(50,50))
        self.image.set_colorkey((0,0,0))
        self.original = self.image
        self.orientation = angle
        self.x = x
        self.y = y
        self.id = id
        self.health = 100
        self.hit_by = []

        self.rect = self.image.get_rect()
        self.rect.topleft = (x-20, y-30)

    def to_json(self):
        tank_json = {
            "type": "tank",
            "id": self.id,
            "center x": self.rect.center[0],
            "center y": self.rect.center[1],
            "rect x": self.rect.x,
            "rect y": self.rect.y,
            "orientation": self.orientation,
            "hit by": self.hit_by
        }
        return tank_json

    def move(self, pixels):
        orientation_rad = self.orientation*math.pi/180
        offset_x = pixels*math.cos(orientation_rad)
        offset_y = -1*pixels*math.sin(orientation_rad)

        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > windowWidth:
            self.rect.x = windowWidth - 20
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > windowHeight:
            self.rect.y = windowHeight - 50

        pygame.Rect.move_ip(self.rect, offset_x, offset_y)

    def rotate(self, angle):
        center = self.rect.center
        self.orientation += angle
        self.orientation %= 360

        self.image = pygame.transform.rotate(self.original, self.orientation)
        self.rect = self.image.get_rect(center=center)

    def rotate_fixed(self, angle):
        center = self.rect.center
        self.orientation = angle
        self.orientation %= 360
        self.image = pygame.transform.rotate(self.original, self.orientation)
        self.rect = self.image.get_rect(center=center)

    def shoot(self):
        orientation_rad = self.orientation*math.pi/180
        return Bullet(self.rect.center[0]+20*math.cos(orientation_rad),
                      self.rect.center[1]-20*math.sin(orientation_rad),
                      self.orientation, self.id)

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def check_hit(self, bullets):
        hit_list = pygame.sprite.spritecollide(self, bullets, True)
        self.health -= len(hit_list)
        self.hit_by = []
        for bullet in hit_list:
            self.hit_by.append(bullet.id)








